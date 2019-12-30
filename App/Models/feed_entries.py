import datetime
from App.Common.storage import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String


class FeedEntry(Base):
    __tablename__ = "feed_entries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(String(24), unique=True)

    title = Column(String(255))
    author = Column(String(255))

    post = Column(String(255))
    posted_on = Column(DateTime, default=datetime.datetime.utcnow())
    text = Column(String(4096))

    link = Column(String(255))
    flair = Column(String(255))
    thumb = Column(String(255))
    sticky = Column(Boolean, default=False)
    nsfw = Column(Boolean, default=False)

    posted = Column(Boolean, default=False)
