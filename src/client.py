import time, hmac, hashlib
from urllib.parse import urlencode
import requests, logging

logger = logging.getLogger("BinanceBot.client")
TESTNET_BASE = "https://demo.binance.com"


class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str, base_url: str = TESTNET_BASE, session=None):
        if not api_key or not api_secret:
            raise ValueError("API key and secret must be provided.")
        self.api_key = api_key
        self.api_secret = api_secret.encode("utf-8")
        self.base = base_url.rstrip("/")
        self.session = session or requests.Session()
        self.session.headers.update({"X-MBX-APIKEY": self.api_key})

    def _get_ts(self):
        return int(time.time() * 1000)

    def _sign(self, params: dict):
        query = urlencode(params, doseq=True)
        signature = hmac.new(self.api_secret, query.encode("utf-8"), hashlib.sha256).hexdigest()
        return signature

    def _request(self, method: str, path: str, params: dict = None, signed: bool = False):
        url = self.base + path
        params = params or {}

        if signed:
            params["timestamp"] = self._get_ts()
            params["signature"] = self._sign(params)

        logger.debug(f"REQUEST -> {method.upper()} {url} {params}")

        try:
            if method.lower() == "get":
                resp = self.session.get(url, params=params, timeout=10)
            elif method.lower() == "post":
                resp = self.session.post(url, params=params, timeout=10)
            elif method.lower() == "delete":
                resp = self.session.delete(url, params=params, timeout=10)
            else:
                raise ValueError("Unsupported HTTP method")
        except Exception as e:
            logger.exception(f"Network error: {e}")
            raise

        logger.debug(f"RESPONSE <- {resp.status_code} {resp.text[:500]}")

        if not resp.ok:
            try:
                data = resp.json()
            except Exception:
                resp.raise_for_status()
            raise RuntimeError(f"API error: {data}")

        try:
            return resp.json()
        except:
            return resp.text

    def place_order(self, symbol: str, side: str, type_: str, quantity: float,
                    price: float = None, timeInForce: str = None, stopPrice: float = None, reduceOnly: bool = False):

        path = "/fapi/v1/order"
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": type_.upper(),
            "quantity": float(quantity)
        }

        if price is not None:
            params["price"] = str(price)

        if timeInForce:
            params["timeInForce"] = timeInForce

        if stopPrice is not None:
            params["stopPrice"] = str(stopPrice)

        params["reduceOnly"] = str(bool(reduceOnly)).lower()

        return self._request("post", path, params=params, signed=True)

