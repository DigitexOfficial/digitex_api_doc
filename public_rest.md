# DIGITEX Futures API Draft

## Market Data API

**Note**: This is *ALPHA-VERSION* of API. In future versions of API could be incompatible changes.

### Protocol

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

------

### Endpoints

*Testnet API URL*: https://rest.tapi.digitexfutures.com.

*Mainnet API URL*: https://rest.mapi.digitexfutures.com.

#### Public - Contracts

**HTTP Request**

`GET /api/v1/public/contracts`

**Response**

```json
{
    "status":"ok",
    "ts":1597073306274,
    "data":[
        {
            "id":1,
            "marketId":1,
            "name":"BTC/USD-PERP",
            "symbol":"BTCUSD-PERP",
            "type":"perpetual_futures",
            "isTradable":true,
            "baseCurrency":"BTC",
            "quoteCurrency":"USD",
            "pnlCurrency":"DGTX",
            "marginCurrency":"DGTX",
            "settleCurrency":"DGTX",
            "lotSize":1,
            "isQuanto":true,
            "isInverse":false,
            "underlyingAsset":"coin",
            "indexSymbol":".DGTXBTCUSD",
            "premiumIndexSymbol":"",
            "fundingRate":0.01,
            "fundingPeriod":28800,
            "indicativeFundingRate":0,
            "markType":"fair_price",
            "initMargin":1,
            "maintMargin":0.5,
            "deleverage":true,
            "isLeverage":true,
            "maxLeverage":25,
            "createTime":1588003200000,
            "listingTime":1588003200000,
            "expiryTime":0,
            "settleTime":0,
            "makerFee":0,
            "takerFee":0,
            "settlementFee":0,
            "insuranceFee":0,
            "minPrice":0,
            "maxPrice":0,
            "minOrderSize":0,
            "maxOrderSize":0,
            "tickSize":5,
            "tickValue":0.1
        },
        {
            "id":2,
            "marketId":2,
            "name":"ETH/USD-PERP",
            "symbol":"ETHUSD-PERP",
            "type":"perpetual_futures",
            "isTradable":true,
            "baseCurrency":"ETH",
            "quoteCurrency":"USD",
            "pnlCurrency":"DGTX",
            "marginCurrency":"DGTX",
            "settleCurrency":"DGTX",
            "lotSize":1,
            "isQuanto":true,
            "isInverse":false,
            "underlyingAsset":"coin",
            "indexSymbol":".DGTXETHUSD",
            "premiumIndexSymbol":"",
            "fundingRate":0.01,
            "fundingPeriod":28800,
            "indicativeFundingRate":0,
            "markType":"fair_price",
            "initMargin":1,
            "maintMargin":0.5,
            "deleverage":true,
            "isLeverage":true,
            "maxLeverage":25,
            "createTime":1588003200000,
            "listingTime":0,
            "expiryTime":0,
            "settleTime":0,
            "makerFee":0,
            "takerFee":0,
            "settlementFee":0,
            "insuranceFee":0,
            "minPrice":0,
            "maxPrice":0,
            "minOrderSize":0,
            "maxOrderSize":0,
            "tickSize":0.25,
            "tickValue":0.25,
            "priceIncrement":1
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
            "openInterest":431229,
            "openInterestUsd":4586283.33,
            "dgtxUsdRate":0.03728994,
            "insuranceFund":1711653380.28
        },
        {
            "symbol":"ETHUSD-PERP",
            "openTime":1599558120000,
            "closeTime":1599644520000,
            "openPx":342.75,
            "highPx24h":346.5,
            "lowPx24h":325.5,
            "pxChange24h":0.66,
            "volume24h":983328,
            "volume24hUsd":11797492.97,
            "fundingTime":1599667200000,
            "fundingRate":0.01,
            "bestBidPx":344.75,
            "bestBidQty":88,
            "bestAskPx":345,
            "bestAskQty":573,
            "lastTradePx":345,
            "lastTradeQty":186,
            "lastTradeTs":1599644494456,
            "contractValue":345,
            "openInterest":9465,
            "openInterestUsd":116110.45,
            "dgtxUsdRate":0.03555753,
            "insuranceFund":239178.5,
            "markPx":346.7181
        }
    ]
}
```

`openInterestUsd` is calculated as: `openInterest` * `contractValue` * `dgtxUsdRate`.

`contractValue` is calculated as: `lastTradePx` / `TICK_SIZE` * `TICK_VALUE`, where:

*  `TICK_SIZE`=5 and `TICK_VALUE`=0.1 for `BTCUSD-PERP` contract;
* `TICK_SIZE`=0.25 and `TICK_VALUE`=0.25 for `ETHUSD-PERP` contract.



------

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
| symbol    | String | Contract symbol or index symbol, e.g. 'BTCUSD-PERP'          |
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
            "spotPx":9549.4469,
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
                "type":"LONG"
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

