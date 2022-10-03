#!/bin/bash
apt update
apt install -y python3-venv python3-pip

sleep  10
#if [[ `pip` =~ "${+,*} not found" ]] then
pip install pika
#fi


echo "
172.24.0.10 rmq01
172.24.0.11 rmq02
" >> /etc/hosts
# 
# 
rabbitmqctl set_policy ha-all "" \
  '{"ha-mode":"all","ha-sync-mode":"automatic"}'
#   
# rabbitmqctl set_policy ha-all ""
# '{"ha-mode":"all","ha-sync-mode":"automatic"}'