#!/usr/bin/env python

import os
import logging
from flask import Flask, request, abort
from paho.mqtt import publish

AUTH_TOKEN = os.environ.get('AUTH_TOKEN', '6136a6c5-619b-4554-bad8-5aef3ffa9aa7')
HTTP_PORT = int(os.environ.get('HTTP_PORT', '8080'))
MQTT_BROKER = os.environ.get('MQTT_BROKER', '192.168.1.61')
MQTT_PORT = int(os.environ.get('MQTT_PORT', '1883'))
MQTT_TOPIC = os.environ.get('MQTT_TOPIC', '2da58838-665a-42e6-bca6-2e5d3690422e')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)


@app.route('/', methods=['POST'])
def generate_mqtt_message():
    auth_header = request.headers.get('Authorization')
    if auth_header != AUTH_TOKEN:
        logging.warning('Invalid Authorization header')
        abort(403)
    message = request.get_data().decode('utf-8')
    logging.info(f'Request payload: {message}')
    publish.single(topic=MQTT_TOPIC, payload=message, hostname=MQTT_BROKER, port=MQTT_PORT)
    return 'MQTT message published successfully!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=HTTP_PORT)
