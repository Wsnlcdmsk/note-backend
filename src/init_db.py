from src.config import engine
from src.models import Base


def init_db():
    Base.metadata.create_all(bind=engine)
