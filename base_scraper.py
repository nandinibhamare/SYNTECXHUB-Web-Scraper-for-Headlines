


from abc import ABC, abstractmethod


class BaseScraper(ABC):
    

    @abstractmethod
    def fetch_page(self, url):
        pass

    @abstractmethod
    def parse_headlines(self, html, base_url):
        pass

    @abstractmethod
    def scrape(self, url):
        pass