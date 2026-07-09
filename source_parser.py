

from bs4 import BeautifulSoup


class SourceParser:

    @staticmethod
    def parse_bbc(html):

        soup = BeautifulSoup(html, "lxml")

        headlines = []

        for item in soup.select("h2"):

            text = item.get_text(strip=True)

            if len(text) > 8:

                headlines.append({
                    "title": text,
                    "url": "",
                    "published_time": "Not Available"
                })

        return headlines

    @staticmethod
    def parse_reuters(html):

        soup = BeautifulSoup(html, "lxml")

        headlines = []

        for item in soup.select("h3"):

            text = item.get_text(strip=True)

            if len(text) > 8:

                headlines.append({
                    "title": text,
                    "url": "",
                    "published_time": "Not Available"
                })

        return headlines

    @staticmethod
    def parse_generic(html):

        soup = BeautifulSoup(html, "lxml")

        headlines = []

        for tag in soup.find_all(["h1", "h2", "h3"]):

            text = tag.get_text(strip=True)

            if len(text) > 8:

                headlines.append({
                    "title": text,
                    "url": "",
                    "published_time": "Not Available"
                })

        return headlines