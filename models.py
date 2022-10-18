from database.base import Base, engine
from sqlalchemy import Column, String, Integer, Boolean

class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)