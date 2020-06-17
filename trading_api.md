# Trading API Draft

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

Possible value of order's `status`: `UNDEFINED`, `PENDING`, `ACCEPTED`, `REJECTED`, `CANCELED`, `FILLED`, `PARTIAL`, `TERMINATED`, `EXPIRED`, `TRIGGERED`.

------

#### Place order

**Request**

`POST /api/v1/private/order/place`

| Parameter name | Parameter type | Description                       |
| -------------- | -------------- | --------------------------------- |
| symbol         | string         | e.g. 'BTCUSD-PERP'                |
| clOrdId        | string         | assigned by the trader            |
| ordType        | string         | `MARKET`/`LIMIT`                  |
| timeInForce    | string         | `GTD`, `GTC`, `GTF`, `IOC`, `FOK` |
| side           | string         | `BUY`/`SELL`                      |
| px             | float          | not required if type is `MARKET`  |
| qty            | float          |                                   |

For `BTCUSD-PERP`: `px` should be positive and <u>multiple of 5</u>, `qty` positive and <u>integral</u>.

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

------

#### Get order status

**Request**

`GET /api/v1/private/order`

| Parameter name | Parameter type | Description            |
| -------------- | -------------- | ---------------------- |
| ordId          | string         | assigned by the API    |
| clOrdId        | string         | provided by the trader |

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



------

#### Get active orders

**Request**

`GET /api/v1/private/orders/active`

| Parameter name | Parameter type | Description                  |
| -------------- | -------------- | ---------------------------- |
| symbol         | string         | e.g. 'BTCUSD-PERP'; optional |

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

------

#### Update order

**Request**

`POST /api/v1/private/order/update`

| Parameter name | Parameter type | Description                             |
| -------------- | -------------- | --------------------------------------- |
| symbol         | string         | e.g. 'BTCUSD-PERP'                      |
| oldClOrdId     | string         | `clOrdId` of the original order         |
| clOrdId        | string         | assigned by the trader (new order's ID) |
| ordType        | string         | `MARKET`/`LIMIT`                        |
| timeInForce    | string         | `GTD`, `GTC`, `GTF`,` IOC`, `FOK`       |
| side           | string         | `BUY`/`SELL`                            |
| px             | float          | not required if type is `MARKET`        |
| qty            | float          |                                         |

For `BTCUSD-PERP`: `px` should be positive and <u>multiple of 5</u>, `qty` positive and <u>integral</u>.

**Response**

General response with `ok` or `error`.

------

#### Cancel order

You can cancel the order by using a Client Order ID (`clOrdId`) of a placed order.

**Request**

`POST /api/v1/private/order/cancel`

| Parameter name | Parameter type | Description            |
| -------------- | -------------- | ---------------------- |
| clOrdId        | string         | provided by the trader |

**Response**

General response with `ok` or `error`.

------

#### Cancel orders

Trader can cancel all the orders (`side` and `px` are omitted) or just orders with the specified `side`  and/or `px`.

**Request**

`POST /api/v1/private/orders/cancel`

| Parameter name | Parameter type | Description            |
| -------------- | -------------- | ---------------------- |
| side           | string         | `BUY`/`SELL`; optional |
| px             | float          |                        |

**Response**

General response with `ok` or `error`.

------

#### Get positions

**Request**

`GET /api/v1/private/positions`

**Response**

```json
{
    "status": "ok",
    "data": [
        {
            "id": 1254789,
            "symbol": "BTCUSD-PERP",
            "type": "long/short",
            "openTime": 124578957000,
            "entryPx": 9550,
            "qty": 500,
            "volume": 10000,
            "pnl": 50,
            "upnl": 10,
            "liquidationVolume": 5000,
            "bankruptcyVolume": 5000,
            "lastTradePx": 9800,
            "lastTradeQty": 50,
            "buy_order_margin": 10,
            "buy_order_quantity": 1,
            "sell_order_margin": 10,
            "sell_order_quantity": 2,
            "mark_price": 9950,
        }
    ]
}
```

------

#### Close contract

You can close single or all contracts (if `contractId` is omitted).

**Request**

`POST /api/v1/private/contract/close`

| Parameter name | Parameter type | Description                         |
| -------------- | -------------- | ----------------------------------- |
| contractId     | uint64         | *optional*                          |
| ordType        | string         | `MARKET`/`LIMIT`                    |
| px             | float          | `px` is the price for `LIMIT` order |
| qty            | float          | `0` or omit to fully close          |

**Response**

General response with `ok` or `error`.

------

#### Get trader balance

There are several kinds of wallets: `exchange`(main), `trading`.

**Request**

`GET /api/v1/private/wallet/balances`

**Response**

```json
{
    "status": "ok",
    "data": [
        {
            "walletType": "exchange",
            "currency": "DGTX",
            "balance": 100000,
        },
        {
            "walletType": "trading",
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

**Request**

`POST /api/v1/private/transfer`

| Parameter name | Parameter type | Description                            |
| -------------- | -------------- | -------------------------------------- |
| fromWallet     | string         | kind of wallet (`exchange`, `trading`) |
| toWallet       | string         | kind of wallet (`exchange`, `trading`) |
| currency       | string         |                                        |
| amount         | float          |                                        |

**Response**

General response with `ok` or `error`.

------

#### Withdrawals

**Request**

`POST /api/v1/private/wallet/withdraw`

| Parameter name | Parameter type | Description                            |
| -------------- | -------------- | -------------------------------------- |
| wallet         | string         | kind of wallet (`exchange`, `trading`) |
| method         | string         | `eth`,`btc`, `xrp`                     |
| amount         | float          |                                        |
| address        | string         | e.g. 0x25b78frd4...8n                  |
| priority       | string         | `low`, `mid`, `high`                   |

**Response**

```json
{
    "status": "ok",
    "data": {
        "withdrawalId": 123456,
        "createdAt": 1592397360000,
        "updatedAt": 1592397360000,
        "method": "eth",
        "address": "0x25b78frd4...8n",
        "priority": "mid",
        "fee": 0.05,
        "state": "PENDING"
    }
}
```

Possible withdrawal state: `PENDING`, `CONFIRMED`, `CANCELLED`, `REJECTED`, `COMPLETED`.

------

#### Trade History

**Request**

`GET /api/v1/private/trades/history`

| Parameter name | Parameter type | Description           |
| -------------- | -------------- | --------------------- |
| symbol         | string         | e.g. 'BTCUSD-PERP'    |
| from           | int64          | Timestamp             |
| to             | int64          | Timestamp             |
| limit          | int64          | Default: 10. Max: 100 |

**Response**

```json
{
    "status": "ok",
    "data": [
        {
            "id": 1234567,
            "ts": 123456789000,
            "symbol": "BTCUSD-PERP",
            "px": 9600,
            "qty": 100,
        }
    ]
}
```

------

#### Fill History

**Request**

`GET /api/v1/private/fills/history`

| Parameter name | Parameter type | Description           |
| -------------- | -------------- | --------------------- |
| symbol         | string         | e.g. 'BTCUSD-PERP'    |
| from           | int64          | Timestamp             |
| to             | int64          | Timestamp             |
| limit          | int64          | Default: 10. Max: 100 |

**Response**

```json
{
    "status": "ok",
    "data": [
        {
            "symbol": "BTCUSD-PERP",
            "createdAt": 123456789000,
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

------



**Note:** subscriptions for streams will be provided by WS API.