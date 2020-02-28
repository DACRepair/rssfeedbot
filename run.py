from App.Common.config import POST, FEED, DIRTY
from App.Models import Base
from App.tasks import app, post, store, dirty_fix

if __name__ == "__main__":
    try:
        Base.metadata.create_all()

        if FEED:
            app.create_task(store())
        if POST:
            app.create_task(post())

        if DIRTY > 0:
            app.create_task(dirty_fix())

        app.run_forever()
    except:
        exit(1)
