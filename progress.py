

import sys
import time


class ProgressBar:

    @staticmethod
    def show(current, total, source_name):

        percent = (current / total) * 100

        bar_length = 30

        filled = int(bar_length * current // total)

        bar = "█" * filled + "-" * (bar_length - filled)

        sys.stdout.write(
            f"\r[{bar}] {percent:.0f}% | Scraping: {source_name}"
        )

        sys.stdout.flush()

        time.sleep(0.2)

        if current == total:
            print()