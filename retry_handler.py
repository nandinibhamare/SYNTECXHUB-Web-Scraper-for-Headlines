

import time
import requests

from logger import logger


def retry_request(session, url, retries=3, timeout=10):
    """
    Retry HTTP requests if they fail.
    """

    for attempt in range(1, retries + 1):

        try:
            response = session.get(url, timeout=timeout)

            response.raise_for_status()

            return response

        except requests.RequestException as error:

            logger.warning(
                f"Attempt {attempt}/{retries} failed: {error}"
            )

            if attempt < retries:
                time.sleep(2)

    logger.error("Maximum retry limit reached.")

    return None