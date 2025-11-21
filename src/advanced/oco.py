import os, sys, logging
from client import BinanceFuturesClient

def oco_order(api_key, api_secret, symbol, side, quantity, tp_price, stop_price, stop_limit_price):
    client = BinanceFuturesClient(api_key, api_secret)
    opposite = "SELL" if side.upper()=="BUY" else "BUY"

    tp = client.place_order(symbol, opposite, "LIMIT", quantity, price=tp_price, timeInForce="GTC")
    sl = client.place_order(symbol, opposite, "STOP_LOSS_LIMIT", quantity, price=stop_limit_price,
                            stopPrice=stop_price, timeInForce="GTC")
    return {"take_profit": tp, "stop_limit": sl}

