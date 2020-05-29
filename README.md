# DIGITEX Futures API Draft

## Market Data API

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

### Endpoints

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
            "tradable":true,
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
      },
      {
         "id":1,
         "name":"Digitex Token",
         "symbol":"DGTX",
         "type":"token",
         "precision":4,
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

`GET /api/v1/ping`

**Response**

```json
{}
```

------

#### Public - Announcement

**HTTP Request**

`GET /api/v1/announcement`

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

`GET /api/v1/time`

**Response**

| Parameters | Type   | Description               |
| ---------- | ------ | ------------------------- |
| iso        | String | "2020-05-15T14:03:29.038" |
| ts         | int64  | timestamp                 |

------

#### Public - Orderbook

**HTTP Request**

`GET /api/v1/orderbook`

| Parameters | Type   | Description        |
| ---------- | ------ | ------------------ |
| symbol     | String | e.g. 'BTCUSD-PERP' |
| depth      | int64  | Default: 5.        |

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

#### Public - Stats

**HTTP Request**

`GET /api/v1/stats`

**Response**

```json
{
    "status":"ok",
    "ts":1590736884842,
    "data":[
        {
            "symbol":"BTCUSD-PERP",
            "openTime":1590650460000,
            "closeTime":1677050460000,
            "highPx24h":9625,
            "lowPx24h":9110,
            "volume24h":694250105,
            "fundingTime":1590739200000000,
            "fundingRate":0.0003,
            "bestBidPx":9530,
            "bestBidQty":14007,
            "bestAskPx":9535,
            "bestAskQty":57248,
            "lastTradePx":9535,
            "lastTradeQty":38645,
            "lastTradeTs":1590736884753
        }
    ]
}
```

------

#### Public - Last Trade

**HTTP Request**

`GET /api/v1/trades/last`

| Parameter | Type   | Description        |
| --------- | ------ | ------------------ |
| symbol    | String | e.g. 'BTCUSD-PERP' |

**Response**

```json
{
    "status":"ok",
    "ts":1590736996540,
    "data":{
        "symbol":"BTCUSD-PERP",
        "px":9535,
        "qty":5261,
        "ts":1590736996453
    }
}
```



------

#### Public - Trade History

**HTTP Request**

`GET /api/v1/trades`

| Parameter | Type   | Description           |
| --------- | ------ | --------------------- |
| symbol    | String | e.g. 'BTCUSD-PERP'    |
| size      | int64  | Default: 5. Max: 200. |

**Response**

```json
{
    "status":"ok",
    "ts":1590737141606,
    "data":{
        "symbol":"BTCUSD-PERP",
        "trades":[
            {
                "px":9530,
                "qty":26,
                "ts":1590737104653
            },
            {
                "px":9530,
                "qty":2,
                "ts":1590737104653
            },
            {
                "px":9530,
                "qty":1,
                "ts":1590737104653
            },
            {
                "px":9530,
                "qty":2,
                "ts":1590737104653
            },
            {
                "px":9530,
                "qty":48,
                "ts":1590737104653
            }
        ]
    }
}
```

------

#### Public - Kline History

**HTTP Request**

`GET /api/v1/klines`

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| symbol    | String | e.g. 'BTCUSD-PERP'     |
| size      | int64  | Default: 60. Max: 1440 |

**Response**

```json
{
    "status":"ok",
    "ts":1590737272724,
    "data":{
        "symbol":"BTCUSD-PERP",
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

`GET /api/v1/index`

| Parameter | Type   | Description                        |
| --------- | ------ | ---------------------------------- |
| symbol    | String | e.g. 'BTCUSD-PERP'; ***optional*** |

**Response**

```json
{
    "status":"ok",
    "ts":1590751652363,
    "data":{
        "BTCUSD-PERP":{
            "updated":0,
            "markPx":9388.7828,
            "fairPx":0,
            "spotPx":0,
            "components":{
                "binance":{
                    "weight":0,"ts":0,"px":0,"vol":0
                },
                "bitfinex":{
                    "weight":0,"ts":0,"px":0,"vol":0
                },
                "coinbasepro":{
                    "weight":0,"ts":0,"px":0,"vol":0
                },
                "kraken":{
                    "weight":0,"ts":0,"px":0,"vol":0
                }
            }
        }
    }
}
```

------

