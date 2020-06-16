# Trading API Draft

Place order

POST /api/v1/private/order

| Parameter name | Parameter type | Description                    |
| -------------- | -------------- | ------------------------------ |
| symbol         | string         |                                |
| clOrdId        | string         |                                |
| type           | string         | MARKET/LIMIT                   |
| timeInForce    | string         | GTD, GTC, GTF, FOK, IOC        |
| side           | string         | BUY/SELL                       |
| px             | float          | not required if type is MARKET |
| qty            | float          |                                |

Response

| Parameter name | Parameter type | Description |
| -------------- | -------------- | ----------- |
| ordId          | string         |             |
| clOrdId        | string         |             |

Update order



Cancel order

DELETE /api/v1/private/order

| Parameter name | Parameter type | Description |
| -------------- | -------------- | ----------- |
|                |                |             |
|                |                |             |
|                |                |             |

Cancel all orders

Close contract



get order status 

get pnl

get balances

get position

subscriptions to that

close position

withdrawals

transfer main -> trade

trade/fill history