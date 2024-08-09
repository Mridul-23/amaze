# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from urllib.parse import urlencode
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time, random, requests, logging



class SeleniumMiddleware:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def process_request(self, request, spider):
        self.driver.get(request.url)

        if "/c/" in request.url:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".plp-card-wrapper"))
                )
            except Exception as e:
                spider.logger.error(f"Error waiting for element: {e}")

            total_items = 0
            while total_items < 100:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                new_items = len(self.driver.find_elements(By.CSS_SELECTOR, ".plp-card-wrapper"))
                if new_items == total_items:
                    break
                total_items = new_items

                spider.logger.info(f"Loaded {total_items} items")

        elif "/p/" in request.url:
            try:
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#pdp_product_name"))
                )
            except Exception as e:
                spider.logger.error(f"Error waiting for product detail element: {e}")

        else:
            spider.logger.warning(f"Unknown page type for URL: {request.url}")

        body = self.driver.page_source
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

    def __del__(self):
        self.driver.quit()



class ScrapeOpsFakeBrowserHeaderAgentMiddleware:
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):
        self.scrapeops_api_key = 'api-key' # Replace with your ScrapeOps API key
        self.scrapeops_endpoint = 'http://headers.scrapeops.io/v1/browser-headers'
        self.scrapeops_fake_browser_headers_active = True
        self.scrapeops_num_results = 1
        self.headers_list = []
        self._get_headers_list()
        self._scrapeops_fake_browser_headers_enabled()

    def _get_headers_list(self):
        try:
            payload = {'api_key': self.scrapeops_api_key}
            if self.scrapeops_num_results is not None:
                payload['num_results'] = str(self.scrapeops_num_results)  # Convert to string
            response = requests.get(self.scrapeops_endpoint, params=urlencode(payload))
            response.raise_for_status()  # Raise an exception for non-2xx responses
            json_response = response.json()
            self.headers_list = json_response.get('result', [])
        except (requests.RequestException, ValueError) as e:
            self.headers_list = []  # Set empty list on failure
            logging.error(f"Failed to fetch headers list: {e}")

    def _scrapeops_fake_browser_headers_enabled(self):
        if not self.scrapeops_api_key or not self.scrapeops_fake_browser_headers_active:
            self.scrapeops_fake_browser_headers_active = False

    def process_request(self, request, spider):
        if not self.scrapeops_fake_browser_headers_active or not self.headers_list:
            return  # Skip if headers are disabled or not fetched

        random_browser_header = random.choice(self.headers_list)

        for header_name, header_value in random_browser_header.items():
            request.headers[header_name] = str(header_value)  # Convert header_value to string

        print("****************** NEW HEADER ATTACHED ****************")
        print(request.headers)