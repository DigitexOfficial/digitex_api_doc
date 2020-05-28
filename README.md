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
  "ts":1590402678700,
  "data": {
    "symbol":"BTCUSD-PERP",
    "bids":[
      ["9220.0000","29644"],
      ["9215.0000","68492"],
      ["9210.0000","10"],
      ["9205.0000","1000"],
      ["9200.0000","10"]
    ],
    "asks":[
      ["9225.0000","45786"],
      ["9230.0000","3061"],
      ["9235.0000","500"],
      ["9240.0000","7544"],
      ["9245.0000","77379"]
    ]
  }
}
```

------

#### Public - Stats

**HTTP Request**

`GET /api/v1/stats`

| Parameters | Type   | Description        |
| ---------- | ------ | ------------------ |
| symbol     | String | e.g. 'BTCUSD-PERP' |

**Response**

```json
{
   "status":"ok",
   "ts":1590413564472,
   "data":{
      "symbol":"BTCUSD-PERP",
      "openTime":1590327120000,
      "closeTime":1590413520000,
      "highPx24h":"9150.0000",
      "lowPx24h":"8645.0000",
      "volume24h":"714064643",
      "fundingTime":1590422400000,
      "fundingRate":"0.00030000",
      "bestBidPx":"8750.0000",
      "bestBidQty":"70723",
      "bestAskPx":"8755.0000",
      "bestAskQty":"32428",
      "lastTradePx":"8755.0000",
      "lastTradeQty":"11286"
   }
}
```

------

#### Public - Last Trade

**HTTP Request**

`GET /api/v1/trade/last`

| Parameter | Type   | Description        |
| --------- | ------ | ------------------ |
| symbol    | String | e.g. 'BTCUSD-PERP' |

**Response**

```json
{
   "status":"ok",
   "ts":1590481932218,
   "data": {
      "symbol":"BTCUSD-PERP",
      "px":"8975.0000",
      "qty":"8208"
   }
}
```



------

#### Public - Trade History

**HTTP Request**

`GET /api/v1/history/trade`

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| symbol    | String | e.g. 'BTCUSD-PERP'     |
| size      | int64  | Default: 50. Max: 200. |

**Response**

```json
{
    "status":"ok",
    "ts":1590497248414,
    "data":{
        "symbol":"BTCUSD-PERP",
        "trades":[
            ["8815.0000","32"],
            ["8815.0000","4"],
            ["8815.0000","301"],
            ["8815.0000","85"],
            ["8815.0000","1"]
        ]
    }
}
```

------

#### Public - Kline History

**HTTP Request**

`GET /api/v1/history/kline`

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| symbol    | String | e.g. 'BTCUSD-PERP'     |
| size      | int64  | Default: 60. Max: 1440 |

**Response**

```json
{
    "status":"ok",
    "ts":1590494157693,
    "data":{
        "symbol":"BTCUSD-PERP",
        "klines":[
            {
                "id":1590493920,
                "o":"8880.0000",
                "h":"8885.0000",
                "l":"8875.0000",
                "c":"8880.0000",
                "v":"463705"
            },
            {
                "id":1590493980,
                "o":"8880.0000",
                "h":"8885.0000",
                "l":"8875.0000",
                "c":"8880.0000",
                "v":"347447"
            }
        ]
    }
}
```

------

#### Public - Mark Price

**HTTP Request**

`GET /api/v1/mark_price`

| Parameter | Type   | Description        |
| --------- | ------ | ------------------ |
| symbol    | String | e.g. 'BTCUSD-PERP' |

**Response**

```json
{
    "status":"ok",
    "ts":1590497191142,
    "data":{
        "symbol":"BTCUSD-PERP",
        "px":"8816.2804"
    }
}
```

------

