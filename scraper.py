

import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from base_scraper import BaseScraper
from config import HEADERS, REQUEST_TIMEOUT, REQUEST_DELAY
from logger import logger
from robots_checker import is_scraping_allowed
from retry_handler import retry_request


class NewsScraper(BaseScraper):

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def fetch_page(self, url):
        

        if not is_scraping_allowed(url):
            logger.warning(f"Scraping not allowed: {url}")
            return None

        try:
            logger.info(f"Connecting to {url}")

            response = retry_request(
                self.session,
                url,
                retries=3,
                timeout=REQUEST_TIMEOUT
            )

            if response is None:
                return None

            time.sleep(REQUEST_DELAY)

            return response.text

        except requests.exceptions.Timeout:
            logger.error(f"Request timed out: {url}")

        except requests.exceptions.ConnectionError:
            logger.error(f"Connection failed: {url}")

        except requests.exceptions.HTTPError as error:
            logger.error(f"HTTP Error: {error}")

        except Exception as error:
            logger.error(f"Unexpected Error: {error}")

        return None

    def parse_headlines(self, html, base_url):
        

        soup = BeautifulSoup(html, "lxml")

        headlines = []
        seen = set()

        ignore_titles = {
            "News",
            "Sport",
            "Sports",
            "Live",
            "Video",
            "Videos",
            "Weather",
            "Entertainment",
            "Business",
            "Travel",
            "More",
            "Menu"
        }

        tags = soup.find_all(["h1", "h2", "h3"])

        for tag in tags:

            title = tag.get_text(" ", strip=True)

            if not title:
                continue

            if len(title) < 12:
                continue

            if title in ignore_titles:
                continue

            if title.lower() in seen:
                continue

            seen.add(title.lower())

            link = ""

            parent = tag.find_parent("a")

            if parent and parent.get("href"):
                link = urljoin(base_url, parent["href"])

            elif tag.find("a"):

                href = tag.find("a").get("href")

                if href:
                    link = urljoin(base_url, href)

            # Try to extract published time
            published = "Not Available"

            time_tag = tag.find_next("time")

            if time_tag:

                published = (
                    time_tag.get("datetime")
                    or time_tag.get_text(strip=True)
                    or "Not Available"
                )

            headlines.append({
                "title": title,
                "url": link,
                "published_time": published
            })

        logger.info(f"{len(headlines)} headlines extracted.")

        return headlines

    def scrape(self, url):
        

        html = self.fetch_page(url)

        if html is None:
            return []

        return self.parse_headlines(html, url)