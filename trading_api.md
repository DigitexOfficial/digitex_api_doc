# TRADING API DRAFT

*<u>Note:</u> for each private request authentication is required.*

#### General

Every response has the following structure in case of success. Field `data` could be either an object or an array.

```json
{
  "status": "ok",
  "data": {}
}
```

And in case of error response would be like:

```json
{
  "status": "error",
  "code": 2222,
  "msg": "error description"
}
```

<u>Note</u>: the error will also be returned in case of system maintenance and absence of data for the response. 

Value for the `clOrdId` is assigned by the trader. It should be unique string for each order.

Possible value of order's `status`: `UNDEFINED`, `PENDING`, `ACCEPTED`, `REJECTED`, `CANCELED`, `FILLED`, `PARTIAL`, `TERMINATED`, `EXPIRED`, `TRIGGERED`.

Possible values of `ordType`: `MARKET`, `LIMIT`, `STOP`, `TAKE_PROFIT`.

Possible values of `timeInForce`: `GTD`, `GTC`, `GTF`, `IOC`, `FOK`.

Possible values of `side`: `BUY`, `SELL`.

Value of `stopPx` is associated with a stop or take profit order. Required if `ordType` is `STOP` or `TAKE_PROFIT`. 

For `STOP` order `px` denotes the worst price at which the `STOP` or `TAKE_PROFIT` order can get filled at. If no `px` is provided the `STOP` or `TAKE_PROFIT` order will trigger a `MARKET` order. 

For `BTCUSD-PERP`: `px` should be positive and <u>multiple of 5</u>, `qty` positive and <u>integral</u>.

All timestamps are provided in milliseconds.

------

## HTTP REST API

#### Place order

**Request**

`POST /api/v1/private/order/place`

```json
{
    "symbol": "BTCUSD-PERP",
    "clOrdId": "q1w2e3r2",
    "ordType": "LIMIT",
    "timeInForce": "GTC",
    "side": "SELL",
    "px": 9200,
    "qty": 10
}
```

**Response**

```json
{
    "status": "ok",
    "data": {
        "symbol": "BTCUSD-PERP",
        "clOrdId": "123456",
        "status": "PENDING",
        "createdAt": 1592381206000,
        "updatedAt": 1592381206000,
        "ordType": "LIMIT",
        "timeInForce": "GTC",
        "side": "BUY",
        "px": 9200,
        "avgPx": 0,
        "qty": 100,
        "filledQty": 0,
        "unfilledQty": 100
    }
}
```

`createdAt` and `updatedAt` are timestamps in milliseconds.

------

#### Get order status

**Request**

`GET /api/v1/private/order/status`

| Parameter name | Parameter type | Description                    |
| -------------- | -------------- | ------------------------------ |
| clOrdId        | string         | identifier of the placed order |

**Response**

```json
{
    "status": "ok",
    "data": {
        "symbol": "BTCUSD-PERP",
        "clOrdId": "123456",
        "status": "FILLED",
        "createdAt": 1592381206000,
        "updatedAt": 1592381785000,
        "ordType": "LIMIT",
        "timeInForce": "GTC",
        "side": "BUY",
        "px": 9200,
        "avgPx": 9200,
        "qty": 100,
        "filledQty": 100,
        "unfilledQty": 0
    }
}
```

`createdAt` and `updatedAt` are timestamps in milliseconds.

------

#### Get active orders

**Request**

`GET /api/v1/private/order/active`

| Parameter name | Parameter type | Description                    |
| -------------- | -------------- | ------------------------------ |
| symbol         | string         | e.g. 'BTCUSD-PERP'; *optional* |

**Response**

```json
{
    "status": "ok",
    "data": [
        {
            "symbol": "BTCUSD-PERP",
            "clOrdId": "45622358",
            "status": "ACCEPTED",
            "createdAt": 1592382086000,
            "updatedAt": 1592382086000,
            "ordType": "LIMIT",
            "timeInForce": "GTC",
            "side": "BUY",
            "px": 9200,
            "avgPx": 0,
            "qty": 100,
            "filledQty": 0,
            "unfilledQty": 100
        },
        {
            "symbol": "BTCUSD-PERP",
            "clOrdId": "1256987",
            "status": "ACCEPTED",
            "createdAt": 1592382180000,
            "updatedAt": 1592382180000,
            "ordType": "LIMIT",
            "timeInForce": "GTC",
            "side": "SELL",
            "px": 9400,
            "avgPx": 0,
            "qty": 100,
            "filledQty": 0,
            "unfilledQty": 100
        }
    ]
}
```

`createdAt` and `updatedAt` are timestamps in milliseconds.

------

#### Update order

**Request**

`POST /api/v1/private/order/update`

```json
{
    "symbol": "BTCUSD-PERP",
    "oldClOrdId": "q1w2e3r2",
    "clOrdId": "vbn12358",
    "ordType": "LIMIT",
    "timeInForce": "GTC",
    "side": "SELL",
    "px": 9300,
    "qty": 20
}
```

`oldClOrdId` is the identifier of the order you want to update.

**Response**

General response with `ok` or `error`.

------

#### Cancel order

You can cancel the order by using a Client Order ID (`clOrdId`) of a placed order.

**Request**

`POST /api/v1/private/order/cancel`

```json
{
    "clOrdId": "p2w5r3t8"
}
```

**Response**

General response with `ok` or `error`.

------

#### Cancel multiple orders

Trader can cancel all the orders (`side` and `px` are omitted) or just orders with the specified `side`  and/or `px`.

**Request**

`POST /api/v1/private/order/cancel_all`

```json
{
    "side": "SELL"
}
```

**Response**

General response with `ok` or `error`.

------

#### Get positions

Possible values of position `type`: `LONG`, `SHORT`.

**Request**

`GET /api/v1/private/position`

**Response**

```json
{
    "status": "ok",
    "data": [
        {
            "id": 1254789,
            "symbol": "BTCUSD-PERP",
            "type": "LONG",
            "openTime": 124578957000,
            "entryPx": 9550,
            "qty": 50,
            "margin": 9550,
            "liquidationPx": 14180,
            "leverage": 1,
            "pnl": 50,
            "upnl": 10,
            "liquidationVolume": 0,
            "bankruptcyVolume": 0,
            "lastTradePx": 9800,
            "lastTradeQty": 50,
            "markPx": 9950,
        }
    ]
}
```

`openTime` is timestamp in milliseconds.

------

#### Close position

Trader can specify `ordType` (`MARKET` or `LIMIT`), `px` (only for `LIMIT`) and `qty` (to close only a part of the position).

**Request**

`POST /api/v1/private/position/close`

```json
{
    "positionId": 451236,
    "ordType": "LIMIT",
    "px": 9300
}
```

**Response**

General response with `ok` or `error`.

------

#### Close all positions

Trader can specify `ordType` (`MARKET` or `LIMIT`) and `px` (if `ordType` is set to `LIMIT`).

**Request**

`POST /api/v1/private/position/close_all`

```json
{
    "ordType": "LIMIT",
    "px": 9500
}
```

**Response**

General response with `ok` or `error`.

------

#### Get wallet balance

There are several kinds of wallets: `MAIN`, `TRADING`.

**Request**

`GET /api/v1/private/wallet/balance`

**Response**

```json
{
    "status": "ok",
    "data": [
        {
            "walletType": "MAIN",
            "currency": "DGTX",
            "balance": 100000,
        },
        {
            "walletType": "TRADING",
            "currency": "DGTX",
            "balance": 5000,
            "orderMargin": 2000,
            "positionMargin": 2000
        }
    ]
}
```

------

#### Transfer

You can transfer certain `amount` of `currency` (`DGTX`) between `fromWallet` and `toWallet`.

**Request**

`POST /api/v1/private/wallet/transfer`

```json
{
    "fromWallet": "MAIN",
    "toWallet": "TRADING",
    "amount": 1000,
    "currency": "DGTX"
}
```

**Response**

```json
{
    "status": "ok",
    "data": {
        "id": 125468,
        "createdAt": 1592484229000,
        "updatedAt": 1592484229000,
        "status": "CREATED",
        "fromWallet": "TRADING",
        "toWallet": "MAIN",
        "amount": 10000,
        "currency": "DGTX"
    }
}
```

Possible values of transfer `status`: `CREATED`, `PENDING`, `ACCEPTED`, `REJECTED`.

`createdAt` and `updatedAt` are timestamps in milliseconds.

------

#### Withdrawals

You can request withdrawal from `wallet` using `method` and specify an `amount` witch will be sent to `address`. The request will be processed with `priority`. `message` is optional text.

Possible values of `method`: `ETH`, `BTC`, `XRP`, `DGTX`.

Possible values of `priority`: `LOW`, `MID`, `HIGH`. Default: `MID`.

**Request**

`POST /api/v1/private/wallet/withdraw`

```json
{
    "wallet": "MAIN",
    "method": "ETH",
    "amount": 5,
    "address": "0x25b78frd4...8n",
    "priority": "HIGH",
    "message": "from DIGITEX with love"
}
```

**Response**

```json
{
    "status": "ok",
    "data": {
        "withdrawalId": 123456,
        "wallet": "MAIN",
        "createdAt": 1592397360000,
        "updatedAt": 1592397360000,
        "method": "ETH",
        "address": "0x25b78frd4...8n",
        "priority": "HIGH",
        "fee": 0.05,
        "status": "PENDING",
        "message": "from DIGITEX with love"
    }
}
```

Possible withdrawal `status`:  `CREATED`, `PENDING`, `ACCEPTED`, `REJECTED`, `DECLINED`, `CANCELED`.

`createdAt` and `updatedAt` are timestamps in milliseconds.

------

#### Trade history

**Request**

`GET /api/v1/private/trades/history`

| Parameter name | Parameter type | Description               |
| -------------- | -------------- | ------------------------- |
| symbol         | string         | e.g. 'BTCUSD-PERP'        |
| from           | int64          | Timestamp in milliseconds |
| to             | int64          | Timestamp in milliseconds |
| limit          | int64          | Default: 10. Max: 100     |

**Response**

```json
{
    "status": "ok",
    "data": [
        {
            "id": 1234567,
            "ts": 1592906400000,
            "symbol": "BTCUSD-PERP",
            "px": 9600,
            "qty": 100,
        }
    ]
}
```

`ts` is a timestamp in milliseconds.

------

#### Fill history

**Request**

`GET /api/v1/private/fills/history`

| Parameter name | Parameter type | Description               |
| -------------- | -------------- | ------------------------- |
| symbol         | string         | e.g. 'BTCUSD-PERP'        |
| from           | int64          | Timestamp in milliseconds |
| to             | int64          | Timestamp in milliseconds |
| limit          | int64          | Default: 10. Max: 100     |

**Response**

```json
{
    "status": "ok",
    "data": [
        {
            "symbol": "BTCUSD-PERP",
            "ts": 123456789000,
            "clOrdId": "qwerty",
            "side": "BUY/SELL",
            "ordPx": 9500,
            "fillId": "12345",
            "fillPx": 9500,
            "fillQty": 100
        }
    ]
}
```

`ts`  is a timestamp in milliseconds.

------

## WEBSOCKET API

### REQUESTS

------

#### Place order

```json
{
    "id": 2,
    "method": "placeOrder",
    "params": {
        "symbol": "BTCUSD-PERP",
        "clOrdId": "q1w2e3r2",
        "ordType": "LIMIT",
        "timeInForce": "GTC",
        "side": "SELL",
        "px": 9200,
        "qty": 10
    }
}
```

**Response message**

```json
{
    "id": 2,
    "status": "ok"
}
```

Messages about changes to order's status will be sent during order processing. 

------

#### Get active orders

Field `symbol` is optional.

```json
{
    "id": 4,
    "method": "activeOrders",
    "params": {
        "symbol": "BTCUSD-PERP"
    }
}
```

**Response message**

```json
{
    "id": 4,
    "status": "ok",
    "result": [
        {
            "symbol": "BTCUSD-PERP",
            "clOrdId": "45622358",
            "status": "ACCEPTED",
            "createdAt": 1592382086000,
            "updatedAt": 1592382086000,
            "ordType": "LIMIT",
            "timeInForce": "GTC",
            "side": "BUY",
            "px": 9200,
            "avgPx": 0,
            "qty": 100,
            "filledQty": 0,
            "unfilledQty": 100
        },
        {
            "symbol": "BTCUSD-PERP",
            "clOrdId": "1256987",
            "status": "ACCEPTED",
            "createdAt": 1592382180000,
            "updatedAt": 1592382180000,
            "ordType": "LIMIT",
            "timeInForce": "GTC",
            "side": "SELL",
            "px": 9400,
            "avgPx": 0,
            "qty": 100,
            "filledQty": 0,
            "unfilledQty": 100
        }
    ]
}
```

`createdAt` and `updatedAt` are timestamps in milliseconds.

------

#### Update order

```json
{
    "id": 5,
    "method": "updateOrder",
    "params": {
        "symbol": "BTCUSD-PERP",
        "oldClOrdId": "q1w2e3r2",
        "clOrdId": "vbn12358",
        "ordType": "LIMIT",
        "timeInForce": "GTC",
        "side": "SELL",
        "px": 9300,
        "qty": 20
    }
}
```

`oldClOrdId` is the identifier of the order you want to update.

**Response message**

```json
{
    "id": 5,
    "status": "ok"
}
```

------

#### Cancel order

You can cancel the order by using a Client Order ID (`clOrdId`) of a placed order.

```json
{
    "id": 6,
    "method": "cancelOrder",
    "params": {
        "symbol": "BTCUSD-PERP",
        "clOrdId": "p2w5r3t8"
    }
}
```

**Response message**

```json
{
    "id": 6,
    "status": "ok"
}
```

------

#### Cancel multiple orders

Trader can cancel all the orders (`side` and `px` are omitted) or just orders with the specified `side`  and/or `px`.

```json
{
    "id": 7,
    "method": "cancelAllOrders",
    "params": {
        "symbol": "BTCUSD-PERP",
        "side": "SELL"
    }
}
```

**Response message**

```json
{
    "id": 7,
    "status": "ok"
}
```

------

#### Get positions

Possible values of position `type`: `LONG`, `SHORT`.

```json
{
    "id": 8,
    "method": "listOpenPositions",
    "params": {}
}
```

**Response message**

```json
{
    "status": "ok",
    "data": [
        {
            "id": 1254789,
            "symbol": "BTCUSD-PERP",
            "type": "LONG",
            "openTime": 124578957000,
            "entryPx": 9550,
            "qty": 50,
            "margin": 9550,
            "liquidationPx": 14180,
            "leverage": 1,
            "pnl": 50,
            "upnl": 10,
            "liquidationVolume": 0,
            "bankruptcyVolume": 0,
            "lastTradePx": 9800,
            "lastTradeQty": 50,
            "markPx": 9950,
        }
    ]
}
```

`openTime` is a timestamp in milliseconds.

------

#### Close position

Trader can specify `ordType` (`MARKET` or `LIMIT`), `px` (only for `LIMIT`) and `qty` (to close only a part of the position).

```json
{
    "id": 9,
    "method": "closePosition",
    "params": {
        "symbol": "BTCUSD-PERP",
        "positionId": 451236,
        "ordType": "LIMIT",
        "px": 9300
    }
}
```

**Response message**

```json
{
    "id": 10,
    "status": "ok"
}
```

------

#### Close all positions

Trader can specify `ordType` (`MARKET` or `LIMIT`) and `px` (if `ordType` is set to `LIMIT`).

```json
{
    "id": 10,
    "method": "closeAllPositions",
    "params": {
        "symbol": "BTCUSD-PERP",
        "ordType": "LIMIT",
        "px": 9500
    }
}
```

**Response message**

```json
{
    "id": 10,
    "status": "ok"
}
```

------

#### Get wallet balance

There are several kinds of wallets: `MAIN`, `TRADING`.

```json
{
    "id": 11,
    "method": "walletBalance",
    "params": {}
}
```

**Response message**

```json
{
    "id": 11,
    "status": "ok",
    "result": [
        {
            "walletType": "MAIN",
            "currency": "DGTX",
            "balance": 100000,
        },
        {
            "walletType": "TRADING",
            "currency": "DGTX",
            "balance": 5000,
            "orderMargin": 2000,
            "positionMargin": 2000
        }
    ]
}
```

------

#### Transfer

You can transfer certain `amount` of `currency` (`DGTX`) between `fromWallet` and `toWallet`.

```json
{
    "id": 12,
    "method": "transfer",
    "params": {
        "fromWallet": "MAIN",
        "toWallet": "TRADING",
        "amount": 1000,
        "currency": "DGTX"
    }
}
```

**Response message**

```json
{
    "id": 12,
    "status": "ok",
    "result": {
        "id": 125468,
        "createdAt": 1592484229000,
        "updatedAt": 1592484229000,
        "fromWallet": "MAIN",
        "toWallet": "TRADING",
        "amount": 1000,
        "currency": "DGTX",
        "status": "CREATED"
    }
}
```

Possible values of transfer `status`: `CREATED`, `PENDING`, `ACCEPTED`, `REJECTED`.

`createdAt` and `updatedAt` are timestamps in milliseconds.

------

#### Withdrawals

You can request withdrawal from `wallet` using `method` and specify an `amount` witch will be sent to `address`. The request will be processed with `priority`. `message` is optional.

Possible values of `method`: `ETH`, `BTC`, `XRP`, `DGTX`.

Possible values of `priority`: `LOW`, `MID`, `HIGH`. Default: `MID`.

```json
{
    "id": 13,
    "method": "makeWithdrawal",
    "params": {
        "wallet": "MAIN",
        "method": "ETH",
        "amount": 5,
        "address": "0x25b78frd4...8n",
        "priority": "HIGH",
        "message": "from DIGITEX with love"
    }
}
```

**Response message**

```json
{
    "id": 13,
    "status": "ok",
    "result": {
        "withdrawalId": 123456,
        "wallet": "MAIN",
        "createdAt": 1592397360000,
        "updatedAt": 1592397360000,
        "method": "ETH",
        "address": "0x25b78frd4...8n",
        "priority": "HIGH",
        "fee": 0.05,
        "status": "PENDING",
        "message": "from DIGITEX with love"
    }
}
```

Possible withdrawal `status`:  `CREATED`, `PENDING`, `ACCEPTED`, `REJECTED`, `DECLINED`, `CANCELED`.

`createdAt` and `updatedAt` are timestamps in milliseconds.

------

#### Trade history

Trade history of `symbol` from point `from` to point `to`, no more than `limit` trades.

Maximum value of `limit`: 100.

```json
{
    "id": 14,
    "method": "tradeHistory",
    "params": {
        "symbol": "BTCUSD-PERP",
        "from": 1592906400000,
        "to": 1592917200000,
        "limit": 100
    }
}
```

**Response message**

```json
{
    "id": 14,
    "status": "ok",
    "result": [
        {
            "id": 1234567,
            "ts": 1592906400000,
            "symbol": "BTCUSD-PERP",
            "px": 9600,
            "qty": 100,
        },
        {
            "id": 1234568,
            "ts": 1592906405000,
            "symbol": "BTCUSD-PERP",
            "px": 9605,
            "qty": 25,
        }
    ]
}
```

`ts` is a timestamp in milliseconds.

------

#### Fill history

```json
{
    "id": 15,
    "method": "makeWithdrawal",
    "params": {
        "symbol": "BTCUSD-PERP",
        "from": 1592906400000,
        "to": 1592917200000,
        "limit": 100
    }
}
```

**Response message**

```json
{
    "id": 15,
    "status": "ok",
    "result": [
        {
            "symbol": "BTCUSD-PERP",
            "ts": 123456789000,
            "fillId": "12345",
            "clOrdId": "qwerty",
            "side": "BUY",
            "ordPx": 9500,
            "fillPx": 9500,
            "fillQty": 100
        }
    ]
}
```

`ts` is a timestamp in milliseconds.

------

### SUBSCRIPTIONS

------

#### List of public channels

- pnl (PnL/UPnL values)
- tradingbalance (changes to trader's balance)
- deposits (deposit events)
- withdrawals (withdrawal events)
- positions (trader's position changes)
- transfers (transfer between wallets)
- fills

------

#### Pnl/UPnL channel

**Channel name:** `private@pnl`.

Published message:

```json
{
    "ch": "pnl",
    "data": [
        {
            "symbol":"BTCUSD-PERP",
            "ts": 1591295037813,
            "pnl": 50,
            "upnl": 3
        }
    ]
}
```

------

#### Trading balance channel

**Channel name:** `private@tradingbalance`.

Published message:

```json
{
    "ch": "tradingbalance",
    "data": {
        "currency": "DGTX",
        "balance": 10000,
        "availableBalance": 5000
    }
}
```

------

#### Deposits channel

**Channel name:** `private@deposits`.

Published message:

```json
{
    "ch": "deposits",
    "data": {
        "ts": 1592939551000,
        "wallet": "MAIN",
        "amount": 5000,
        "currency": "DGTX"
    }
}
```

------

#### Withdrawals channel

**Channel name:** `private@withdrawals`.

Published message:

```json
{
    "ch": "withdrawals",
    "data": {
        "withdrawalId": 123456,
        "wallet": "MAIN",
        "createdAt": 1592397360000,
        "updatedAt": 1592940633000,
        "method": "ETH",
        "address": "0x25b78frd4...8n",
        "priority": "HIGH",
        "fee": 0.05,
        "status": "ACCEPTED",
        "message": "from DIGITEX with love"
    }
}
```

------

#### Positions channel

**Channel name:** `private@positions`.

Published message:

```json
{
    "ch": "positions",
    "data": [
        {
            "id": 1254789,
            "symbol": "BTCUSD-PERP",
            "type": "LONG",
            "openTime": 124578957000,
            "entryPx": 9550,
            "qty": 50,
            "margin": 9550,
            "liquidationPx": 14180,
            "leverage": 1,
            "pnl": 50,
            "upnl": 10,
            "liquidationVolume": 0,
            "bankruptcyVolume": 0,
            "lastTradePx": 9800,
            "lastTradeQty": 50,
            "markPx": 9950,
        }    
    ]
}
```

------

#### Transfers channel

**Channel name:** `private@transfers`.

Published message:

```json
{
    "ch": "transfers",
    "data": {
        "id": 125468,
        "createdAt": 1592484229000,
        "updatedAt": 1592941512000,
        "fromWallet": "MAIN",
        "toWallet": "TRADING",
        "amount": 1000,
        "currency": "DGTX",
        "status": "ACCEPTED"
    }
}
```

------

#### Fills channel

**Channel name:** `private@fills`.

Published message:

```json
{
    "ch": "fills",
    "data": {
        "symbol": "BTCUSD-PERP",
        "ts": 1592941576000,
        "fillId": "12345",
        "clOrdId": "qwerty",
        "side": "BUY",
        "ordPx": 9500,
        "fillPx": 9500,
        "fillQty": 100
    }
}
```

------

