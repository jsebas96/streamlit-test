import random
import json
from datetime import datetime
from paho.mqtt import client as mqtt_client
from config.index import config
from database.mongo_client import db_collection

# Functions to handle MQTT events


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("electric-meter")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    data = json.loads(msg.payload)
    if "date" in data:
        data['date'] = datetime.fromtimestamp(data['date'])
    else:
        data['date'] = datetime.now()
    db_collection.insert_one(data)


# Generate a random client ID
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# Create a new MQTT client instance
client = mqtt_client.Client(client_id=client_id)
client.username_pw_set(
    username=config["USER"], password=config["PWD"])
client.connect_async(config['HOST'], int(config['PORT']),
               keepalive=60)  # Connect to the MQTT broker

client.on_connect = on_connect  # Attach the on_connect function to the client
client.on_message = on_message  # Attach the on_message function to the client

client.loop_start()  # Start the MQTT client loop
