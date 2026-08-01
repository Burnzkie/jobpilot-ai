import requests

from app.scrapers.base import BaseScraper


class ArbeitnowScraper(BaseScraper):

    URL = "https://www.arbeitnow.com/api/job-board-api"

    def fetch_jobs(self):

        response = requests.get(self.URL, timeout=30)

        response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data["data"]:

            jobs.append(
                {
                    "title": job["title"],
                    "company": job["company_name"],
                    "location": (
                        ", ".join(job["location"])
                        if isinstance(job["location"], list)
                        else job["location"]
                    ),
                    "salary": None,
                    "description": job["description"],
                    "url": job["url"],
                    "source": "Arbeitnow",
                }
            )

        return jobs
