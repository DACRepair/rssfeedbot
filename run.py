from App.Models import Base
from App.tasks import app, post, store
from App.Common.config import POST_ONLY, FEED_ONLY

if __name__ == "__main__":
    try:
        Base.metadata.create_all()

        if FEED_ONLY:
            app.create_task(store())
        if POST_ONLY:
            app.create_task(post())
        app.run_forever()
    except:
        exit(1)
