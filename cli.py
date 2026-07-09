
import argparse


def get_arguments():

    parser = argparse.ArgumentParser(
        description="NewsPulse Smart Web Scraper"
    )

    parser.add_argument(
        "--keyword",
        type=str,
        default="",
        help="Filter news using keyword"
    )

    parser.add_argument(
        "--format",
        choices=["json", "csv", "both"],
        default="both",
        help="Export format"
    )

    parser.add_argument(
        "--source",
        type=str,
        default="all",
        help="Scrape specific source"
    )

    return parser.parse_args()