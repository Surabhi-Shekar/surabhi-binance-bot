import os, sys, logging
from client import BinanceFuturesClient
logger = logging.getLogger("BinanceBot.stoplimit")

def stop_limit_order(api_key, api_secret, symbol, side, quantity, stop_price, limit_price, tif="GTC"):
    client = BinanceFuturesClient(api_key, api_secret)
    return client.place_order(
        symbol, side, "STOP_LOSS_LIMIT",
        quantity=quantity,
        price=limit_price,
        stopPrice=stop_price,
        timeInForce=tif
    )

