from App.Common.config import SUBREDDIT, FEED_LIMIT, WEBHOOK_URL, REFRESH_TIME
from App.Common.discord import Discord
from App.Common.reddit import Reddit
from App.Common.storage import Session
from App.Models import FeedEntry

from time import sleep
import asyncio

app = asyncio.get_event_loop()


def bootstrap():
    while True:
        if app.is_running():
            return True
        else:
            sleep(1)


def store_entries():
    ses = Session()
    reddit = Reddit(SUBREDDIT)

    entries = reddit.get_posts(FEED_LIMIT)
    for entry in entries:
        exists = ses.query(FeedEntry).filter(FeedEntry.post_id == entry.id).count() > 0
        if not exists and not entry.sticky:
            print("Stored: {}".format(entry))
            ses.add(FeedEntry(post_id=entry.id,
                              title=entry.title,
                              author=entry.author,
                              post=entry.post,
                              posted_on=entry.posted_on,
                              text=entry.text,
                              link=entry.link,
                              thumb=entry.thumb,
                              sticky=entry.sticky,
                              nsfw=entry.nsfw,
                              flair=entry.flair,
                              posted=False))
            ses.commit()
    ses.close()


def send_entries():
    ses = Session()

    results = ses.query(FeedEntry).filter(~FeedEntry.posted).filter(~FeedEntry.nsfw).filter(~FeedEntry.sticky)
    results = [x for x in results.order_by(FeedEntry.posted_on.asc()).all()]

    length = len(results)
    mod = 1 if length % 10 > 0 else 0
    for x in range(int(length / 10 + mod)):
        entries = results[x * 10: x * 10 + 9]
        discord = Discord(WEBHOOK_URL)
        discord.post_entries(entries)
        for entry in entries:
            entry.posted = True
            ses.commit()
        sleep(2)


async def store():
    while bootstrap():
        store_entries()
        await asyncio.sleep(REFRESH_TIME)


async def post():
    while bootstrap():
        send_entries()
        await asyncio.sleep(10)
