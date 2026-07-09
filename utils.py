

import json
import os

from config import SOURCE_FILE
from logger import logger


"""def load_sources():
    
    if os.path.exists(SOURCE_FILE):
        logger.error(f"Source file not found: {SOURCE_FILE}")
        return []

    try:
        with open(SOURCE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except Exception as error:
        logger.error(error)
        return []
"""
def load_sources():
    """
    Load news sources from JSON file.
    """

    if not os.path.exists(SOURCE_FILE):
        logger.error(f"Source file not found: {SOURCE_FILE}")
        return []

    try:
        with open(SOURCE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        logger.info(f"{len(data)} news source(s) loaded.")

        return data

    except json.JSONDecodeError:
        logger.error(f"Invalid JSON format: {SOURCE_FILE}")

    except Exception as error:
        logger.error(f"Error loading sources: {error}")

    return []

def print_headlines(headlines):
    
    print("\n" + "=" * 70)
    print("LATEST NEWS HEADLINES")
    print("=" * 70)

    if not headlines:
        print("No headlines found.")
        return

    for index, news in enumerate(headlines, start=1):

        print(f"\n{index}. {news['title']}")

        print(f"URL : {news['url']}")

        print(f"Published : {news['published_time']}")

        print("-" * 70)