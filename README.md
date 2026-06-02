Binance Futures Trading Bot

Overview

A Python-based Command Line Interface (CLI) Trading Bot for Binance Futures Testnet (USDT-M).

This application allows users to place MARKET and LIMIT orders on Binance Futures Testnet using Binance API credentials. The bot supports both BUY and SELL orders with input validation, logging, and exception handling.

---

Features

- Place MARKET Orders
- Place LIMIT Orders
- Supports BUY and SELL
- Command Line Interface (CLI)
- Input Validation
- Logging of API Requests and Responses
- Error Handling
- Binance Futures Testnet Integration
- Modular and Reusable Code Structure

---

```Project Structure

binance-futures-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env

---
```
Requirements

- Python 3.x
- Binance Futures Testnet Account
- Binance API Key
- Binance Secret Key

---

Installation

1. Clone the Repository

git clone <repository-url>
cd binance-futures-trading-bot

2. Install Dependencies

pip install -r requirements.txt

3. Create .env File

Create a ".env" file in the project root directory:

API_KEY=your_api_key
API_SECRET=your_api_secret

---

Running the Application

MARKET BUY Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT SELL Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 110000

---

```Sample Output

==============================
ORDER REQUEST SUMMARY
==============================
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

==============================
SUCCESS
==============================
Order ID      : 13814980918
Status        : NEW
Executed Qty  : 0.0000
Average Price : 0.00

---
```
Logging

All API requests, responses, and errors are stored in:

logs/trading.log

Example:

REQUEST -> MARKET | Symbol=BTCUSDT | Side=BUY | Qty=0.001

RESPONSE -> {...}

REQUEST -> LIMIT | Symbol=BTCUSDT | Side=SELL | Qty=0.001 | Price=110000

RESPONSE -> {...}

---

Error Handling

The application handles:

- Invalid order side
- Invalid order type
- Missing price for LIMIT orders
- Invalid quantity values
- Binance API errors
- Network-related exceptions

---

Assumptions

- Binance Futures Testnet is used.
- Only USDT-M Futures are supported.
- LIMIT orders require a price value.
- API credentials are stored in a ".env" file.
- Unfilled orders may return:

Status = NEW
Executed Qty = 0.0000
Average Price = 0.00

This means the order has been accepted by Binance but has not yet been executed or filled. This behavior is common for pending LIMIT orders and may also occur in the Testnet environment.

---

Screenshots

The repository includes screenshots for:

1. MARKET BUY Order
![alt text](<Screenshot 2026-06-02 182332-2.png>)

2. LIMIT SELL Order
![alt text](<Screenshot 2026-06-02 182404.png>)

3. trading.log Output
![alt text](<Screenshot 2026-06-02 182643.png>)

---

Author

Nitish Kumar 
