from apscheduler.schedulers.background import BackgroundScheduler

from app.scheduler.tasks import import_jobs_task

scheduler = BackgroundScheduler()


def start_scheduler():

    if not scheduler.running:

        scheduler.add_job(
            import_jobs_task,
            trigger="interval",
            minutes=60,
            id="heartbeat",
            replace_existing=True,
        )

        scheduler.start()

        print("✅ Job Scheduler Started")


def stop_scheduler():
    """
    Stop the scheduler when FastAPI shuts down.
    """

    if scheduler.running:
        scheduler.shutdown()
        print("🛑 Job Scheduler Stopped")
