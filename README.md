
# Binance Futures Trading Bot Using Python

A modular trading bot built using the *inance Demo (replacement for the old Testnet) Futures API .  
Supports "Market", "Limit", "Stop-Limit", "OCO", and "TWAP" trading, with full logging, API signing, and an interactive CLI UI.


## Features

- Connects to Binance Demo Futures (Testnet equivalent)
- Supports:
  - Market Orders
  - Limit Orders
- Both 'BUY' and 'SELL' sides
- Uses 'official REST endpoints' with proper HMAC SHA-256 signing
- Command-line interface with argument support
- Full logging of requests, responses, and errors
- Clean, reusable, modular code structure

# Bonus Features
- Stop-Limit Orders
- OCO (One-Cancels-Other)
- TWAP Strategy (Time-Weighted Average Price)
- Interactive CLI UI menu for easy trading

---

# Project Structure


surabhi_binance_bot/
│
├── src/
│   ├── main.py                # Interactive CLI + command router
│   ├── client.py              # REST API client with signing
│   ├── market_orders.py       # Market Buy/Sell
│   ├── limit_orders.py        # Limit Buy/Sell
│   ├── advanced/
│   │   ├── stop_limit.py      # Stop-Limit orders
│   │   ├── oco.py             # OCO orders
│   │   └── twap.py            # TWAP strategy
│
├── bot.log                    # Generated during trading
├── README.md


---

# API Setup 

# 1. Generate API Keys  
Go to: https://demo.binance.com/en/my/settings/api-management

Enable:
- Reading 
- Spot & Margin Trading  
- Futures 

---

# 2. Set keys in terminal

```bash
export BINANCE_API_KEY="YOUR_API_KEY"
export BINANCE_API_SECRET="YOUR_API_SECRET"
```

Verify:

```bash
echo $BINANCE_API_KEY
echo $BINANCE_API_SECRET
```

---

# Installation

```bash
git clone https://github.com/Surabhi-Shekar/surabhi-binance-bot.git
cd surabhi-binance-bot
pip install -r requirements.txt
```

---

# Usage

## 1. Interactive UI Mode 

```bash
python src/main.py
```

Menu:

```
=== Binance Futures Trading Bot ===
1. Market Order
2. Limit Order
3. Stop-Limit Order
4. OCO Order
5. TWAP Strategy
0. Exit
```

---

## 2. Direct CLI Commands

### Market
```
python src/main.py market BTCUSDT BUY 0.001
```

### Limit
```
python src/main.py limit BTCUSDT SELL 0.002 50000
```

### Stop-Limit
```
python src/main.py stop_limit BTCUSDT BUY 0.001 45000 46000
```

### OCO
```
python src/main.py oco BTCUSDT SELL 0.001 52000 48000 47900
```

### TWAP
```
python src/main.py twap BTCUSDT BUY 0.01 5 3
```

---

# How It Works

### ✔ Custom REST Client
- Fully signs requests using timestamp + signature  
- Sends POST requests to Binance Demo Futures  
- Logs every request and response  

---

# Logging

All activity is logged to:

```
bot.log
```

---

