

import os


REQUEST_TIMEOUT = 10
REQUEST_DELAY = 2


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/126.0 Safari/537.36"
    )
}


OUTPUT_FOLDER = "output"


LOG_FOLDER = "logs"


SOURCE_FILE = "sources/news_sources.json"


CSV_FILE = os.path.join(OUTPUT_FOLDER, "headlines.csv")


JSON_FILE = os.path.join(OUTPUT_FOLDER, "headlines.json")

LOG_FILE = os.path.join(LOG_FOLDER, "scraper.log")