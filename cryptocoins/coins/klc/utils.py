from decimal import Decimal

from web3 import Web3

from cryptocoins.coins.klc.consts import KLC, KLC_CURRENCY_DECIMALS
from cryptocoins.utils.commons import Web3Token, Web3Transaction


class KLCTransaction(Web3Transaction):
    CURRENCY = KLC
    CURRENCY_DECIMALS = KLC_CURRENCY_DECIMALS

    def get_fee(self) -> Decimal:
        """
        Calculate transaction fee
        """
        return self.gas_price * self.gas_limit


class KLCToken(Web3Token):
    CURRENCY = KLC
    BLOCKCHAIN_CURRENCY = KLC
    DECIMALS = KLC_CURRENCY_DECIMALS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.w3 = Web3()

    def get_decimals(self) -> int:
        """
        Get token decimals from smart contract
        """
        return self.DECIMALS

    def get_symbol(self) -> str:
        """
        Get token symbol from smart contract
        """
        return self.CURRENCY 