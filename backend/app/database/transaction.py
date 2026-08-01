from contextlib import contextmanager


@contextmanager
def transaction(db):

    try:

        yield

        db.commit()

    except Exception:

        db.rollback()

        raise
