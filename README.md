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
  "status": "ok",
  "ts":1590402678700,
  "data": [
    {
      "id": 1,
      "symbol": "DGTX",
      "precision": 4,
    },
    {
      "id": 2,
      "symbol": "BTC",
      "precision": 8,
    },
    {
      "id": 3,
      "symbol": "USD",
      "precision": 2,
    },
    {
      "id": 4,
      "symbol": "ETH",
      "precision": 8,
    },
    {
      "id": 5,
      "symbol": "XRP",
      "precision": 8,
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
      "date": "2020-05-21T08:08:49.464Z"
    },
    {
      "id": 2,
      "link": "string",
      "title": "string",
      "content": "string",
      "date": "2020-05-21T08:08:49.464Z"
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

| Parameter | Type   | Description  |
| --------- | ------ | ------------ |
| ts        | int64  |              |
| side      | String | "buy"/"sell" |
| px        | String |              |
| qty       | String |              |

------

#### Public - Trade History

**HTTP Request**

`GET /api/futures/v1/trade/history`

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| symbol    | String | e.g. 'BTCUSD-PERP'     |
| size      | int64  | Default: 50. Max: 200. |

**Response**

| Parameter | Type                 | Description                       |
| --------- | -------------------- | --------------------------------- |
| trades    | [ {trade}, {trade} ] | trade - see `Last Trade` endpoint |

------

#### Public - Klines

**HTTP Request**

`GET /api/futures/v1/klines`

| Parameter  | Type         | Description                    |
| ---------- | ------------ | ------------------------------ |
| resolution | String/int64 | 60s, 1m, etc. / 60, 3600, etc. |
| start_time | int64        | timestamp                      |
| end_time   | int64        | timestamp                      |

**Response**

| Parameter | Type   | Description |
| --------- | ------ | ----------- |
| ts        | int64  | timestamp   |
| open      | String |             |
| high      | String |             |
| low       | String |             |
| close     | String |             |
| volume    | String |             |

------

#### Public - Index

**HTTP Request**

`GET /api/futures/v1/index`

| Parameter | Type   | Description        |
| --------- | ------ | ------------------ |
| symbol    | String | e.g. 'BTCUSD-PERP' |

**Response**

| Parameter | Type   | Description |
| --------- | ------ | ----------- |
| ts        | int64  | timestamp   |
| px        | String | index price |

------

