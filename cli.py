import argparse

from bot.validators import validate_order
from bot.orders import (
    place_market_order,
    place_limit_order
)

parser = argparse.ArgumentParser(
    description="Binance Futures Trading Bot"
)

parser.add_argument(
    "--symbol",
    required=True,
    help="Trading pair e.g. BTCUSDT"
)

parser.add_argument(
    "--side",
    required=True,
    help="BUY or SELL"
)

parser.add_argument(
    "--type",
    required=True,
    help="MARKET or LIMIT"
)

parser.add_argument(
    "--quantity",
    type=float,
    required=True,
    help="Order quantity"
)

parser.add_argument(
    "--price",
    type=float,
    help="Price required for LIMIT orders"
)

args = parser.parse_args()

try:

    validate_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\n==============================")
    print("ORDER REQUEST SUMMARY")
    print("==============================")

    print("Symbol   :", args.symbol)
    print("Side     :", args.side)
    print("Type     :", args.type)
    print("Quantity :", args.quantity)

    if args.price:
        print("Price    :", args.price)

    if args.type.upper() == "MARKET":

        order = place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    else:

        order = place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    print("\n==============================")
    print("SUCCESS")
    print("==============================")

    print("Order ID      :", order.get("orderId"))
    print("Status        :", order.get("status"))
    print("Executed Qty  :", order.get("executedQty"))

    if order.get("avgPrice"):
        print("Average Price :", order.get("avgPrice"))

except Exception as e:

    print("\n==============================")
    print("FAILED")
    print("==============================")

    print(str(e))