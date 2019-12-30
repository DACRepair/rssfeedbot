from App.Models import Base
from App.tasks import app, post, store

if __name__ == "__main__":
    try:
        Base.metadata.create_all()

        app.create_task(store())
        app.create_task(post())
        app.run_forever()
    except:
        exit(1)
