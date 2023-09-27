FROM python:3.8.10

RUN pip3 install Flask gunicorn requests pyTelegramBotAPI

WORKDIR /.

COPY . .

ENV FLASK_APP ./gdp-chan/index.py
ENV BOT_TOKEN 626130318:AAF0CCD1hnKmnxhQCcZTHRSSC8jDlSeOXkQ
ENV PORT 8080
ENV SERVER_URL https://gdp-chan-p67toivrga-rj.a.run.app

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 gdp-chan.index:app
