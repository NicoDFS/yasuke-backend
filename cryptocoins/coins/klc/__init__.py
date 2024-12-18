from core.currency import CoinParams
from cryptocoins.coins.klc.connection import get_w3_klc_connection
from cryptocoins.coins.klc.consts import KLC, KLC_CURRENCY
from cryptocoins.coins.klc.wallet import (
    get_or_create_klc_wallet,
    get_or_create_klc20_wallet,
    is_valid_klc_address,
    klc_wallet_creation_wrapper,
    klc20_wallet_creation_wrapper,
)
from cryptocoins.utils.register import register_coin

w3 = get_w3_klc_connection()

KLC_CURRENCY = register_coin(
    currency_id=KLC,
    currency_code='KLC',
    address_validation_fn=is_valid_klc_address,
    wallet_creation_fn=klc_wallet_creation_wrapper,
    latest_block_fn=lambda currency: w3.eth.get_block_number(),
    blocks_diff_alert=100,
)

__all__ = [
    'KLC',
    'KLC_CURRENCY',
    'get_or_create_klc_wallet',
    'get_or_create_klc20_wallet',
    'is_valid_klc_address',
    'klc_wallet_creation_wrapper',
    'klc20_wallet_creation_wrapper',
] 