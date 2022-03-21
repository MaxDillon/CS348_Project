FROM python:3

WORKDIR /app

ENV FLASK_ENV=development
ENV FLASK_APP=app.py
ENV PATH="/app/bin:${PATH}"

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]