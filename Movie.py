from sqlalchemy import String, Date
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

class Movie(Base):

    __tablename__ = "movies"


    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128), unique=True)
    director: Mapped[str] = mapped_column(String(64))
    release_date: Mapped[datetime.date] = mapped_column(Date)
    duration: Mapped[int] = mapped_column() # in minutes
    genre: Mapped[str] = mapped_column(String(32))
    rating: Mapped[float] = mapped_column()

    def __repr__(self):
        return f'Movie({self.id}, "{self.title}")'



load_dotenv()
engine = create_async_engine(
    "sqlite+aiosqlite:///myfile.db", connect_args={"autocommit": False}
)
