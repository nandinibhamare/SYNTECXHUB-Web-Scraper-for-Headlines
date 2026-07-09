

from urllib.parse import urlparse


def validate_url(url):

    try:
        result = urlparse(url)

        return all([result.scheme, result.netloc])

    except Exception:
        return False


def validate_source(source):

    required = ["name", "url"]

    return all(key in source for key in required)