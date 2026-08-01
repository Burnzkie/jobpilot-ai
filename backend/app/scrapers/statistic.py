from collections import Counter


def summarize(jobs):

    stats = Counter()

    for job in jobs:

        stats[job["source"]] += 1

    return dict(stats)
