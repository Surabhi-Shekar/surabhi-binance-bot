import os, sys, logging
from client import BinanceFuturesClient

logger = logging.getLogger("BinanceBot.market")

def market_order(api_key, api_secret, symbol, side, quantity):
    client = BinanceFuturesClient(api_key, api_secret)
    res = client.place_order(symbol=symbol, side=side, type_="MARKET", quantity=quantity)
    logger.info("Market order response: %s", res)
    return res

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py SYMBOL BUY|SELL QUANTITY")
        sys.exit(1)
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    _, symbol, side, quantity = sys.argv
    out = market_order(api_key, api_secret, symbol, side, quantity)
    print(out)

