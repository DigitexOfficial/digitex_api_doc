# DIGITEX Futures API Draft

## Market Data API

Every json-response has common fields:

```json
{
    "success": true, // or false in case of error
    "err_code": 777, // in case of success==false
    "err_msg": "Error description"
}
```

Currently we Digitex Exchange has `market_id` which is not linked to any unique string identifier like `BTC/DGTX-PERP`.

### Endpoints

------

#### Public - Status

**HTTP Request**

`GET /api/futures/v1/platform/status`

**Response**

| Parameter | Type   | Description                |
| --------- | ------ | -------------------------- |
| status    | String | online/offline/maintenance |

------

#### Public - Time

**HTTP Request**

`GET /api/futures/v1/platform/time`

**Response**

| Parameters | Type   | Description               |
| ---------- | ------ | ------------------------- |
| iso        | String | "2020-05-15T14:03:29.038" |
| ts         | int64  | timestamp                 |

------

#### Public - Orderbook

**HTTP Request**

`GET /api/futures/v1/orderbook`

| Parameters | Type   | Description          |
| ---------- | ------ | -------------------- |
| symbol     | String | e.g. 'BTC/DGTX-PERP' |
| depth      | int64  | Default: 5.          |

**Response**

| Parameters | Type                                                     | Description                         |
| ---------- | -------------------------------------------------------- | ----------------------------------- |
| ts         | int64                                                    | timestamp                           |
| bids       | [ [String, String], [String, String], [String, String] ] | [ [px, qty], [px, qty], [px, qty] ] |
| asks       | [ [String, String], [String, String], [String, String] ] | [ [px, qty], [px, qty], [px, qty] ] |

------

#### Public - Ticker

**HTTP Request**

`GET /api/futures/v1/ticker`

| Parameters | Type   | Description          |
| ---------- | ------ | -------------------- |
| symbol     | String | e.g. 'BTC/DGTX-PERP' |

**Response**

| Parameters     | Type   | Description          |
| -------------- | ------ | -------------------- |
| symbol         | String | e.g. 'BTC/DGTX-PERP' |
| open_time      | int64  | timestamp            |
| close_time     | int64  | timestamp            |
| high_px_24h    | String |                      |
| low_px_24h     | String |                      |
| volume_24h     | String |                      |
| last_trade_px  | String |                      |
| last_trade_qty | String |                      |
| funding_time   | int64  | timestamp            |
| funding_rate   | String |                      |
| best_bid_px    | String |                      |
| best_bid_size  | String |                      |
| best_ask_px    | String |                      |
| best_ask_size  | String |                      |
| mark_price     | String |                      |

------

#### Public - Last Trade

**HTTP Request**

`GET /api/futures/v1/trade/last`

| Parameter | Type   | Description          |
| --------- | ------ | -------------------- |
| symbol    | String | e.g. 'BTC/DGTX-PERP' |

**Response**

| Parameter | Type    | Description  |
| --------- | ------- | ------------ |
| ts        | int64   |              |
| side      | Strings | "buy"/"sell" |
| px        | String  |              |
| qty       | String  |              |

------

#### Public - Trade History

**HTTP Request**

`GET /api/futures/v1/trade/history`

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| symbol    | String | e.g. 'BTC/DGTX-PERP'   |
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

| Parameter | Type   | Description          |
| --------- | ------ | -------------------- |
| symbol    | String | e.g. 'BTC/DGTX-PERP' |

**Response**

| Parameter | Type   | Description |
| --------- | ------ | ----------- |
| ts        | int64  | timestamp   |
| px        | String | index price |

------

