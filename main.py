import json
import pika, logging
from config import *
from performer import *

def on_message(channel, method_frame, header_frame, body):
    body = json.loads(body)
    send = body["NAME"] = perform(body["NAME"])
    send_to_queve(body)
    LOG.info(f'Message "{send}" has been sent')
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

def send_to_queve(data):
    qn = channel.queue_declare(SET['queue_above'])
    qn_name = qn.method.queue

    channel.basic_publish(exchange='', routing_key=qn_name, body=json.dumps(data))


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)

    credentials = pika.PlainCredentials(SET['name'], SET['passwd'])
    parameters = pika.ConnectionParameters(SET['server'], SET['port'], '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    q = channel.queue_declare(SET['queue_current'])
    q_name = q.method.queue

    # Turn on delivery confirmations
    channel.confirm_delivery()

    channel.basic_consume(on_message, SET['queue_current'])

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()

    #connection.close()
