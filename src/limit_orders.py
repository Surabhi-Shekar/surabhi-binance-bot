import os, sys, logging
from client import BinanceFuturesClient
logger = logging.getLogger("BinanceBot.limit")

def limit_order(api_key, api_secret, symbol, side, quantity, price, tif="GTC"):
    client = BinanceFuturesClient(api_key, api_secret)
    res = client.place_order(symbol=symbol, side=side, type_="LIMIT", quantity=quantity,
                             price=price, timeInForce=tif)
    logger.info("Limit order response: %s", res)
    return res

