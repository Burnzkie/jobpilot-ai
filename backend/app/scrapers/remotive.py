import requests

from app.scrapers.base import BaseScraper


class RemotiveScraper(BaseScraper):

    URL = "https://remotive.com/api/remote-jobs"

    def fetch_jobs(self):

        response = requests.get(self.URL, timeout=30)

        data = response.json()

        jobs = []

        for job in data["jobs"]:

            jobs.append(
                {
                    "title": job["title"],
                    "company": job["company_name"],
                    "location": job["candidate_required_location"],
                    "description": job["description"],
                    "url": job["url"],
                    "source": "Remotive",
                }
            )

        return jobs
