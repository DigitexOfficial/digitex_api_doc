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

- orderbook_*depth*, where *depth* can be: 5, 10, 25, 50, 100 or 200
- kline_*interval*, where *interval* can be: 1min, 3min, 5min, 15min, 30min, 1h, 3h, 6h, 12h, 1D, 3D, 1W, 3W, 1M, 3M, 6M, 1Y
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
        "updated":1591295037813,
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

Message

```json
{
	"ch": "liquidations",
	"data":
        "symbol": "BTCUSD-PERP",
        "orders": [
            {
                "px": 9540,
                "qty": 100,
                "ts": 123456789000 
            }
	    ]
    }
}
```

#### Insurance fund channel

**Channel name:** `<symbol>@insurance`

Message

```json
{
	"ch": "insurance",
	"data": [
        {
            "currency": "BTC",
            "ts": 123456789000,
            "balance": 1000
        }
	]
}
```

#### Ticker channel

**Channel name:** `<symbol>@ticker`

Message

```json
{
	"ch": "ticker",
	"data": {
        "symbol": "BTCUSD-PERP",
	    "openTime":1590906900000,
        "closeTime":1590993300000,
	    "bidPx": 9420,
	    "bidQty": 100,
	    "askPx": 9450,
	    "askQty": 250,
	    "lastPx": 9400,
        "lastQty": 200,
	    "pxChange24h": 0.009353,
        "highPx24h": 7267.50,
        "lowPx24h": 7067.00,
        "volume24h": 78053288,
        "markPx": 7230,
        "indexPx": 7235,
        "openInterest": 117860186,
        "fundingRate": 0.0003,
        "nextFundingTime": 123456789000
    }
}
```

#### Funding channel

**Channel name:** `<symbol>@funding`

Message

```json
{
	"ch": "funding",
	"data": {
        "symbol": "BTCUSD-PERP",
	    "ts": 157743360000,
        "rate": 0.0003
    }
}
```

#### Index channel

**Channel name:** `<symbol>@index`

Message

```json
{
    "ch": "index",
	"data": {
        "symbol": "BTCUSD-PERP",
        "indexSymbol": ".DGTXBTCUSD",
        "updated": 1590999736783,
        "markPx": 9549,
        "fairPx": 9548,
        "spotPx": 9565,
        "components":{
            "binance":{
                "weight":25,"ts":0,"px":0,"vol":0
            },
            "bitfinex":{
                "weight":25,"ts":0,"px":0,"vol":0
            },
            "coinbasepro":{
                "weight":25,"ts":0,"px":0,"vol":0
            },
            "kraken":{
                "weight":25,"ts":0,"px":0,"vol":0
            }
        }
    }
}
```

