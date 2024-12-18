import logging
from django.conf import settings
from django.core.cache import cache
from environ import env

from cryptocoins.coins.klc.connection import get_w3_klc_connection
from cryptocoins.coins.klc.manager import klc_manager
from cryptocoins.interfaces.web3_commons import Web3CommonHandler
from cryptocoins.utils.register import register_evm_handler

log = logging.getLogger(__name__)
w3 = get_w3_klc_connection()


@register_evm_handler
class KLCHandler(Web3CommonHandler):
    CURRENCY = klc_manager.CURRENCY
    COIN_MANAGER = klc_manager
    TOKEN_CURRENCIES = klc_manager.registered_token_currencies
    TOKEN_CONTRACT_ADDRESSES = klc_manager.registered_token_addresses
    TRANSACTION_CLASS = klc_manager.TRANSACTION_CLASS
    IS_ENABLED = env('COMMON_TASKS_KLC', default=True)

    if IS_ENABLED:
        SAFE_ADDR = w3.to_checksum_address(settings.KLC_SAFE_ADDR)

    CHAIN_ID = settings.KLC_CHAIN_ID
    BLOCK_GENERATION_TIME = settings.KLC_BLOCK_GENERATION_TIME
    ACCUMULATION_PERIOD = settings.KLC_ACCUMULATION_PERIOD
    W3_CLIENT = w3
    DEFAULT_BLOCK_ID_DELTA = 100 