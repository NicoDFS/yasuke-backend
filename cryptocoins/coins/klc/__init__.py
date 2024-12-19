from core.currency import CoinParams
from cryptocoins.coins.klc.connection import get_w3_kaly_connection
from cryptocoins.coins.klc.consts import KLC, CODE
from cryptocoins.coins.klc.wallet import klc_wallet_creation_wrapper, is_valid_klc_address
from cryptocoins.utils.register import register_coin

w3 = get_w3_kaly_connection()

KLC_CURRENCY = register_coin(
    currency_id=KLC,
    currency_code=CODE,
    address_validation_fn=is_valid_klc_address,
    wallet_creation_fn=klc_wallet_creation_wrapper,
    latest_block_fn=lambda currency: w3.eth.get_block_number(),
    blocks_diff_alert=100,
)