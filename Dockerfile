FROM python:3.8.10-alpine3.12

ENV TZ="Asia/Calcutta"

RUN apk add --no-cache python3-dev tzdata\
    && pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r Requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
