

from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

from logger import logger


def is_scraping_allowed(url, user_agent="*"):
    """
    Check whether scraping is allowed by robots.txt.

    Parameters
    ----------
    url : str
        Website URL

    user_agent : str
        User-Agent string

    Returns
    -------
    bool
        True if scraping is allowed, otherwise False.
    """

    try:
        parsed = urlparse(url)

        robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

        parser = RobotFileParser()
        parser.set_url(robots_url)
        parser.read()

        allowed = parser.can_fetch(user_agent, url)

        if allowed:
            logger.info(f"Scraping allowed: {url}")
        else:
            logger.warning(f"Scraping not allowed by robots.txt: {url}")

        return allowed

    except Exception as error:
        logger.warning(
            f"Could not read robots.txt: {error}"
        )

        # Continue scraping if robots.txt cannot be accessed
        return True