### Public Websocket API Draft

#### General information

Server send message `ping` every 30 seconds. Client should respond with message `pong` or it would be disconnected. 

The `id` used in JSON as an identifier of the request. The response for the particular request has the same `id` value.

#### Subscribe to a channel

**Request**

```json
{
    "id": 1,
    "method": "subscribe",
    "params": [
        "BTCUSD-PERP@orderbook_25"
    ]
}
```

**Response**

```json
{
    "id": 1,
    "status": "ok"
}
```

#### Unsubscribe from a channel

**Request**

```json
{
    "id": 1,
    "method": "unsubscribe",
    "params": [
        "BTCUSD-PERP@orderbook_25"
    ]
}
```

**Response**

```json
{
    "id": 1,
    "status": "ok"
}
```

**Response in case of error**

```json
{
    "id": 1,
    "status": "error",
    "code": 501,
    "msg": "unknown contract"
}
```

#### Subscription list

**Request**

```json
{
    "id": 1,
    "method": "subscriptions",
    "params": []
}
```

**Response**

```json
{
    "id":2,
    "status":"ok",
    "result":[
        "BTCUSD-PERP@kline_1min"
    ]
} 
```

#### List of public channels

- orderbook_*depth*, where *depth* can be: `5`, `10`, `25`, `50` of `full`.
- kline_*interval*, where *interval* can be: `1min`, `3min`, `5min`, `15min`, `30min`, `1h`, `3h`, `6h`, `12h`, `1D`, `3D`, `1W`, `3W`, `1M`, `3M`, `6M`, `1Y`
- trades
- liquidations
- insurance
- ticker
- funding
- index

#### Orderbook channel

**Channel name:** `<symbol>@orderbook_5`

Message

```json
{
    "ch":"orderbook_5",
    "data":{
        "symbol":"BTCUSD-PERP",
        "ts":1591295037813,
        "bids":[
            [9840,53914],[9835,26103],[9830,37644],[9825,21331],[9820,43942]
        ],
        "asks":[
            [9845,15899],[9850,85810],[9855,41480],[9860,39565],[9865,40374]
        ]
    }
} 
```

#### Trade channel

**Channel name:** `<symbol>@trades`

Message

```json
{
    "ch":"trades",
    "data":{
        "symbol":"BTCUSD-PERP",
        "trades":[
            {"px":9845,"qty":2356,"ts":1591295123213},
            {"px":9845,"qty":75,"ts":1591295123213}
        ]
    }
} 
```

#### Kline channel

**Channel name:** `<symbol>@kline_1min`

Only `1min` interval is supported now.

*Kline history is in development, only single kline is published every minute*

Message

```json
{
    "ch":"kline_1min",
    "data":{
        "symbol":"BTCUSD-PERP",
        "interval":"1min",
        "id":1591295280,
        "o":9835,
        "h":9840,
        "l":9825,
        "c":9830,
        "v":654088
    }
}
```

#### Liquidations channel

**Channel name:** `<symbol>@liquidations`

**Note:** not implemented yet.

Message

```json
{
    "ch":"liquidations",
    "data":{
        "symbol":"BTCUSD-PERP",
        "orders":[
            {"px":9540,"qty":100,"ts":123456789000}
        ]
    }
}
```

#### Insurance fund channel

**Channel name:** `exchange@insurance`

**Note:** not implemented yet.

Message

```json
{
    "ch":"insurance",
    "data":[
        {"currency":"DGTX","ts":123456789000,"balance":1000}
    ]
}
```

#### Ticker channel

**Channel name:** `<symbol>@ticker`

Message

```json
{
    "ch":"ticker",
    "data":{
        "symbol":"BTCUSD-PERP",
        "openTime":1590906900000,
        "closeTime":1590993300000,
        "openPx": 9250,
        "highPx24h":9450,
        "lowPx24h":9100,
        "pxChange24h": -3.35,
        "volume24h":78053288,
        "volume24hUsd":2852425063.05,
        "bidPx":9420,
        "bidQty":100,
        "askPx":9450,
        "askQty":250,
        "lastPx":9400,
        "lastQty":200,
        "fundingRate":0.0003,
        "nextFundingTime":123456789000,
        "contractValue":194.9,
        "dgtxUsdRate":0.03728994
    }
}
```

`volume24hUsd` is calculated as: `volume24h` * `contractValue` * `dgtxUsdRate`.

`contractValue` is calculated as: `lastTradePx` / `TICK_SIZE` * `TICK_PRICE`, where `TICK_SIZE`=5 and `TICK_PRICE`=0.1 for BTCUSD-PERP contract.

#### Funding channel

**Channel name:** `<symbol>@funding`

Message

```json
{
    "ch":"funding",
    "data":{
        "symbol":"BTCUSD-PERP",
        "ts":157743360000,
        "rate":0.0003
    }
}
```

#### Index channel

**Channel name:** `<symbol>@index`

Symbol can be either a contract symbol (`BTCUSD-PERP`) or index symbol (`.DGTXBTCUSD`).

Message

```json
{
    "ch":"index",
    "data":{
        "indexSymbol":".DGTXBTCUSD",
        "ts":1590999736783,
        "markPx":9549,
        "fairPx":9549,
        "spotPx":9565,
        "components":{
            "binance":{"weight":25,"ts":0,"px":0,"vol":0},
            "bitfinex":{"weight":25,"ts":0,"px":0,"vol":0},
            "coinbasepro":{"weight":25,"ts":0,"px":0,"vol":0},
            "kraken":{"weight":25,"ts":0,"px":0,"vol":0}
        }
    }
}
```

#### Error codes

| Code | Description                                               |
| ---- | --------------------------------------------------------- |
| 3001 | Bad Request (unknown method, ill-formed parameters, etc.) |
| 3002 | Channel not found                                         |
| 3003 | Contract not found                                        |
| 3004 | Index not found                                           |
| 3005 | Kline interval not specified                              |
| 3006 | Kline interval not found                                  |
| 3007 | Orderbook depth not specified                             |
| 3008 | Orderbook depth not found                                 |
| 3009 | Already subscribed for the topic                          |
| 3010 | Not subscribed for the topic                              |
| 3011 | Feature is not implemented yet                            |
| 3012 | Other error                                               |

