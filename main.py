
from scraper import NewsScraper
from parser import NewsParser
from exporter import Exporter
from utils import load_sources, print_headlines
from logger import logger


def main():
    #print("=" * 60)
    print("        NewsPulse - Smart News Scraper")
    #print("=" * 60)

    keyword = input(
        "\nEnter keyword to filter news (Press Enter for all): "
    ).strip()

    sources = load_sources()

    if not sources:
        print("No news sources found.")
        return

    scraper = NewsScraper()
    parser = NewsParser()
    exporter = Exporter()

    all_headlines = []

    for source in sources:

        print(f"\nScraping: {source['name']}")

        logger.info(f"Started scraping {source['name']}")

        headlines = scraper.scrape(source["url"])

        all_headlines.extend(headlines)

    all_headlines = parser.remove_duplicates(all_headlines)

    if keyword:
        all_headlines = parser.filter_by_keyword(
            all_headlines,
            keyword
        )

    all_headlines = parser.sort_headlines(all_headlines)

    exporter.save_json(all_headlines)
    exporter.save_csv(all_headlines)

    print_headlines(all_headlines)

    print("\n")
    print("=" * 60)
    print(f"Total Headlines : {len(all_headlines)}")
    print("JSON Saved Successfully")
    print("CSV Saved Successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()