#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('user', 'user')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',5672,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
connection.close()