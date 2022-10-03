#!/usr/bin/env python
# coding=utf-8
import pika
credentials = pika.PlainCredentials('user', 'user')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',5672,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        
channel.basic_consume(queue='hello', on_message_callback=callback)
#channel.basic_consume(callback, queue='hello' , no_ack = True)
channel.start_consuming()