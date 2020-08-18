# CHANGELOG

###### 21.07.2020

Add field `errCode` to API responses such as:

- `orderStatus`
- `orderCancelled`
- `contractClosed`
- `leverage`
- `condOrderStatus`

------

###### 22.07.2020

- Introduce simple version detection.

To obtain version information make request to `/public/version` endpoint.

- Add `XRPUSD-PERP` contract.

------

###### 24.07.2020

- public WS API: rename channel `funding` to `fundingInfo`.
- change the way `volume24hUsd` is calculated.
- change the way `fundingRate` is calculated.

------

###### 26.07.2020

- make `auth` pseudo-synchronous.
- add `AuthInProgress` error response.

###### 28.07.2020

- WS API: add trade request limiter (error `RequestRateLimitExceeded`).

###### 31.07.2020

- public API: add `markPx` to `/public/markets` response.

###### 10.08.2020

- add `tickSize` and `tickValue` to `/public/contracts` response.

###### 14.08.2020

- version 1.0.1 released.

###### 18.08.2020

- update examples of trading messages in the documentation.