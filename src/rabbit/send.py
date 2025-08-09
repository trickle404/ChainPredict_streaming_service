import asyncio
import aio_pika
import logging
import json

async def send_msg_rabbit(data):
    try:
        connection = await aio_pika.connect_robust(
                "amqp://guest:guest@127.0.0.1/"
        )
        async with connection:
            routing_key = "msg"
            channel = await connection.channel()
            await channel.default_exchange.publish(
                    aio_pika.Message(body=json.dumps(data).encode('utf-8')),
                    routing_key = routing_key
            )
            logging.info(data)
    except Exception as e:
        logging.error(f"Error sent queue to Rabbit {e}")
