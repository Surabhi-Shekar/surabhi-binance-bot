import os, sys, logging
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler(str(Path(__file__).resolve().parent.parent / "bot.log")),
        logging.StreamHandler()
    ],
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def print_help():
    print("""
Usage:
  python src/main.py market SYMBOL BUY|SELL QTY
  python src/main.py limit SYMBOL BUY|SELL QTY PRICE
  python src/main.py stop_limit SYMBOL BUY|SELL QTY STOP LIMIT
  python src/main.py oco SYMBOL BUY|SELL QTY TP STOP SL_LIMIT
  python src/main.py twap SYMBOL BUY|SELL TOTAL_QTY CHUNKS INTERVAL
""")

def main(args):
    if len(args) < 1:
        print_help()
        return

    cmd = args[0]
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if cmd == "market":
        from market_orders import market_order
        _, symbol, side, qty = args
        print(market_order(api_key, api_secret, symbol, side, qty))

    elif cmd == "limit":
        from limit_orders import limit_order
        _, symbol, side, qty, price = args
        print(limit_order(api_key, api_secret, symbol, side, qty, price))

    elif cmd == "stop_limit":
        from advanced.stop_limit import stop_limit_order
        _, symbol, side, qty, sp, lp = args
        print(stop_limit_order(api_key, api_secret, symbol, side, qty, sp, lp))

    elif cmd == "oco":
        from advanced.oco import oco_order
        _, symbol, side, qty, tp, sp, slp = args
        print(oco_order(api_key, api_secret, symbol, side, qty, tp, sp, slp))

    elif cmd == "twap":
        from advanced.twap import twap_order
        _, symbol, side, total, chunks, interval = args
        print(twap_order(api_key, api_secret, symbol, side, total, chunks, interval))

    else:
        print_help()

if __name__ == "__main__":
    main(sys.argv[1:])

