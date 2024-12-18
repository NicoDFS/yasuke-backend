from django.conf import settings
from environ import env

from core.currency import Currency
from cryptocoins.coins.klc.connection import get_w3_klc_connection
from cryptocoins.coins.klc.consts import KLC_CURRENCY, KLC_TOKENS
from cryptocoins.coins.klc.token import KLC20Token
from cryptocoins.coins.klc.transaction import KLCTransaction
from cryptocoins.evm.manager import Web3Manager
from cryptocoins.utils.gas_price import GasPriceCache

w3 = get_w3_klc_connection()


class KLCGasPriceCache(GasPriceCache):
    GAS_PRICE_UPDATE_PERIOD = 15
    GAS_PRICE_COEFFICIENT = 1.1
    MIN_GAS_PRICE = 1000000000  # 1 gwei
    MAX_GAS_PRICE = 100000000000  # 100 gwei

    def _get_price(self) -> int:
        return w3.eth.gas_price


class KLCManager(Web3Manager):
    GAS_CURRENCY = settings.KLC_TX_GAS
    CURRENCY: Currency = KLC_CURRENCY
    TOKEN_CURRENCIES = KLC_TOKENS
    TOKEN_CLASS = KLC20Token
    TRANSACTION_CLASS = KLCTransaction
    GAS_PRICE_CACHE_CLASS = KLCGasPriceCache
    CHAIN_ID = settings.KLC_CHAIN_ID
    MIN_BALANCE_TO_ACCUMULATE_DUST = env.decimal('KLC_MIN_BALANCE_TO_ACCUMULATE_DUST', default=0.01)
    DEFAULT_RECEIPT_WAIT_TIMEOUT = env.int('KLC_DEFAULT_RECEIPT_WAIT_TIMEOUT', default=5*60)
    COLD_WALLET_ADDRESS = settings.KLC_SAFE_ADDR


klc_manager: KLCManager = KLCManager(client=w3) 