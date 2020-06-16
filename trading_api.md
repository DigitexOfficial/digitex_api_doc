# Trading API Draft

*<u>Note:</u> for each private request authentification is required.*

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

------

#### Place order

**Request**

`POST /api/v1/private/order`

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

| Parameter name | Parameter type | Description            |
| -------------- | -------------- | ---------------------- |
| ordId          | string         | assigned by the API    |
| clOrdId        | string         | provided by the trader |

------

#### Get order status

**Request**

`GET /api/v1/private/order`

| Parameter name | Parameter type | Description            |
| -------------- | -------------- | ---------------------- |
| ordId          | string         | assigned by the API    |
| clOrdId        | string         | provided by the trader |

**Response**

| Parameter name        | Parameter type | Description                                                  |
| --------------------- | -------------- | ------------------------------------------------------------ |
| symbol                | string         | e.g. 'BTCUSD-PERP'                                           |
| ordId                 | string         | assigned by the API                                          |
| clOrdId               | string         | assigned by the trader                                       |
| createdAt             | int64          | Timestamp                                                    |
| updatedAt             | int64          | Timestamp                                                    |
| ordType               | string         | `MARKET`/`LIMIT`                                             |
| timeInForce           | string         | `GTD`, `GTC`, `GTF`, `IOC`, `FOK`                            |
| side                  | string         | `BUY`/`SELL`                                                 |
| px                    | float          | not required if type is `MARKET`                             |
| qty                   | float          |                                                              |
| status                | string         | `UNDEFINED`, `PENDING`, `ACCEPTED`, `REJECTED`, `CANCELED`, `FILLED`, `PARTIAL`, `TERMINATED`, `EXPIRED`, `TRIGGERED` |
| filledQty/cumQty      | float          | total quantity filled                                        |
| unfilledQty/leavesQty | float          | unfilled order quantity                                      |

------

#### Get active orders

**Request**

`GET /api/v1/private/orders/active`

| Parameter name | Parameter type | Description                  |
| -------------- | -------------- | ---------------------------- |
| symbol         | string         | e.g. 'BTCUSD-PERP'; optional |

**Response**

List of objects, each has the following fields:

| Parameter name | Parameter type | Description                                                  |
| -------------- | -------------- | ------------------------------------------------------------ |
| symbol         | string         | e.g. 'BTCUSD-PERP'                                           |
| ordId          | string         | assigned by the API                                          |
| clOrdId        | string         | assigned by the trader                                       |
| createdAt      | int64          | Timestamp                                                    |
| updatedAt      | int64          | Timestamp                                                    |
| ordType        | string         | `MARKET`/`LIMIT`                                             |
| timeInForce    | string         | `GTD`, `GTC`, `GTF`, `IOC`, `FOK`                            |
| side           | string         | `BUY`/`SELL`                                                 |
| px             | float          | not required if type is `MARKET`                             |
| qty            | float          |                                                              |
| status         | string         | `UNDEFINED`, `PENDING`, `ACCEPTED`, `REJECTED`, `CANCELED`, `FILLED`, `PARTIAL`, `TERMINATED`, `EXPIRED`, `TRIGGERED` |
| filledQty      | float          | total quantity filled                                        |
| avgPx          | float          | average price of all order fills                             |

------

#### Update order

**Request**

`PATCH /api/v1/private/order`

| Parameter name | Parameter type | Description                       |
| -------------- | -------------- | --------------------------------- |
| symbol         | string         | e.g. 'BTCUSD-PERP'                |
| oldClOrdId     | string         | `clOrdId` of the original order   |
| clOrdId        | string         | assigned by the trader            |
| ordType        | string         | `MARKET`/`LIMIT`                  |
| timeInForce    | string         | `GTD`, `GTC`, `GTF`,` IOC`, `FOK` |
| side           | string         | `BUY`/`SELL`                      |
| px             | float          | not required if type is `MARKET`  |
| qty            | float          |                                   |

For `BTCUSD-PERP`: `px` should be positive and <u>multiple of 5</u>, `qty` positive and <u>integral</u>.

**Response**

| Parameter name | Parameter type | Description            |
| -------------- | -------------- | ---------------------- |
| ordId          | string         | assigned by the API    |
| clOrdId        | string         | provided by the trader |

`ordId` and `clOrdId` are identificators of the new order.

------

#### Cancel order

You can cancel the order by the Internal Order ID (`ordId`) or using a Client Order ID (`clOrdId`).

**Request**

`DELETE /api/v1/private/order`

| Parameter name | Parameter type | Description            |
| -------------- | -------------- | ---------------------- |
| ordId          | string         | assigned by the API    |
| clOrdId        | string         | provided by the trader |

**Response**

General response with `ok` or `error`.

------

#### Cancel orders

Trader can cancel all the orders (`side` is omited) or just orders with the specified `side` .

**Request**

`DELETE /api/v1/private/orders`

| Parameter name | Parameter type | Description            |
| -------------- | -------------- | ---------------------- |
| side           | string         | `BUY`/`SELL`; optional |

**Response**

General response with `ok` or `error`.

------

#### Close contract (the same as close position?)

**Request**

`DELETE /api/v1/private/contract`

| Parameter name | Parameter type | Description                         |
| -------------- | -------------- | ----------------------------------- |
| contractId     | uint64         | what is `contractID`???             |
| ordType        | string         | `MARKET`/`LIMIT`                    |
| px             | float          | `px` is the price for `LIMIT` order |
| qty            | float          | `0` or omit to fully close          |

**Response**

General response with `ok` or `error`.

------

#### Get trader balance

**Request**

`GET /api/v1/private/wallet/balances`

**Response**

```json
{
    "status": "ok",
    "data": [
        {
            "currency": "DGTX",
            "balance": 100000,
            "orderMargin": 5000,
            "positionMargin": 3000
        }
    ]
}
```

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
            "symbol": "BTCUSD-PERP",
            "type": "long/short",
            "pnl": 50,
            "upnl": 10,
            "contracts": 500,
            "volume": 10000,
            "liquidationVolume": 500,
            "bankruptcyVolume": 500,
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

#### Transfer

**Request**

`POST /api/v1/private/transfer`

| Parameter name | Parameter type | Description |
| -------------- | -------------- | ----------- |
| fromWallet     | string         |             |
| toWallet       | string         |             |
| currency       | string         |             |
| amount         | float          |             |

**Response**

General response with `ok` or `error`.

------

#### Withdrawals

**Request**

`POST /api/v1/wallet/withdrawal`

| Parameter name | Parameter type | Description |
| -------------- | -------------- | ----------- |
| wallet         | string         |             |
| currency       | string         |             |
| amount         | float          |             |
| address        | string         |             |

**Response**

General response with `ok` or `error`.

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
            "ordId": "123456",
            "side": "BUY/SELL",
            "px": 9600,
            "qty": 100,
            "ordPx": 9600,
            "ordType": "MARKET/LIMIT",
            "maker": true/false
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
            "ordId": "1234",
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