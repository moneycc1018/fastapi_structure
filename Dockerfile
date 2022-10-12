FROM python:3.8.9

WORKDIR /fastapi_structure

ADD . /fastapi_structure

ENV ALLOW_ORIGINS=http://0.0.0.0:3333
ENV TEST=MONEY

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]