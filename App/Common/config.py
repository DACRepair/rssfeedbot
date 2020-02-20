from os import getcwd as _getcwd
from os import getenv as _getenv
from os.path import normpath as _normpath

SUBREDDIT: str = _getenv("SUBREDDIT", "")
WEBHOOK_URL: str = _getenv("WEBHOOK_URL", "")

DB_URI: str = _getenv("DB_URI", "sqlite:///" + (_normpath(_getcwd() + "/app.db")))

FEED_LIMIT: int = int(_getenv("FEED_LIMIT", 100))
REFRESH_TIME: int = int(_getenv("REFRESH_TIME", 60))

POST: bool = _getenv("POST", "true").lower() == "true"
FEED: bool = _getenv("FEED_ONLY", "true").lower() == "true"
