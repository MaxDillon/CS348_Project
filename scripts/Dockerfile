FROM python:3.10

WORKDIR /scripts

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "fetchFinanceData.py" ]
