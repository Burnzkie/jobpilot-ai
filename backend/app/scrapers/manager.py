import logging

from app.scrapers.arbeitnow import ArbeitnowScraper
from app.scrapers.remotive import RemotiveScraper

logger = logging.getLogger(__name__)


SCRAPERS = [
    RemotiveScraper(),
    ArbeitnowScraper(),
]


class ScraperManager:

    def fetch_all(self):

        jobs = []

        for scraper in SCRAPERS:

            try:

                data = scraper.fetch_jobs()

                jobs.extend(data)

                logger.info(
                    "%s imported %d jobs", scraper.__class__.__name__, len(data)
                )

            except Exception:

                logger.exception("%s failed", scraper.__class__.__name__)

        unique = {}

        for job in jobs:

            unique[job["url"]] = job

        return list(unique.values())
