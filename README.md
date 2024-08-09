# Amaze

Amaze is a Scrapy tool designed for dynamic web scraping using Selenium and Scrapy. This project utilizes Selenium WebDriver (ChromeDriver) to handle dynamic content loading and ScrapeOps fake header middleware for request headers.

You can use the concept used here in middlewares to scrape your own custom data from your preferred dynamic website. This project particularly focuses on JioMart website which have dynamic loading of products (lazy loading) as well as dynamic content loading on a specific product page.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
- Dynamic web scraping using Selenium WebDriver.
- Handling of lazy-loaded content.
- ScrapeOps fake header middleware for rotating request headers.

## Requirements
- Python 3.x
- Scrapy
- Selenium
- ChromeDriver
- ScrapeOps Fake Header Middleware

## Installation

To set up this project, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Mridul-23/amaze.git
   cd amaze
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Download and configure ChromeDriver:**
   - [Download ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/)
   - Ensure ChromeDriver is in your PATH or specify its location in your Scrapy settings.

## Usage

To run the Scrapy spider, use the following command:

```sh
scrapy crawl <spider_name>
```

Replace `<spider_name>` with the name of your spider, which is defined in the `amaze/spiders` directory.

## Project Structure

- `.gitignore`: Lists files and directories ignored by Git.
- `requirements.txt`: Contains the Python dependencies for the project.
- `scrapy.cfg`: Configuration file for the Scrapy project.
- `amaze/`: Main directory containing the Scrapy project.
  - `spiders/`: Directory containing the spider definitions.
  - `items.py`: Defines the data structures for scraped items.
  - `middlewares.py`: Contains custom middlewares for the project.
  - `pipelines.py`: Defines item pipelines for processing scraped data.
  - `settings.py`: Project settings, including configuration for spiders, middlewares, and pipelines.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Scrapy](https://scrapy.org/) - An open-source and collaborative web crawling framework for Python.
- [Selenium](https://www.selenium.dev/) - A suite of tools for automating web browsers.
- [ScrapeOps](https://scrapeops.io/) - Provides useful tools and services for web scraping, including fake header middleware.
