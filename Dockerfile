FROM python:3.11
WORKDIR /app

COPY wheels /wheels
COPY requirements.txt .

RUN pip install --find-links=/wheels -r requirements.txt

COPY server/ server/
ENV FLASK_APP=server/app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD ["flask", "run"]

