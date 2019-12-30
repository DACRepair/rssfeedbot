from App.Models import Base
from App.tasks import app, post, store
from App.Common.config import POST, FEED

if __name__ == "__main__":
    try:
        Base.metadata.create_all()

        if FEED:
            app.create_task(store())
        if POST:
            app.create_task(post())
        app.run_forever()
    except:
        exit(1)
