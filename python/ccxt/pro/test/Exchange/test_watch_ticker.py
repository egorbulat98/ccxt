import os
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root)

# ----------------------------------------------------------------------------

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from ccxt.test.exchange.base import test_ticker  # noqa E402
from ccxt.test.exchange.base import test_shared_methods  # noqa E402

async def test_watch_ticker(exchange, skipped_properties, symbol):
    method = 'watchTicker'
    now = exchange.milliseconds()
    ends = now + 15000
    while now < ends:
        response = None
        try:
            response = await exchange.watch_ticker(symbol)
        except Exception as e:
            if not test_shared_methods.is_temporary_failure(e):
                raise e
            now = exchange.milliseconds()
            continue
        assert isinstance(response, dict), exchange.id + ' ' + method + ' ' + symbol + ' must return an object. ' + exchange.json(response)
        now = exchange.milliseconds()
        test_ticker(exchange, skipped_properties, method, response, symbol)
