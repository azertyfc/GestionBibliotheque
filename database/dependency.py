from database.session import SessionLocal

def get_db():
    """Get a database session.
    
    This function provides a database session for interacting with the database.
    It uses a context manager to ensure that the session is properly closed after use.
    
    Yields:
        Session: A SQLAlchemy session object for database operations.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()