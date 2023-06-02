import os
import threading
import winsound
import paho.mqtt.client as mqtt
from win10toast import ToastNotifier

MQTT_BROKER = os.environ.get('MQTT_BROKER', '192.168.1.61')
MQTT_PORT = int(os.environ.get('MQTT_PORT', '1883'))
MQTT_TOPIC = os.environ.get('MQTT_TOPIC', '2da58838-665a-42e6-bca6-2e5d3690422e')

POPUP_TITLE = "Hello!"
POPUP_MESSAGE = "Come downstairs please!"
SOUND_EFFECT_PATH = r"C:\Windows\Media\Ring04.wav"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker, waiting for messages.")
        client.subscribe(MQTT_TOPIC)
    else:
        print("Failed to connect to MQTT broker")


def on_message(client, userdata, msg):
    print("Message received")

    def play_sound():
        print("Playing sound")
        winsound.PlaySound(SOUND_EFFECT_PATH, winsound.SND_FILENAME)
    sound_thread = threading.Thread(target=play_sound)
    sound_thread.start()

    print("Showing toast")
    toaster.show_toast(
        title=POPUP_TITLE,
        msg=POPUP_MESSAGE,
        duration=30,
        icon_path="icon.ico",
        threaded=True)


def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT broker")


toaster = ToastNotifier()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_forever()
