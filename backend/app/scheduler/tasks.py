from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.services.import_service import ImportService


def import_jobs_task():
    """
    Background task that imports jobs automatically.
    """

    print("\n========== Job Import Started ==========")

    db: Session = SessionLocal()

    try:

        service = ImportService(db)

        result = service.import_jobs()

        print("Import Finished")

        print(result)

    except Exception as e:

        print("Scheduler Error:")

        print(e)

    finally:

        db.close()

        print("Database Closed")

        print("=======================================\n")
