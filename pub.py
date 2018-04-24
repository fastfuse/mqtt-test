# from paho.mqtt.client import Client
#
#
# client = Client()
#
# # client.connect("test.mosquitto.org", 1883)
# # client.connect("iot.eclipse.org", 1883)
#
# client.connect("broker.hivemq.com")
#
# r = client.publish(topic="my/test", payload="Hello MQTT")
#
# print(f"{r}")


import paho.mqtt.publish as publish

# publish.single(topic, payload=None, qos=0, retain=False, hostname="localhost",
#                port=1883, client_id="", keepalive=60, will=None, auth=None,
#                tls=None, protocol=mqtt.MQTTv31)

publish.single(topic="my/test", payload="qweqweqweqweqwe",
               hostname="broker.hivemq.com")
