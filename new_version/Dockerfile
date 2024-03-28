FROM python:3.11.3

WORKDIR /fastapi_structure

ADD . /fastapi_structure

ENV ALLOW_ORIGINS=http://0.0.0.0:3000

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]