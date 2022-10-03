FROM python:latest

WORKDIR /code
# Install dependencies
RUN pip install pika
COPY ./  .


CMD ["python","-u", "producer.py"]

CMD ["tail", "-f", "/dev/null"]