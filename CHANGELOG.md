# CHANGELOG

###### 28.08.2020

* API v1.0.3 released.

------

###### 26.08.2020

- WS Trading API: rate limiter improved.
- WS Trading API: fix issued with `side` of `marketTrades` .
- WS Public API: introduce channel `<CONTRACT>@orderbook_1`. 
- WS Public API: don't send cached messages from already subscribed channels after `subscribe`.
- WS Public API: subscription more than one time for the same channel doesn't produce an error.
- WS Public API: unsubscription from the channel without subscription for this channel doesn't produce an error.

------

###### 19.08.2020

- API v1.0.2 released.

------

###### 18.08.2020

- update examples of trading messages in the documentation.

------

###### 14.08.2020

- version 1.0.1 released.

------

###### 10.08.2020

- add `tickSize` and `tickValue` to `/public/contracts` response.

------

###### 31.07.2020

- public API: add `markPx` to `/public/markets` response.

------

###### 28.07.2020

- WS API: add trade request limiter (error `RequestRateLimitExceeded`).

------

###### 26.07.2020

- make `auth` pseudo-synchronous.
- add `AuthInProgress` error response.

------

###### 24.07.2020

- public WS API: rename channel `funding` to `fundingInfo`.
- change the way `volume24hUsd` is calculated.
- change the way `fundingRate` is calculated.

------

###### 22.07.2020

- Introduce simple version detection. To obtain version information make request to `/public/version` endpoint.

- Add `XRPUSD-PERP` contract.

------

###### 21.07.2020

Add field `errCode` to API responses such as:

- `orderStatus`
- `orderCancelled`
- `contractClosed`
- `leverage`
- `condOrderStatus`

------

