FROM python:3.6-alpine

ENV SUBREDDIT ""
ENV WEBHOOK_URL ""
ENV DB_URI sqlite///./test.db

ENV FEED_LIMIT 100
ENV REFRESH_TIME 100

ENV POST True
ENV FEED True

WORKDIR /usr/src/rssfeedbot
COPY App/ /usr/src/rssfeedbot/App
COPY run.py /usr/src/rssfeedbot/
COPY requirements.txt /usr/src/rssfeedbot/


RUN apk --no-cache add --virtual build postgresql-dev gcc python3-dev musl-dev \
    && pip install -r requirements.txt \
    && pip install psycopg2-binary \
    && apk del build

CMD python3 ./run.py