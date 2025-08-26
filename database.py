from sqlmodel import SQLModel, create_engine, Session

# Database configuration
DATABASE_URL = "sqlite:///task.db"

# Main connection with database
engine = create_engine(DATABASE_URL, echo=True) ####!!!!!!schrijf over echo: log alle ruwe sql statements in terminal, wil je dit wel?

def init_db() -> None:
    """Initialise database and create tables in SQLModel MetaData."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Generate new database session for every request."""
    with Session(engine) as session:
        yield session
 
close_db = engine.dispose()