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

- orderbook_25
- trades
- kline_1min

#### Orderbook stream

**Stream name:** `<symbol>@orderbook_25`

Message

```json
{
    "e": "orderbook_25",
    "s": "BTCUSD-PERP",
    "u": 12457823654,
    "b": [
        [9250, 100],
        [9245, 350]
    ],
    "a": [
        [9255, 50],
        [9260, 150]
    ]
}
```

#### Trade stream

**Stream name:** `<symbol>@trades`

Message

```json
{
    "e": "trades",
    "s": "BTCUSD-PERP",
    "t": [
        {
            "px": 9412,
            "qty": 500,
            "ts": 2245712569
        },
        {
            "px": 9315,
            "qty": 200,
            "ts": 22457145698
        },
        {
            "px": 9245,
            "qty": 750,
            "ts": 1246587413
        }
    ]   
}
```

#### Kline stream

**Stream name:** `<symbol>@kline_1min`

```json
{
    "e": "kline",
    "i": "1min",
    "s": "BTCUSD-PERP",
    "id": 1591274820,
    "o": 9325,
    "h": 9540,
    "l": 9250,
    "c": 9420,
    "v": 10000
}
```

