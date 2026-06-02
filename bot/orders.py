from binance.enums import *
from bot.client import client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    try:
        logger.info(
            f"REQUEST -> MARKET | Symbol={symbol} | Side={side} | Qty={quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(f"RESPONSE -> {order}")

        return order

    except Exception as e:
        logger.error(f"MARKET ORDER ERROR -> {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"REQUEST -> LIMIT | Symbol={symbol} | Side={side} | Qty={quantity} | Price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"RESPONSE -> {order}")

        return order

    except Exception as e:
        logger.error(f"LIMIT ORDER ERROR -> {e}")
        raise