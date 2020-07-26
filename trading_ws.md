# Websocket Trading API Draft

### General

#### Messages

*<u>Note:</u> authentication request must be sent before any other trading request.*

Each request has the following structure:

```json
{
    "id":2,
    "method":"methodName",
    "params":{
        "desc": "params field could be either an object or an array"
    }
}
```

Every response has the following structure in case of success:

```json
{
    "id":2,
    "status":"ok"
} 
```

And in case of error response would be like:

```json
{
  "id":2,
  "status": "error",
  "code": 2222,
  "msg": "error description"
}
```

<u>Note</u>: the error will also be returned in case of system maintenance and absence of data for the response. 

Possible value of order's `status`:  `PENDING`, `ACCEPTED`, `REJECTED`, `CANCELLED`, `FILLED`, `PARTIALLY_FILLED`, `TERMINATED`, `EXPIRED`, `TRIGGERED`.

Possible values of `ordType`: `MARKET`, `LIMIT`.

Possible values of `timeInForce`: `GTD`, `GTC`, `GTF`, `IOC`, `FOK`.

Possible values of `side`: `BUY`, `SELL`.

Possible values of `ch` (channel name): `error`, `orderStatus`, `orderFilled`, `orderCancelled`, `contractClosed`, `traderStatus`, `traderBalance`, `position`, `funding`, `leverage`, `condOrderStatus`.

For `BTCUSD-PERP`: order price should be positive and a <u>multiple of 5</u>, order quantity should be positive and <u>integral</u>.

All timestamps are provided in milliseconds.

<u>Note</u>: the trader cannot have a mix of long and short contracts in his/her position.

#### Order Chain

Each active order in the engine has a unique order identifier (`clOrdId`). 

Value of the `clOrdId` is assigned by the trader. It should be a unique string for each order. This string can be any length, but only the first 16 bytes are used by the exchange. If the length is less than 16 bytes the trading engine will add zero bytes to make it 16 bytes total.

This original order identifier is preserved in `origClOrdId` field of the order-related messages.

Orders are immutable objects in the engine, that means that any modification to the order (full or partial fill, quantity change or leverage change, cancellation) creates a **new** order with `clOrdId` generated bu the engine. The new identifier is reported to the trader in `newClOrdId` field, and the previous (old) order identifier is reported in `oldClOrdId` field.

Full fill or cancellation also create a new empty order with a quantity 0.

Therefore the full life cycle of an order is represented by a chain of orders. All orders in the chain have the same `origClOrdId` equal to the `clOrdId` of the `placeOrder` message. The last order in the chain has `qty` field equal to 0, and all orders in the chain except the first have `oldClOrdId` field referring to the previous order in the chain.

#### Contract Chain

Contracts (or position) represent future contracts in possession of a trader. 

Each contract has a unique identifier (`contractId`) and the trader can close a particular contract using this identifier.

Contracts are immutable and any change to the existing contract, including its closing, liquidation or settlement results in creation of a **new** contract. 

Life cycle of a contract is represented by a contract chain. The last contract in the chain has `qty` equal to 0.
All contracts in the chain except the first one have `oldContractId` field referring to the previous contract in the chain.
All contracts in the chain have `origContractId` field equal to `contractId` of the first contract in the chain.
Field `oldClOrdId` is the identifier of the order that was matched and resulted in the first contract in the contract chain.

If neither fields `isIncrease`, `isFunding`, `isLiquidation` are set, the contract is created from another contract by increasing/decreasing (possibly to 0) the quantity of that contract.

A terminal contract is a contract with `qty` equal to 0. The terminal contract is always the last contract in a contract chain.
A terminal contract is created when a contract is fully closed by matching an order on the opposite side, or in case of liquidation.

------

### Trade Flow

------

#### Authentication

To authenticate, trader need to send:

```json
{
    "id":2,
    "method":"auth",
    "params":{
        "type":"token",
        "value":"yourToken"
    }
}
```

The server will respond with an appropriate `status` value.

If provided token isn't valid trader will receive the following message:

```json
{
    "id":2,
    "status":"error",
    "code":10501,
    "msg":"invalid credentials"
}
```

Trader needs to send again the `auth` message with the token every time he/she gets this error.

------

#### Trading Status

If authentication was successful and trading engine is ready to receive and process trader's request the following message will be received:

```json
{
    "ch":"tradingStatus",
    "data":{
        "available":true
    }
}
```

This message indicates that trader can start trading.

In case of maintenance, connection issues, etc. trader will receive the following:

```json
{
    "ch":"tradingStatus",
    "data":{
        "available":false
    }
}
```

This message indicates that trading is not available in that very moment.

------

#### Place Order

To place a new order the following message should be sent:

```json
{
    "id":3,
    "method":"placeOrder",
    "params":{
        "symbol":"BTCUSD-PERP",
        "clOrdId":"7b17f2d9d94a477a",
        "ordType":"MARKET",
        "timeInForce":"IOC",
        "side":"BUY",
        "px": 0,
        "qty":25
    }
} 
```

<u>Note</u>: in case of `MARKET` order field `px` could be omitted.

The order can be either accepted or rejected by the exchange.

If the order has been accepted by the trading engine trader will receive the following message:

```json
{
    "ch":"orderStatus",
    "data":{
        "symbol":"BTCUSD-PERP",
        "timestamp":1594045833043,
        "clOrdId":"7b17f2d9d94a477a",
        "origClOrdId":"7b17f2d9d94a477a",
        "openTime":1594045833043,
        "orderStatus":"ACCEPTED",
        "orderType":"MARKET",
        "orderSide":"BUY",
        "timeInForce":"IOC",
        "px":0,
        "paidPx":462.25,
        "qty":25,
        "origQty":25,
        "leverage":20,
        "traderBalance":100665.635,
        "orderMargin":0,
        "positionMargin":231.125,
        "upnl":0,
        "pnl":468.16,
        "markPx":9239.7181,
    }
}
```

The value of `clOrdId` can be used to cancel this order in the future (in case of `LIMIT` order).

`orderStatus` will have a value `ACCEPTED` or `REJECTED`. In case of `REJECTED` order a field `errCode` is set to appropriate error code.

`leverage` contains current trader's position.

`openTime` is the timestamp when the original `placeOrder` has been handled by the trading engine.

`origQty` is the quantity of the original order.

`paidPx` is the amount of funds locked on the trader's account as the margin. If `leverage` is 1, `paidPx` equals to `px`. 

`traderBalance` is the current trading balance of the trader.

`orderMargin` is the amount of funds locked in all active orders. 

`positionMargin` is the total amount of funds locked in the position (contracts, active orders). 

`upnl` is the unrealized PnL at this moment.
`pnl` is the realized PnL, i.e. the change to the trader balance achieved as the result of all trading operations since the last funding. Explicit trader's transfers to/from trading account are not accounted into PnL.

------

#### Order Fills

When order is filled trader will receive the following message:

```json
{
    "ch":"orderFilled",
    "data":{
        "symbol":"BTCUSD-PERP",
        "timestamp":1594045833043,
        "clOrdId":"7b17f2d9d94a477a",
        "orderStatus":"FILLED",
        "newClOrdId":"generated-by-the-engine",
        "origClOrdId":"7b17f2d9d94a477a",
        "openTime":1594045833043,
        "px":0,
        "paidPx":0,
        "qty":0,
        "droppedQty":0,
        "origQty":25,
        "traderBalance":100665.635,
        "orderMargin":0,
        "positionMargin":231.125,
        "upnl":0,
        "pnl":468.16,
        "positionContracts":25,
        "positionVolume":231125,
        "positionLiquidationVolume":225375,
        "positionBankruptcyVolume":219568.75,
        "positionType":"LONG",
        "markPx":9239.7181,
        "contracts":[
            {
                "timestamp":1594045833043,
                "traderId":94889,
                "contractId":612705754,
                "origContractId":612705754,
                "openTime":1594045833043,
                "positionType":"LONG",
                "entryPx":9245,
                "paidPx":462.25,
                "liquidationPx":9015,
                "bankruptcyPx":8782.75,
                "qty":25,
                "exitPx":0,
                "leverage":20,
                "oldClOrdId":"7b17f2d9d94a477a",
                "isIncrease":1,
                "entryQty":25,
                "exitQty":0,
                "exitVolume":0,
                "fundingPaidPx":0,
                "fundingQty":0,
                "fundingVolume":0,
                "fundingCount":0
            }
        ],
        "marketTrades":[
            {
                "side":"BUY",
                "px":9245,
                "paidPx":462.25,
                "qty":25,
                "leverage":20,
                "isMaker":0
            }
        ]
    }
}
```

`status` contains the order fill status. It is either `FILLED` if the order has been filled entirely, or `PARTIALLY_FILLED` if the order has been partially filled.

If the order has been partially filled, either the remainder of the order stays in the orderbook as a **new** order, or the remainder of the order is cancelled.

If the remainder of the order is cancelled, field `droppedQty` contains the quantity of the cancelled part of the order. 

In case of partial fill either `qty` > 0  or `droppedQty` > 0 but not both.

If the order has been entirely filled `qty` == 0 and `droppedQty` == 0.

`positionType` is `LONG` if the trader has long position, `SHORT` if the trader has short position.

`positionContracts` is the total amount of contracts held by the trader. This value is always non-negative. `positionVolume` is the total monetary value of the position. It is computed as sum of `px` * `qty` over all active contracts.

`positionLiquidationVolume` is the total monetary value of all liquidations of the position, i.e. sum of `liquidationPx` * `qty` over all active contracts.
`positionBankruptcyVolume` is the same for the bankruptcy price.

`contracts` contains a list of contacts that were changed as the result of this fill. 

`entryPx` is the entry price of the contract.

`paidPx` is the price which is held as position margin per unit.

`exitPx` holds the price at which the quantity was decreased.

`entryQty` contains total quantity of all increases to the contract chain.

`exitQty` contains total quantity of all decreases to the contract chain.

As opposed to the increases, the decreases may be at different exit prices, so field `exitVolume` contains the volume of all exits to the contract chain.

`fundingCount` contains number of fundings performed during the lifetime of this contract chain.
`fundingPaidPx` is the accumulated value of fundings per one unit in terms of the market price.
`fundingQty` is the total number of units accumulated during all fundings.
`fundingVolume` is the total volume (`px` * `qty`) of all funding during the contract lifetime.

<u>Note</u>: the funding information is reset to 0 if the quantity of the contract is increased and the trader has enough funds on his/her trading balance to replenish the position margin for this contract to the original value.

Trader can use the value of `contractId` to close specific contract in the future using this ID.

`openTime` is the timestamp of the first contract in the contract chain.

`marketTrades` contains the list of trades of this trader performed as the result of the fill.

`isMaker` is set to 1, if this trade resulted from filling up the order already in the orderbook.

<u>Note</u>: the value of `newClOrdId` is generated by the exchange (16 bytes). It's the ID of `FILLED` order and this order has the reference to the originally placed order via `origClOrdId`.

------

#### Order Cancellation

Specific order can be cancelled using its `clOrdId` via the following message:

```json
{
    "id":4,
    "method":"cancelOrder",
    "params":{
        "symbol":"BTCUSD-PERP",
        "clOrdId":"dff7de23224c4929"
    }
}
```

More than one order can be cancelled using the following message:

```json
{
    "id":5,
    "method":"cancelAllOrders",
    "params":{
        "symbol":"BTCUSD-PERP",
        "px":0,
        "side":"BUY"
    }
}
```

Trader can cancel all the orders (`side` and `px` are omitted) or just orders with the specified `side`  and/or `px`.

The following message will be received as a result of order/orders cancellation:

```json
{
    "ch":"orderCancelled",
    "data":{
        "symbol":"BTCUSD-PERP",
        "timestamp":1594048959068,
        "orderStatus":"CANCELLED",
        "orders":[
            {
                "timestamp":1594048949070,
                "clOrdId":"generated-by-the-engine",
                "oldClOrdId":"af0574c0f09743fe",
                "origClOrdId":"af0574c0f09743fe",
                "traderId":94889,
                "openTime":1594048949070,
                "orderType":"LIMIT",
                "orderSide":"BUY",
                "timeInForce":"GTC",
                "px":9100,
                "qty":85,
                "origQty":85,
                "paidPx":455,
                "leverage":20
            },
            {
                "timestamp":1594048949068,
                "clOrdId":"generated-by-the-engine",
                "oldClOrdId":"36cbaf53b17c4a7e",
                "origClOrdId":"36cbaf53b17c4a7e",
                "traderId":94889,
                "openTime":1594048949068,
                "orderType":"LIMIT",
                "orderSide":"BUY",
                "timeInForce":"GTC",
                "px":9150,
                "qty":75,
                "origQty":75,
                "paidPx":457.5,
                "leverage":20
            }
        ],
        "traderBalance":100665.635,
        "orderMargin":0,
        "positionMargin":231.125,
        "upnl":15,
        "pnl":468.16,
        "markPx":9274.7042
    }
}
```

<u>Note</u>: `CENCELLED` order ID (`clOrdId`) - differs from ID of placed order (`oldClOrdId`).

Another valid value for `orderStatus` is `TERMINATED` which is used when orders are cancelled by the exchange.

In case of error `orderStatus` will be set to `REJECTED` and `errCode` will indicate the error.

`GFD` (good for day) orders are cancelled automatically by the engine at 00:00:00 UTC of the next day. The trader will receive `orderCancelled`with the `orderStatus` equal to `EXPIRED`.

`GTF` (good till funding) orders are cancelled automatically by the engine at the next funding (i.e 00:00:00, 08:00:00, 16:00:00 UTC). The trader will receive `orderCancelled` with the `orderStatus` equal to `EXPIRED`.

Field `orders` contains all the orders that have been cancelled. 

<u>Note</u>: the value of `clOrdId` is generated by the exchange (16 bytes).

------

#### Conditional Orders

##### Placement

Trader can schedule order placement if particular condition would be met. The value of  either `SPOT_PRICE` or `LAST_PRICE` can act as a trigger. The following message schedules order placement:

```json
{
    "id":4,
    "method":"placeCondOrder",
    "params":{
        "actionId":"a5b90ca768754b75",
        "pxType":"SPOT_PRICE",
        "condition":"LESS_EQUAL",
        "pxValue":9105,
        "symbol":"BTCUSD-PERP",
        "clOrdId":"010e2b91e5214410",
        "ordType":"LIMIT",
        "timeInForce":"GTC",
        "side":"BUY",
        "px":9105,
        "qty":100,
        "mayIncrPosition": true
    }
} 
```

`actionId` can be set by the trader or will be generated by the exchange. This value can be used later to cancel order placement.

`pxType` can be either `SPOT_PRICE` or `LAST_PRICE`.

<u>Note</u>: currently only `SPOT_PRICE` is supported.

`condition` represents the condition that should be met. Possible values: `GREATER_EQUAL`, `LESS_EQUAL`.

`pxValue` is the value to which `SPOT_PRICE` or `LAST_PRICE` will be compared using `condition`.

`mayIncrPosition` should be set to `true` if the order is allowed to change the sign of the trader's position.

When the condition is triggered a new order with the parameters `symbol`, `clOrdId`, `ordType`, `timeInForce`, `side`, `px`, `qty` will be placed. 

If a conditional order was created successfully the exchange will send the following message in response:

```json
{
    "ch":"condOrderStatus",
    "data":{
        "symbol":"BTCUSD-PERP",
        "status":"ACCEPTED",
        "conditionalOrders":[
            {
                "ts":1594379135077,
                "actionId":"a5b90ca768754b75",
                "pxType":"SPOT_PRICE",
                "condition":"LESS_EQUAL",
                "pxValue":9105,
                "clOrdId":"010e2b91e5214410",
                "ordType":"LIMIT",
                "side":"BUY",
                "timeInForce":"GTC",
                "px":9105,
                "qty":100,
                "mayIncrPosition": true
            }
        ]
    }
}
```

In case of an error the value of `status` will be set to `REJECTED` and `errCode` will provide the appropriate error code.

When conditional order is triggered the exchange will inform the trader with the following message and activate the order:

```json
{
    "ch":"condOrderStatus",
    "data":{
        "symbol":"BTCUSD-PERP",
        "status":"TRIGGERED",
        "conditionalOrders":[
            {
                "ts":1594383515908,
                "actionId":"generated-by-the-engine",
                "oldActionId":"0559991a2f042d6",
                "pxType":"SPOT_PRICE",
                "condition":"GREATER_EQUAL",
                "pxValue":9185,
                "clOrdId":"5689b870f57e4edf",
                "ordType":"MARKET",
                "side":"SELL",
                "timeInForce":"FOK",
                "px":0,
                "qty":25,
                "mayIncrPosition": true
            }
        ]
    }
} 
```

<u>Note</u>: the value of `actionId` is generated by the exchange (16 bytes).

##### Cancellation

The trader can cancel previously placed conditional order using corresponding `actionId`:

```json
{
    "id":4,
    "method":"cancelCondOrder",
    "params":{
        "symbol":"BTCUSD-PERP",
        "actionId":"a5b90ca768754b75",
        "allForTrader":false
    }
}
```

All conditional orders can be cancelled by setting `allForTrader` to `true`. In this case `actionId` can be omitted.

The exchange will send a list of all cancelled conditional orders:

```json
{
    "ch":"condOrderStatus",
    "data":{
        "symbol":"BTCUSD-PERP",
        "status":"CANCELLED",
        "conditionalOrders":[
            {
                "ts":1594379135077,
                "actionId":"generated-by-the-engine",
                "oldActionId":"a5b90ca768754b75",
                "pxType":"SPOT_PRICE",
                "condition":"LESS_EQUAL",
                "pxValue":9105,
                "clOrdId":"010e2b91e5214410",
                "ordType":"LIMIT",
                "side":"BUY",
                "timeInForce":"GTC",
                "px":9105,
                "qty":100,
                "mayIncrPosition": true
            }
        ]
    }
}
```

For each cancelled conditional order the engine will generate a new `actionId`. 

The previous one will be assigned to field `oldActionId`.

In case of error the value of `status` will be set to `REJECTED` and `errCode` will contain the appropriate error code.

------

#### Close Contracts

##### One Contract

Trader can close a specific contract using its ID (`contractId`). 

There is an option to specify order type (`MARKET` or `LIMIT`), price (only for `LIMIT`) and quantity (to close only a part of the contract) for a contract close operation.

A particular contract can be closed via the following message:

```json
{
    "id":7,
    "method":"closeContract",
    "params":{
        "symbol":"BTCUSD-PERP",
        "contractId":612705754,
        "ordType":"MARKET",
        "px":0,
        "qty":10
    }
}
```

And the response message will be the following:

```json
{
    "ch":"contractClosed",
    "data":{
        "symbol":"BTCUSD-PERP",
        "orderIds":[
            "generated-by-the-engine"
        ]
    }
} 
```

`orderIds` contains an array of `clOrdId`s which have been created by the exchange to close the contract.

If an error occurs (e.g. unknown `contractId`) an array `orderIds` will be empty and `errCode` will be set to appropriate value.

Trader also will receive `orderStatus` and `orderFilled` messages related to these orders. The latter one will contain the information about affected contracts.

```json
{
    "ch":"orderStatus",
    "data":{
        "symbol":"BTCUSD-PERP",
        "timestamp":1594113819695,
        "clOrdId":"generated-by-the-engine",
        "origClOrdId":"generated-by-the-engine",
        "openTime":1594113819695,
        "orderStatus":"ACCEPTED",
        "orderType":"MARKET",
        "orderSide":"SELL",
        "timeInForce":"GTC",
        "px":0,
        "paidPx":0,
        "qty":50,
        "origQty":50,
        "leverage":10,
        "traderBalance":100552.596,
        "orderMargin":0,
        "positionMargin":0,
        "upnl":0,
        "pnl":7.11,
        "markPx":9242.3196,
        "oldContractId":613903122 
    }
} 
```

```json
{
    "ch":"orderFilled",
    "data":{
        "symbol":"BTCUSD-PERP",
        "timestamp":1594113819695,
        "clOrdId":"id-of-accepted-order",
        "newClOrdId":"generated-by-the-engine",
        "origClOrdId":"id-of-origin-order",
        "openTime":1594113819695,
        "orderStatus":"FILLED",
        "px":0,
        "paidPx":0,
        "qty":0,
        "origQty":50,
        "droppedQty":0,
        "traderBalance":100552.596,
        "orderMargin":0,
        "positionMargin":0,
        "upnl":0,
        "pnl":7.11,
        "positionContracts":0,
        "positionVolume":0,
        "positionLiquidationVolume":0,
        "positionBankruptcyVolume":0,
        "markPx":9242.3196,
        "contracts":[
            {
                "contractId":613903300,
                "origContractId":613903122,
                "entryPx":9240,
                "paidPx":0,
                "liquidationPx":0,
                "bankruptcyPx":0,
                "qty":0,
                "exitPx":9240,
                "oldContractId":613903122,
                "entryQty":0,
                "exitQty":50,
                "exitVolume":462000,
                "fundingPaidPx":0,
                "fundingQty":0,
                "fundingVolume":0,
                "fundingCount":0
            }
        ]
    }
}
```

<u>Note</u>: if the trader closes only a part of the contract the exchange will generate **new** ID for the remained part of the contract (this ID can be found in `orderFilled` message).

##### All Contracts

The trader can close the position (all available contracts) via the following message:

```json
{
    "id":8,
    "method":"closePosition",
    "params":{
        "symbol":"BTCUSD-PERP",
        "ordType":"MARKET",
        "px":0
    }
}
```

Trader can specify `ordType` (`MARKET` or `LIMIT`) and `px` (if `ordType` is set to `LIMIT`).

A sequence of messages that will be received as a result is the same as in the case of closing a single contract (`contractClosed`, `orderStatus`, `orderFilled`).

------

#### Request Trader Status

Trader can request his/her status via the following message:

```json
{
    "id":9,
    "method":"getTraderStatus",
    "params":{
        "symbol":"BTCUSD-PERP"
    }
}
```

The exchange will send the following message in response:

```json
{
    "ch":"traderStatus",
    "data":{
        "symbol":"BTCUSD-PERP",
        "traderBalance":100693.356,
        "orderMargin":465.5,
        "positionMargin":466,
        "upnl":0,
        "pnl":20.721,
        "positionContracts":50,
        "positionVolume":466000,
        "positionLiquidationVolume":454500,
        "positionBankruptcyVolume":442700,
        "positionType":"LONG",
        "contracts":[
            {
                "timestamp":1594052943135,
                "traderId":94889,
                "contractId":612835558,
                "openTime":1594052943135,
                "positionType":"LONG",
                "entryPx":9320,
                "paidPx":466,
                "liquidationPx":9090,
                "bankruptcyPx":8854,
                "qty":50,
                "exitPx":0,
                "leverage":20,
                "entryQty":50,
                "exitQty":0,
                "exitVolume":0,
                "fundingPaidPx":0,
                "fundingQty":0,
                "fundingVolume":0,
                "fundingCount":0,
                "origContractId":612835558
            }
        ],
        "activeOrders":[
            {
                "clOrdId":"generated-by-the-engine",
                "origClOrdId":"generated-by-the-engine",
                "timestamp":1594052913550,
                "openTime":1594052913550,
                "orderType":"LIMIT",
                "orderSide":"BUY",
                "timeInForce":"GTC",
                "px":9310,
                "paidPx":465.5,
                "qty":50,
                "origQty":50,
                "leverage":20
            }
        ],
        "conditionalOrders":[
            {
                "ts":1594382892283,
                "actionId":"09ce730f642247ce",
                "pxType":"SPOT_PRICE",
                "condition":"GREATER_EQUAL",
                "pxValue":9190,
                "clOrdId":"d4a9aec2b8e54537",
                "ordType":"MARKET",
                "side":"SELL",
                "timeInForce":"FOK",
                "px":0,
                "qty":75,
                "mayIncrPosition": true
            }
        ],
        "leverage":20,
        "markPx":9317.4806
    }
}
```

This message contains trader's balance, current position, active orders (can be cancelled using corresponding `clOrdId`), conditional orders (can be cancelled using corresponding `actionId`) and contracts (can be closed using corresponding `contractId`).

------

#### Change Leverage

Trader can change the value of current leverage via the  following message:

```json
{
    "id":2,
    "method":"changeLeverageAll",
    "params":{
        "symbol":"BTCUSD-PERP",
        "leverage":10
    }
}
```

Where `leverage` is the desired leverage.

In case of success the exchange will respond with the following:

```json
{
    "ch":"leverage",
    "data":{
        "symbol":"BTCUSD-PERP",
        "leverage":10,
        "traderBalance":100693.356,
        "orderMargin":0,
        "positionMargin":1863,
        "upnl":-10,
        "pnl":20.721,
        "positionContracts":100,
        "positionVolume":931500,
        "positionLiquidationVolume":885000,
        "positionBankruptcyVolume":838350,
        "positionType":"LONG",
        "contracts":[
            {
                "timestamp":1594053698798,
                "traderId":94889,
                "contractId":612847804,
                "oldContractId":612837668,
                "openTime":1594053061352,
                "positionType":"LONG",
                "entryPx":9310,
                "paidPx":931,
                "liquidationPx":8845,
                "bankruptcyPx":8379,
                "qty":50,
                "exitPx":0,
                "leverage":10,
                "entryQty":50,
                "exitQty":0,
                "exitVolume":0,
                "fundingPaidPx":0,
                "fundingQty":0,
                "fundingVolume":0,
                "fundingCount":0,
                "origContractId":612837668
            },
            {
                "timestamp":1594053698798,
                "traderId":94889,
                "contractId":612847805,
                "oldContractId":612835558,
                "origContractId":612835558,
                "openTime":1594052943135,
                "positionType":"LONG",
                "entryPx":9320,
                "paidPx":932,
                "liquidationPx":8855,
                "bankruptcyPx":8388,
                "qty":50,
                "exitPx":0,
                "leverage":10,
                "entryQty":50,
                "exitQty":0,
                "exitVolume":0,
                "fundingPaidPx":0,
                "fundingQty":0,
                "fundingVolume":0,
                "fundingCount":0
            }
        ]
    }
}
```

This message contains trader's balance, current position, active orders (can be cancelled using corresponding `clOrdId`) and contracts (can be closed using corresponding `contractId`) according to a new leverage value.

<u>Note</u>: trader must renew contracts and active orders on his/her side according to the new values of `contracts` and `activeOrders`.  After this operation (leverage changing) all trader's contracts and active orders will change their identifiers - trading engine will assign the new ones to them.

In case of error (e.g. invalid new leverage value) the response will contain the appropriate `errCode` and `contracts`, `activeOrders` will be empty. Nothing will change.

------

#### Funding

Trader will receive the following message if he/she has open position during funding:

```json
{
    "ch":"funding",
    "data":{
        "symbol":"BTCUSD-PERP",
        "traderBalance":100549.736,
        "orderMargin":0,
        "positionMargin":1850.59,
        "upnl":0,
        "pnl":0,
        "positionContracts":0,
        "positionVolume":0,
        "positionLiquidationVolume":0,
        "positionBankruptcyVolume":0,
        "payout":-1.86,
        "payoutPerContract":0.0186,
        "markPx":238.8477,
        "positionMarginChange":-1.86,
        "contracts":[
            {
                "timestamp":1594137600000,
                "traderId":94889,
                "positionType":"LONG",
                "entryPx":9275,
                "paidPx":927.5,
                "liquidationPx":8815,
                "bankruptcyPx":8348.43,
                "qty":25,
                "exitPx":0,
                "leverage":10,
                "contractId":614339945,
                "oldContractId":614224561,
                "openTime":1594122555760,
                "entryQty":25,
                "exitQty":0,
                "exitVolume":0,
                "fundingPaidPx":0.93,
                "fundingQty":25,
                "fundingVolume":23.25,
                "fundingCount":1,
                "isFunding":1,
                "origContractId":614053631
            },
            {
                ...omitted...
            },
            {
                ...omitted...
            }
        ]
    }
} 
```

`payoutPerContract` is the value of the payout per contract during the funding.

------

#### Position

If trader's position has been liquidated and/or active orders have been terminated by the exchange the following message will be received:

```json
{
    "ch":"position",
    "data":{
        "symbol":"BTCUSD-PERP",
        "liquidatedContracts":[array of contracts],
        "terminatedOrders":[only clOrdId of orders],
        "traderBalance": 2000,
        "orderMargin": 0,
        "positionMargin": 0,
        "upnl": 0,
        "pnl": 0,
        "accumQty": 0,
        "positionContracts": 0,
        "positionVolume": 0,
        "positionLiquidationVolume": 0,
        "positionBankruptcyVolume": 0,
        "traderBalanceIncrement": 1000,
        "markPx": 9285
    }
}
        
```

`liquidatedContracts` contains an array of liquidated contracts (the same structure as in `traderStatus` message).

`terminatedOrders` contains an array of `clOrdId`s of terminated orders.

------

#### Error codes

Trader can receive error code with the response for a specific request (e.g. `placeOrder`).

| Code  | Description                           |
| ----- | ------------------------------------- |
| 3     | ID already exists                     |
| 10    | ID doesn't exist                      |
| 14    | Unknown trader                        |
| 18    | Invalid leverage                      |
| 19    | Invalid price                         |
| 20    | Invalid quantity                      |
| 22    | No market price                       |
| 27    | Not enough balance                    |
| 34    | Invalid contract ID                   |
| 35    | Rate limit exceeded                   |
| 36    | No contracts                          |
| 37    | No opposing orders                    |
| 40    | Price is worse than liquidation price |
| 45    | Tournament in progress                |
| 53    | Max quantity exceeded                 |
| 54    | PnL is too negative                   |
| 55    | Order would become invalid            |
| 58    | Trading suspended                     |
| 63    | Can't be filled                       |
| 65    | Too many conditional orders           |
| 68    | Too many orders                       |
| 3001  | Bad request                           |
| 3011  | Not implemented                       |
| 3012  | Internal error                        |
| 3013  | Not authorized                        |
| 3014  | Already authorized                    |
| 3015  | Trading is not available              |
| 3016  | Authentication in progress            |
| 10501 | Invalid credentials                   |

In case of a general error the following message will be sent by the server:

```json
{
    "ch":"error",
    "data":{
        "code":error_code,
        "msg":"error message"
    }
}
```

------

#### 