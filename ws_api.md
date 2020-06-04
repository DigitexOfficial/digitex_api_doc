### Public Websocket API Draft

#### General information

Server send message `ping` every 30 seconds. Client should respond with message `pong` or it would be disconnected. 

The `id` used in JSON as an identifier of the request. The response for the particular request has the same `id` value.

#### Subscribe to a stream

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

#### Unsubscribe from stream

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

- orderbook_5, orderbook_10, orderbook_25, orderbook_50, orderbook_100, orderbook_200
- trades
- kline_1min

#### Orderbook stream

**Stream name:** `<symbol>@orderbook_5`

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

#### Trade stream

**Stream name:** `<symbol>@trades`

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

#### Kline stream

**Stream name:** `<symbol>@kline_1min`

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

