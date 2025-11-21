import os
import sys
import logging
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
  CLI Mode (interactive):
      python src/main.py

Direct Command Mode:
      python src/main.py market SYMBOL BUY|SELL QTY
      python src/main.py limit SYMBOL BUY|SELL QTY PRICE
      python src/main.py stop_limit SYMBOL BUY|SELL QTY STOP_PRICE LIMIT_PRICE
      python src/main.py oco SYMBOL BUY|SELL QTY TP STOP SL_LIMIT
      python src/main.py twap SYMBOL BUY|SELL TOTAL_QTY CHUNKS INTERVAL
""")


# Interactive CLI

def interactive_menu():
    print("\n=== Binance Futures Trading Bot ===")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. Stop-Limit Order")
    print("4. OCO Order")
    print("5. TWAP Strategy")
    print("0. Exit")
    choice = input("Choose an option: ")
    return choice


def main(args):
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("Error: API keys not found. Set BINANCE_API_KEY and BINANCE_API_SECRET.")
        exit(1)

    if len(args) == 0:
        choice = interactive_menu()

        if choice == "1":
            from market_orders import market_order
            symbol = input("Symbol (e.g., BTCUSDT): ")
            side = input("Side (BUY/SELL): ")
            qty = input("Quantity: ")
            print(market_order(api_key, api_secret, symbol, side, qty))

        elif choice == "2":
            from limit_orders import limit_order
            symbol = input("Symbol: ")
            side = input("Side: ")
            qty = input("Quantity: ")
            price = input("Limit Price: ")
            print(limit_order(api_key, api_secret, symbol, side, qty, price))

        elif choice == "3":
            from advanced.stop_limit import stop_limit_order
            symbol = input("Symbol: ")
            side = input("Side: ")
            qty = input("Quantity: ")
            sp = input("Stop Price: ")
            lp = input("Limit Price: ")
            print(stop_limit_order(api_key, api_secret, symbol, side, qty, sp, lp))

        elif choice == "4":
            from advanced.oco import oco_order
            symbol = input("Symbol: ")
            side = input("Side: ")
            qty = input("Quantity: ")
            tp = input("Take-Profit Price: ")
            sp = input("Stop Price: ")
            slp = input("Stop-Limit Price: ")
            print(oco_order(api_key, api_secret, symbol, side, qty, tp, sp, slp))

        elif choice == "5":
            from advanced.twap import twap_order
            symbol = input("Symbol: ")
            side = input("Side: ")
            total = input("Total Quantity: ")
            chunks = input("Chunks: ")
            interval = input("Interval (seconds): ")
            print(twap_order(api_key, api_secret, symbol, side, total, chunks, interval))

        elif choice == "0":
            print("Goodbye!")
            exit()

        else:
            print("Invalid choice!")
            print_help()

        return

    cmd = args[0]

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
