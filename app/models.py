import datetime

from sqlmodel import SQLModel, Field


class SongBase(SQLModel):
    name: str
    artist: str
    year: int = Field(default=2022)


class Song(SongBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
