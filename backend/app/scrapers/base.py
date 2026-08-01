from abc import ABC, abstractmethod


class BaseScraper(ABC):

    @abstractmethod
    def fetch_jobs(self):
        """
        Return a list of normalized jobs.
        """
        pass
