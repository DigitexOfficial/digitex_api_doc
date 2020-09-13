import asyncio
import websockets
import json
import random
import string
import sys


req_id = 0
# specify your own token
trader_token = "SET_YOUR_TOKEN_HERE"
trading_available = False
active_orders = {}
open_contracts = {}
active_cond_orders = {}


def round_price(price):
    tick_size = 5
    return round(price / tick_size) * tick_size


def generate_id():
    letters = string.ascii_letters + "0123456789"
    result = ''.join(random.choice(letters) for i in range(16))
    return result


def next_req_id():
    global req_id
    req_id += 1
    return req_id


async def send(ws, msg):
    print(f"sending: {msg}")
    await ws.send(msg)


async def send_request(ws, req):
    await send(ws, json.dumps(req))


def create_subscriptions_request(subscriptions):
    req_id = next_req_id()
    data = {"id": req_id, "method": "subscribe", "params": subscriptions}
    return data


async def handle_index_price(ws, msg):
    px = msg["data"]["markPx"]
    symbol = ""
    if msg["data"]["indexSymbol"] == ".DGTXBTCUSD":
        symbol = "BTCUSD-PERP"
    elif msg["data"]["indexSymbol"] == ".DGTXETHUSD":
        symbol = "ETHUSD-PERP"
    await handle_spot_price(ws, symbol, px)


async def handle_spot_price(ws, symbol, px):
    global active_orders
    global open_contracts
    global active_cond_orders

    # make actiions according to 'symbol': currently it can be either BTCUSD-PERP or ETHUSD-PERP

    # some random condition
    # value = random.randint(1, 300)
    # ---> Example of placing LIMIT order
    #if value == 151:
    #    side = random.choice(["BUY", "SELL"])
    #    limit_px = 0.0
    #    if side == "BUY":
    #        limit_px = px - 50
    #    else:
    #        limit_px = px + 50
    #    await place_limit_order(ws, symbol=symbol, side=side, price=round_price(limit_px), amount=10, tif="GTC")

    # some random condition
    # ---> Example of cancelling order
    #if value == 49:
    #    for cl_ord_id in active_orders:
    #        order_data = active_orders[cl_ord_id]
    #        symbol = order_data["symbol"]
    #        print(f"CANCEL order {cl_ord_id}")
    #        await cancel_order(ws, symbol, cl_ord_id)
    #        return

    # ---> Example of placing conditional order
    # some random condition
    #if value == 2:
    #    order_to_place = {"clOrdId": generate_id(),
    #                      "ordType": "LIMIT",
    #                      "timeInForce": "GTC",
    #                      "side": "SELL",
    #                      "px": 9300,
    #                      "qty": 45,
    #                      "mayIncrPosition": True,
    #    }
    #    action_id = generate_id()
    #    await place_conditional_order(ws, symbol, action_id, "SPOT_PRICE", "GREATER_EQUAL", 9300, order_to_place)

    # ---> Example of cancelling conditional order
    # some random condition
    #if value == 7:
    #    if len(active_cond_orders) > 0:
    #        # cancel a single conditional order
    #        for action_id in active_cond_orders:
    #            await cancel_conditional_order(ws, symbol, action_id, False)
    #            return
    #
    #        # cancel all conditional orders
    #        #await cancel_conditional_order(ws, symbol, None, True)

    # ---> Example of closing contract
    # some random condition
    #if value == 196:
    #    # close a particular contract
    #    for contract_id in open_contracts:
    #        await close_contract(ws, symbol, contract_id, "MARKET")
    #
    #    # close all open contracts
    #    await close_position(ws, symbol, "MARKET")


async def handle_orderbook(ws, msg):
    if len(msg["data"]["bids"]) == 0 and len(msg["data"]["asks"]) == 0:
        return

    bids = msg["data"]["bids"]
    asks = msg["data"]["asks"]
    best_bid = bids[0]
    best_bid_price = best_bid[0]
    #print(f"best bid px: {best_bid_price}")
    best_ask = asks[0]
    best_ask_price = best_ask[0]
    #print(f"best ask px: {best_ask_price}")


async def handle_trades(ws, msg):
    trades = msg["data"]["trades"]
    for t in trades:
        trade_price = t["px"]
        trade_amount = t["qty"]
        #print(f"got trade: px={trade_price}, qty={trade_amount}")


async def handle_kline(ws, msg):
    kline = msg["data"]
    i = kline["interval"]
    id = kline["id"]
    o, h, l, c, v = kline["o"], kline["h"], kline["l"], kline["c"], kline["v"]
    #print(f"got kline: interval={i}, id={id}, open_px={o}, high_px={h}, low_px={l}, close_px={c}, volume={v}")


async def handle_ticker(ws, msg):
    ticker = msg["data"]
    open_ts = ticker["openTime"]
    close_ts = ticker["closeTime"]
    high_px = ticker["highPx24h"]
    low_px = ticker["lowPx24h"]
    px_change = ticker["pxChange24h"]
    volume24h = ticker["volume24h"]
    funding_rate = ticker["fundingRate"]
    contract_value = ticker["contractValue"]
    dgtx_rate = ticker["dgtxUsdRate"]
    #print(f"got 24 stats: from={open_ts} to={close_ts} high_price={high_px} low_price={low_px} price_change={px_change} volume={volume24h} funding_rate={funding_rate} contract_value={contract_value} DGTX/USD={dgtx_rate}")


async def handle_exchange_message(ws, msg):
    channel = msg["ch"]

    try:
        if channel == "index":
            await handle_index_price(ws, msg)
        elif channel.startswith("orderbook"):
            await handle_orderbook(ws, msg)
        elif channel == "trades":
            await handle_trades(ws, msg)
        elif channel.startswith("kline"):
            await handle_kline(ws, msg)
        elif channel == "ticker":
            await handle_ticker(ws, msg)
        elif channel == "orderStatus":
            await handle_order_status(ws, msg)
        elif channel == "orderFilled":
            await handle_order_filled(ws, msg)
        elif channel == "orderCancelled":
            await handle_order_cancelled(ws, msg)
        elif channel == "traderStatus":
            await handle_trader_status(ws, msg)
        elif channel == "error":
            await handle_error(ws, msg)
        elif channel == "contractClosed":
            await handle_contract_closed(ws, msg)
        elif channel == "condOrderStatus":
            await handle_conditional_order_status(ws, msg)
        elif channel == "leverage":
            await handle_leverage(ws, msg)
        elif channel == "funding":
            await handle_funding(ws, msg)
        elif channel == "tradingStatus":
            await handle_trading_status(ws, msg)
        elif channel == "position":
            await handle_liquidated_position(ws, msg)
        else:
            print(f"unhandled message: {msg}")
    except Exception as e:
        print(f"WARNING! Exception: {e}", sys.exc_info()[0])


async def authenticate(ws, token):
    global auth_req_id

    if token is None:
        print("invalid token")
        return

    auth_req_id = next_req_id()
    req = {"id": auth_req_id, "method": "auth", "params": {"type": "token", "value": token}}
    print("authenticating with provided token")
    await send_request(ws, req)


async def get_trader_status(ws):
    req = {"id": next_req_id(), "method": "getTraderStatus", "params": {"symbol": "BTCUSD-PERP"}}
    print("requesting trader status")
    await send_request(ws, req)


async def handle_trader_status(ws, msg):
    global active_orders
    global open_contracts
    global active_cond_orders

    print(msg)

    data = msg["data"]

    trader_balance = data["traderBalance"]
    print(f"trader balance: {trader_balance}")

    if "positionType" in data:
        total_contracts = data["positionContracts"]
        pos_type = data["positionType"]
        print(f"trader position: {pos_type}@{total_contracts}")

    open_contracts = {}
    for c in data["contracts"]:
        contract_id = c["contractId"]
        open_contracts[contract_id] = c
    print("open contracts: ", open_contracts)

    active_orders = {}
    symbol = data["symbol"]
    for o in data["activeOrders"]:
        cl_ord_id = o["clOrdId"]
        ord_type = o["orderType"]
        ord_side = o["orderSide"]
        ord_tif = o["timeInForce"]
        px = o["px"] if "px" in o else 0.0
        qty = o["qty"]
        active_orders[cl_ord_id] = {"symbol": symbol,
                                    "orderType": ord_type,
                                    "side": ord_side,
                                    "tif": ord_tif,
                                    "px": px,
                                    "qty": qty
                                    }
    print("active_orders: ", active_orders)

    active_cond_orders = {}
    for co in data["conditionalOrders"]:
        action_id = co["actionId"]
        active_cond_orders[action_id] = co
    print("active conditional orders: ", active_cond_orders)


# usage:
#      place_market_order(ws, symbol=symbol, side="BUY", amount=100, tif="FOK")
async def place_market_order(ws, symbol, side, amount, tif):
    order_id = generate_id()
    params = {"symbol": symbol, "clOrdId": order_id, "ordType": "MARKET", "timeInForce": tif, "side": side, "qty": amount}
    req = {"id": next_req_id(), "method": "placeOrder", "params": params}
    print("placing MARKET order: ", params)
    await send_request(ws, req)


# usage:
#      place_limit_order(ws, symbol="BTCUSD-PERP", side="BUY", price=9250, amount=100, tif="GTC")
async def place_limit_order(ws, symbol, side, price, amount, tif):
    order_id = generate_id()
    params = {"symbol": symbol, "clOrdId": order_id, "ordType": "LIMIT", "timeInForce": tif, "side": side, "px": price, "qty": amount}
    req = {"id": next_req_id(), "method": "placeOrder", "params": params}
    print("placing LIMIT order: ", params)
    await send_request(ws, req)


# usage:
#      cancel_order(ws, symbol="BTCUSD-PERP", "sRJiP18rwdhukaxd")
async def cancel_order(ws, symbol, cl_ord_id):
    params = {"symbol": symbol, "clOrdId": cl_ord_id}
    req = {"id": next_req_id(), "method": "cancelOrder", "params": params}
    print(f"cancelling order: {cl_ord_id}")
    await send_request(ws, req)


# usage:
#      cancel_all_orders(ws, symbol="BTCUSD-PERP", side="SELL") - cancel all SELL orders
async def cancel_all_orders(ws, symbol, side=None, price=None):
    params = {"symbol": symbol}
    if side is not None:
        params["side"] = side
    if price is not None:
        params["px"] = round_price(price)
    req = {"id": next_req_id(), "method": "cancelAllOrders", "params": params}
    print("cancelling ALL orders")
    await send_request(ws, req)


# usage:
#      close_contract(ws, "BTCUSD-PERP", 619920760, "MARKET") - close contract 619920760 with market order
#      close_contract(ws, "BTCUSD-PERP", 619920760, "LIMIT", 9250, 50) - close only part of the contract 619920760 with limit order
async def close_contract(ws, symbol, contract_id, ord_type, price=None, qty=None):
    params = {"symbol": symbol, "contractId": contract_id, "ordType": ord_type}
    if ord_type == "LIMIT":
        if price is None:
            print("LIMIT order must specify a price")
            return
        params["px"] = round_price(price)
    if qty is not None:
        params["qty"] = qty
    req = {"id": next_req_id(), "method": "closeContract", "params": params}
    print(f"closing contract: {contract_id}")
    await send_request(ws, req)


# usage:
#      pass 'price' if the 'ord_type' is 'LIMIT'
async def close_position(ws, symbol, ord_type, price=None):
    if ord_type == "LIMIT" and price is None:
        print("price must be specified for LIMIT order")
        return

    params = {"symbol": symbol, "ordType": ord_type}
    if price is not None:
        params["px"] = price
    req = {"id": next_req_id(), "method": "closePosition", "params": params}
    print("closing position")
    await send_request(ws, req)


# parameters:
# - action_id - generated unique ID of the conditional action
# - trigger_price - currently only "SPOT_PRICE" supported
# - trigger_cond - "GREATER_EQUAL" or "LESS_EQUAL"
# - trigger_val - price value for the condition
# - order_data - conditional order parameters: type, side, TIF, ID, price, quantity:
# {"clOrdId":"010e2b91e5214410", "ordType":"LIMIT", "timeInForce":"GTC", "side":"BUY", "px":9105, "qty":100, "mayIncrPosition": true}
async def place_conditional_order(ws, symbol, action_id, trigger_price, trigger_cond, trigger_val, order_data):
    params = {"symbol": symbol, "actionId": action_id, "pxType": trigger_price, "condition": trigger_cond, "pxValue": round_price(trigger_val)}
    for key in order_data:
        params[key] = order_data[key]
    req = {"id": next_req_id(), "method": "placeCondOrder", "params": params}
    print("placing conditional order: ", params)
    await send_request(ws, req)


# usage:
#      cancel_conditional_order(ws, "BTCUSD-PERP", "a5b90ca768754b75", all=False)
async def cancel_conditional_order(ws, symbol, action_id=None, all=False):
    if action_id is None and all is False:
        print("attempt to cancel conditional order: either 'action_id' should be specified or 'all' set to True")
        return

    params = {"symbol": symbol}
    if action_id is not None:
        print(f"cancelling conditional order: {action_id}")
        params["actionId"] = action_id
    if all:
        print(f"cancelling ALL conditional orders")
        params["allForTrader"] = True
    req = {"id": next_req_id(), "method": "cancelCondOrder", "params": params}
    await send_request(ws, req)


async def change_leverage(ws, symbol, value):
    print(f"changing trader's leverage to {value}")
    params = {"symbol": symbol, "leverage": value}
    req = {"id": next_req_id(), "method": "changeLeverageAll", "params": params}
    await send_request(ws, req)


async def handle_order_status(ws, msg):
    global active_orders

    print(msg)

    data = msg["data"]
    cl_ord_id = data["clOrdId"]
    status = data["orderStatus"]

    if status == "ACCEPTED":
        symbol = data["symbol"]
        ord_type = data["orderType"]
        ord_side = data["orderSide"]
        ord_tif = data["timeInForce"]
        px = data["px"]
        qty = data["qty"]
        if ord_type == "LIMIT":
            print(f"order {cl_ord_id} has been ACCEPTED: {symbol} {ord_type} {ord_tif} {ord_side} {qty} @ {px}")
        else:
            print(f"order {cl_ord_id} has been ACCEPTED: {symbol} {ord_type} {ord_tif} {ord_side} {qty}")

        active_orders[cl_ord_id] = {"symbol": symbol,
                                    "orderType": ord_type,
                                    "side": ord_side,
                                    "tif": ord_tif,
                                    "px": px,
                                    "qty": qty
                                    }
    elif status == "REJECTED" and "errCode" in data:
        error_code = data["errCode"]
        print(f"order {cl_ord_id} has been REJECTED with error code: {error_code}")
    else:
        print(f"order {cl_ord_id} has been {status}")

    print(f"active orders: {active_orders}")


async def handle_order_filled(ws, msg):
    global active_orders
    global open_contracts

    print(msg)

    data = msg["data"]
    filled_ord_id = data["clOrdId"]
    order_status = data["orderStatus"]

    if order_status == "FILLED":
        print(f"order {filled_ord_id} has been FILLED")
    elif order_status == "PARTIALLY_FILLED":
        print(f"order {filled_ord_id} has been PARTIALLY FILLED")
        
        new_order_id = data["newClOrdId"]
        symbol = data["symbol"]
        ord_type = data["orderType"]
        ord_side = data["orderSide"]
        ord_tif = data["timeInForce"]
        px = data["px"]
        qty = data["qty"]
        
        print("add order {} to active orders".format(new_order_id))
        active_orders[new_order_id] = {"symbol": symbol,
                                       "orderType": ord_type,
                                       "side": ord_side,
                                       "tif": ord_tif,
                                       "px": px,
                                       "qty": qty
                                       }
    else:
        print(f"order {filled_ord_id} has status: {order_status}")

    if filled_ord_id in active_orders:
        active_orders.pop(filled_ord_id)
    print(f"active orders: {active_orders}")

    contracts = data["contracts"]
    for c in contracts:
        contract_id = c["contractId"]
        qty = c["qty"]
        if qty > 0:
            open_contracts[contract_id] = c
            pos_type = c["positionType"]
            entry_px = c["entryPx"]
            print(f"new contract {contract_id}: {pos_type} entry_px={entry_px} qty={qty}")
        elif qty == 0:
            closed_contract_id = c["oldContractId"]
            exit_px = c["exitPx"]
            print(f"contract {closed_contract_id} has been closed at {exit_px}")
            if closed_contract_id in open_contracts:
                open_contracts.pop(closed_contract_id)

    trader_balance = data["traderBalance"]
    print(f"trader balance: {trader_balance}")

    if "positionType" in data:
        pos_type = data["positionType"]
        total_contracts = data["positionContracts"]
        print(f"trader position: {pos_type}@{total_contracts}")


async def handle_order_cancelled(ws, msg):
    global active_orders

    print(msg)

    data = msg["data"]
    status = data["orderStatus"]

    if status == "REJECTED" and "errCode" in data:
        error_code = data["errCode"]
        print(f"order cancellation REJECTED with error code: {error_code}")
        return

    if "orders" not in data:
        return
    
    for order in data["orders"]:
        cancelled_order_id = order["oldClOrdId"]
        print(f"order {cancelled_order_id} has been CANCELLED")
        if cancelled_order_id in active_orders:
            active_orders.pop(cancelled_order_id)
        
    print(f"active orders: {active_orders}")


async def handle_contract_closed(ws, msg):
    print(msg)

    data = msg["data"]
    if "errCode" in data:
        error_code = data["errCode"]
        print(f"contract close operation FAILED with error code: {error_code}")


async def handle_conditional_order_status(ws, msg):
    global active_cond_orders

    print(msg)
    data = msg["data"]
    status = data["status"]

    if "errCode" in data:
        error_code = data["errCode"]
        print(f"conditional order placement/cancellation FAILED with error code: {error_code}")
        return

    if status == "ACCEPTED":
        for co in data["conditionalOrders"]:
            action_id = co["actionId"]
            active_cond_orders[action_id] = co
            print(f"conditional order {action_id}: {status}")
    elif status != "PENDING":
        for co in data["conditionalOrders"]:
            action_id = co["oldActionId"]
            if action_id in active_cond_orders:
                active_cond_orders.pop(action_id)
            print(f"conditional order {action_id}: {status}")

    print("active conditional orders: ", active_cond_orders)


async def handle_leverage(ws, msg):
    global active_orders
    global open_contracts

    print(msg)

    data = msg["data"]
    leverage = data["leverage"]
    print(f"trader leverage now is: {leverage}")

    if "errCode" in data:
        error_code = data["errCode"]
        print(f"leverage change FAILED with error code: {error_code}")
        return

    trader_balance = data["traderBalance"]
    print(f"trader balance: {trader_balance}")

    if "positionType" in data:
        total_contracts = data["positionContracts"]
        pos_type = data["positionType"]
        print(f"trader position: {pos_type}@{total_contracts}")

    open_contracts = {}
    for c in data["contracts"]:
        contract_id = c["contractId"]
        open_contracts[contract_id] = c
    print("open contracts: ", open_contracts)

    active_orders = {}
    symbol = data["symbol"]
    for o in data["activeOrders"]:
        cl_ord_id = o["clOrdId"]
        ord_type = o["orderType"]
        ord_side = o["orderSide"]
        ord_tif = o["timeInForce"]
        px = o["px"] if "px" in o else 0.0
        qty = o["qty"]
        active_orders[cl_ord_id] = {"symbol": symbol,
                                    "orderType": ord_type,
                                    "side": ord_side,
                                    "tif": ord_tif,
                                    "px": px,
                                    "qty": qty
                                    }
    print("active_orders: ", active_orders)


async def handle_funding(ws, msg):
    global open_contracts

    print(msg)
    data = msg["data"]

    trader_balance = data["traderBalance"]
    payout = data["payout"]
    pos_margin_change = data["positionMarginChange"]
    print(f"trader balance = {trader_balance}, payout = {payout}, position margin change = {pos_margin_change}")

    open_contracts = {}
    for c in data["contracts"]:
        contract_id = c["contractId"]
        open_contracts[contract_id] = c
    print("open contracts: ", open_contracts)


async def handle_trading_status(ws, msg):
    global trading_available

    print(msg)
    data = msg["data"]
    if data["available"] is True:
        # trading is available
        # trade requests can be sent
        trading_available = True
        print("trading: AVAILABLE")
        await get_trader_status(ws)
    else:
        trading_available = False
        print("trading: NOT AVAILABLE")


async def handle_error(ws, msg):
    print(msg)


async def handle_liquidated_position(ws, msg):
    global active_orders
    global open_contracts

    print(msg)
    data = msg["data"]

    for cl_ord_id in data["terminatedOrders"]:
        if cl_ord_id in active_orders:
            active_orders.pop(cl_ord_id)

    print("active_orders: ", active_orders)

    if "traderBalanceIncrement" in data:
        balance_delta = data["traderBalanceIncrement"]
        print(f"trader balance increment/decrement: {balance_delta}")

    trader_balance = data["traderBalance"]
    print(f"trader balance: {trader_balance}")

    if "positionType" in data:
        total_contracts = data["positionContracts"]
        pos_type = data["positionType"]
        print(f"trader position: {pos_type}@{total_contracts}")

    for contract in data["liquidatedContracts"]:
        id = contract["oldContractId"]
        if id in open_contracts:
            open_contracts.pop(id)

    print("open contracts: ", open_contracts)


async def run():
    global trader_token
    global auth_req_id

    random.seed()

    # use wss://ws.mapi.digitexfutures.com for mainnet environment
    uri = "wss://ws.tapi.digitexfutures.com"
    async with websockets.connect(uri, ssl=True) as ws:
        req = create_subscriptions_request(["BTCUSD-PERP@index", "BTCUSD-PERP@orderbook_5", "BTCUSD-PERP@ticker", "BTCUSD-PERP@trades", "BTCUSD-PERP@liquidations"])
        await send_request(ws, req)
        await authenticate(ws, trader_token)

        while True:
            msg = await ws.recv()

            if msg == "ping":
                print("received: ping")
                await send(ws, "pong")
            else:
                response = json.loads(msg)
                if "ch" in response:
                    await handle_exchange_message(ws, response)
                else:
                    print(f"received: {response}")


asyncio.get_event_loop().run_until_complete(run())
