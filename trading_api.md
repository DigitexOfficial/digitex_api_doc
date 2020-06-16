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
| symbol         | string         |                                   |
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

#### Close contract

**Request**

`DELETE /api/v1/private/contract`

| Parameter name | Parameter type | Description                         |
| -------------- | -------------- | ----------------------------------- |
| contractId     | uint64         |                                     |
| ordType        | string         | `MARKET`/`LIMIT`                    |
| px             | float          | `px` is the price for `LIMIT` order |
| qty            | float          | `0` or omit to fully close          |

**Response**

General response with `ok` or `error`.

------

#### Get trader balance

**Request**



**Response**



------

#### Get positions

**Request**



**Response**



------

#### Close position

**Request**



**Response**



------

#### Get PNL

**Request**



**Response**



------

#### Transfer

**Request**



**Response**



------

#### Withdrawals

**Request**



**Response**



------

#### Trades

**Request**



**Response**



------

#### Fills

**Request**



**Response**



------



**Note:** subscriptions for streams will be provided by WS API.