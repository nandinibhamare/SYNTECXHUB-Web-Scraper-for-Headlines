

import re
from logger import logger


class NewsParser:
    """
    Provides methods to filter, remove duplicates,
    and sort scraped news headlines.
    """

    @staticmethod
    def remove_duplicates(headlines):
        
        unique = []
        seen = set()

        for item in headlines:

            title = item["title"].strip().lower()

            if title not in seen:
                seen.add(title)
                unique.append(item)

        logger.info(
            f"Duplicate removal completed. Total: {len(unique)}"
        )

        return unique

    @staticmethod
    def filter_by_keyword(headlines, keyword):
        

        if not keyword:
            return headlines

        keywords = keyword.lower().split()

        filtered = []

        for item in headlines:

            title = item["title"].lower()

            # Extract words only
            words = re.findall(r"\b[\w'-]+\b", title)

            # Match any keyword as a whole word
            if any(keyword in words for keyword in keywords):
                filtered.append(item)

        logger.info(
            f"Keyword '{keyword}' -> {len(filtered)} result(s)."
        )

        return filtered

    @staticmethod
    def sort_headlines(headlines):
        """
        Sort headlines alphabetically.
        """

        headlines.sort(
            key=lambda item: item["title"].lower()
        )

        logger.info("Headlines sorted alphabetically.")

        return headlines