from cryptocoins.coins.klc.consts import KLC_CURRENCY
from cryptocoins.evm.transaction import Web3Transaction


class KLCTransaction(Web3Transaction):
    CURRENCY = KLC_CURRENCY 