import time, logging, os, sys
from client import BinanceFuturesClient

logger = logging.getLogger("BinanceBot.twap")

def twap_order(api_key, api_secret, symbol, side, total_qty, chunks, interval):
    client = BinanceFuturesClient(api_key, api_secret)

    chunks = int(chunks)
    interval = int(interval)
    total_qty = float(total_qty)

    chunk_qty = total_qty / chunks
    results = []

    for i in range(chunks):
        res = client.place_order(symbol, side, "MARKET", chunk_qty)
        logger.info(f"TWAP chunk {i+1}/{chunks}: {res}")
        results.append(res)

        if i < chunks - 1:
            time.sleep(interval)

    return results


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) != 6:
        print("Usage: python twap.py SYMBOL BUY|SELL TOTAL_QTY CHUNKS INTERVAL_SECONDS")
        sys.exit(1)

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    _, symbol, side, total_qty, chunks, interval = sys.argv
    out = twap_order(api_key, api_secret, symbol, side, total_qty, chunks, interval)
    print(out)

