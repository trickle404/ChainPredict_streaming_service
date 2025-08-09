import os
from src.rabbit.send import send_msg_rabbit
from binance import AsyncClient, BinanceSocketManager
from binance.enums import KLINE_INTERVAL_5MINUTE
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('BINANCE_API_KEY')
SECRET_KEY = os.getenv('BINANCE_SECRET_KEY')


async def websocket_client():
    client = await AsyncClient.create(API_KEY, SECRET_KEY)
    bm = BinanceSocketManager(client)
    ks = bm.kline_socket("BTCUSDT", interval=KLINE_INTERVAL_5MINUTE)
    async with ks as kscm:
        while True:
            res = await kscm.recv()
            await send_msg_rabbit(res)  # Lisiting data from Binance socket 
                        # After Include MongoDB for writting data to Mongo
    await client.close_connection()

