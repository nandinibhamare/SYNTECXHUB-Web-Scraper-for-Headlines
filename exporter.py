

import csv
import json
import os

from config import (
    OUTPUT_FOLDER,
    CSV_FILE,
    JSON_FILE
)

from logger import logger


class Exporter:

    def __init__(self):
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    def save_json(self, headlines):

        try:
            with open(
                JSON_FILE,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    headlines,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            logger.info(f"JSON saved -> {JSON_FILE}")

        except Exception as error:
            logger.error(error)

    def save_csv(self, headlines):

        try:
            with open(
                CSV_FILE,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Title",
                    "URL",
                    "Published Time"
                ])

                for news in headlines:

                    writer.writerow([
                        news["title"],
                        news["url"],
                        news["published_time"]
                    ])

            logger.info(f"CSV saved -> {CSV_FILE}")

        except Exception as error:
            logger.error(error)