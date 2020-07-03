# DIGITEX Futures API Draft

## Market Data API

*NOTE* This is *ALPHA-VERSION* of API. In future versions of API could be incompatible changes.

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

**Note:** the error will also be returned in case of system maintenance and absence of data for the response. 

### Endpoints

*REST API URL* https://rest-api.sandbox.digitex.fun 

*WS API URL* wss://ws-api.sandbox.digitex.fun

#### Public - Contracts

**HTTP Request**

`GET /api/v1/public/contracts`

**Response**

```json
{
    "status":"ok",
    "ts":1590404891291,
    "data":[
        {
            "id":1,
            "name":"BTC/USD-PERP",
            "symbol":"BTCUSD-PERP",
            "type":"perpetual_futures",
            "isTradable":true,
            "baseCurrency":"BTC",
            "quoteCurrency":"USD",
            "pnlCurrency":"DGTX",
            "marginCurrency":"DGTX",
            "lotSize":1,
            "tickPrice":1,
            "isQuanto":true,
            "isInverse":false,
            "underlyingAsset":"token",
            "indexSymbol":".DGTXBTCUSD",
            "premiumIndexSymbol":"",
            "fundingRate":0.0003,
            "fundingPeriod":28800,
            "indicativeFundingRate":0,
            "markType":"fair_price",
            "initMargin":0,
            "maintMargin":0,
            "deleverage":false,
            "isLeverage": true,
            "maxLeverage": 20,
            "createTime":0,
            "listingTime":0,
            "expiryTime":0,
            "settleTime":0,
            "makerFee":0,
            "takerFee":0,
            "settlementFee":0,
            "insuranceFee":0,
            "minPrice":0,
            "maxPrice":0
        }
    ]
}
```

------

#### Public - Assets

**HTTP Request**

`GET /api/v1/public/assets`

**Response**

```json
{
   "status":"ok",
   "ts":1590428686166,
   "data":[
       {
         "id":1,
         "name":"Digitex Token",
         "symbol":"DGTX",
         "type":"token",
         "precision":4,
         "hasDeposit":true,
         "hasWithdraw":true,
         "depositFee":0,
         "withdrawFee":0,
         "minDepositSize":0,
         "maxDepositSize":0
      },
      {
         "id":2,
         "name":"Bitcoin",
         "symbol":"BTC",
         "type":"coin",
         "precision":8,
         "hasDeposit":false,
         "hasWithdraw":false,
         "depositFee":0,
         "withdrawFee":0,
         "minDepositSize":0,
         "maxDepositSize":0
      },
      {
         "id":3,
         "name":"US Dollar",
         "symbol":"USD",
         "type":"coin",
         "precision":2,
         "hasDeposit":false,
         "hasWithdraw":false,
         "depositFee":0,
         "withdrawFee":0,
         "minDepositSize":0,
         "maxDepositSize":0
      },
      {
         "id":4,
         "name":"Ethereum",
         "symbol":"ETH",
         "type":"coin",
         "precision":8,
         "hasDeposit":false,
         "hasWithdraw":false,
         "depositFee":0,
         "withdrawFee":0,
         "minDepositSize":0,
         "maxDepositSize":0
      },
      {
         "id":5,
         "name":"Ripple",
         "symbol":"XRP",
         "type":"coin",
         "precision":8,
         "hasDeposit":false,
         "hasWithdraw":false,
         "depositFee":0,
         "withdrawFee":0,
         "minDepositSize":0,
         "maxDepositSize":0
      }
   ]
}
```

------

#### Public - Ping

**HTTP Request**

`GET /api/v1/public/ping`

**Response**

```json
{}
```

------

#### Public - Announcement

**HTTP Request**

`GET /api/v1/public/announcement`

**Response**

```json
{
  "status": "ok",
  "ts":1590402678700,
  "data": [
    {
      "id": 1,
      "link": "string",
      "title": "string",
      "content": "string",
      "date": "2020-05-21T08:08:49.464Z",
      "tags": ["tag1", "tag2"],
      "urgent": true,
    },
    {
      "id": 2,
      "link": "string",
      "title": "string",
      "content": "string",
      "date": "2020-05-21T08:08:49.464Z",
      "tags": ["tag3"],
      "urgent": false,
    }
  ]
}
```

------

#### Public - Time

**HTTP Request**

`GET /api/v1/public/time`

**Response**

```json
{
    "status":"ok",
    "data":{
        "iso":"2020-06-01T09:17:46.825",
        "timestamp":1590992266825
    }
}
```

------

#### Public - Orderbook

**HTTP Request**

`GET /api/v1/public/orderbook`

| Parameters | Type   | Description          |
| ---------- | ------ | -------------------- |
| symbol     | String | e.g. 'BTCUSD-PERP'   |
| depth      | int64  | Default: 5. Max: 200 |

**Response**

```json
{
    "status":"ok",
    "ts":1590737035730,
    "data":{
        "symbol":"BTCUSD-PERP",
        "updated":1590737035653,
        "bids":[
            [9530,15432],
            [9525,12640],
            [9520,73561],
            [9515,68109],
            [9510,19895]
        ],
        "asks":[
            [9535,63584],
            [9540,51424],
            [9545,79901],
            [9550,56939],
            [9555,161822]
        ]
    }
}
```

------

#### Public - Markets

**HTTP Request**

`GET /api/v1/public/markets`

**Response**

```json
{
    "status":"ok",
    "ts":1590993332256,
    "data":[
        {
            "symbol":"BTCUSD-PERP",
            "openTime":1590906900000,
            "closeTime":1590993300000,
            "openPx": 9450,
            "highPx24h":9640,
            "lowPx24h":9390,
            "pxChange24h": -3.35,
            "volume24h":682494894,
            "volume24hUsd":2852425063.05,
            "fundingTime":1590998400000,
            "fundingRate":0.0003,
            "bestBidPx":9555,
            "bestBidQty":16424,
            "bestAskPx":9560,
            "bestAskQty":31076,
            "lastTradePx":9555,
            "lastTradeQty":4936,
            "lastTradeTs":1590993332183,
            "contractValue":194.9,
            "dgtxUsdRate":0.03728994
        }
    ]
}
```

------

`volume24hUsd` is calculated as: `volume24h` * `contractValue` * `dgtxUsdRate`.

`contractValue` is calculated as: `lastTradePx` / `TICK_SIZE` * `TICK_PRICE`, where `TICK_SIZE`=5 and `TICK_PRICE`=0.1 for BTCUSD-PERP contract.

#### Public - Trades

**HTTP Request**

`GET /api/v1/public/trades`

| Parameter | Type   | Description             |
| --------- | ------ | ----------------------- |
| symbol    | String | e.g. 'BTCUSD-PERP'      |
| count     | int64  | Default: 100. Max: 200. |

**Response**

```json
{
    "status":"ok",
    "ts":1590737141606,
    "data":{
        "symbol":"BTCUSD-PERP",
        "trades":[
            {"ts":1593783145314,"px":9110,"qty":276,"side":"SELL"},
            {"ts":1593783145314,"px":9110,"qty":1,"side":"SELL"},
            {"ts":1593783145317,"px":9110,"qty":157,"side":"SELL"},
            {"ts":1593783145319,"px":9110,"qty":1,"side":"SELL"},
            {"ts":1593783145323,"px":9110,"qty":24,"side":"SELL"}
        ]
    }
}
```

------

#### Public - Klines

**HTTP Request**

`GET /api/v1/public/klines`

| Parameter | Type   | Description                                                  |
| --------- | ------ | ------------------------------------------------------------ |
| symbol    | String | Contract symbol or index symbol, e.g. 'BTCUSD-PERP', '.DGTXBTCUSD' |
| interval  | String | Default: `1min`. Possible values: `1min`, `3min`, `5min`, `15min`, `30min`, `1h`, `3h`, `6h`, `12h`, `1D`, `3D`, `1W`, `3W`, `1M`, `3M`, `6M`, `1Y` |
| from      | int64  | Default: 0.                                                  |
| to        | int64  | Default: 0.                                                  |
| count     | int64  | Default: 60. Max: 1500                                       |

**Response**

```json
{
    "status":"ok",
    "ts":1590737272724,
    "data":{
        "symbol":"BTCUSD-PERP",
        "interval": "1min",
        "klines":[
            {
                "id":1590736620,
                "o":9535,
                "h":9545,
                "l":9530,
                "c":9540,
                "v":382175
            },
            {
                "id":1590736680,
                "o":9540,
                "h":9545,
                "l":9525,
                "c":9530,
                "v":474006
            }
        ]
    }
}
```

------

#### Public - Index

**HTTP Request**

`GET /api/v1/public/index`

| Parameter | Type   | Description                        |
| --------- | ------ | ---------------------------------- |
| symbol    | String | e.g. '.DGTXBTCUSD'; ***optional*** |

**Response**

```json
{
    "status":"ok",
    "ts":1590999736854,
    "data":{
        ".DGTXBTCUSD":{
            "indexSymbol":".DGTXBTCUSD",
            "contracts":["BTCUSD-PERP"],
            "updated":1590999736783,
            "markPx":9549.4469,
            "fairPx":9549.4469,
            "spotPx":0,
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
}
```

------

#### Public - Liquidations

**HTTP Request**

`GET /api/v1/public/liquidations`

| Parameter | Type   | Description               |
| --------- | ------ | ------------------------- |
| symbol    | String | e.g. 'BTCUSD-PERP'        |
| count     | int64  | Default: 100. Max: 10000. |

**Response**

```json
{
    "status":"ok",
    "ts":1593780179450,
    "data":{
        "symbol":"BTCUSD-PERP",
        "positions":[
            {
                "ts":1593780350000,
                "qty":100,
                "px":9100,
                "type":LONG
            }
        ]
    }
}
```

------

#### Error codes

| Code | Description                            |
| ---- | -------------------------------------- |
| 3001 | Bad Request (invalid parameters, etc.) |
| 3003 | Contract not found                     |
| 3004 | Index not found                        |
| 3006 | Kline interval not found               |
| 3011 | Feature is not implemented yet         |
| 4001 | System maintenance                     |

