import logging
from typing import Optional

from django.conf import settings
from web3 import Web3

from cryptocoins.coins.klc.consts import (
    KLC,
    KLC_CHAIN_ID,
    KLC_TX_GAS_LIMIT,
)
from cryptocoins.coins.klc.utils import KLCTransaction
from cryptocoins.utils.commons import Web3CommonHandler

log = logging.getLogger(__name__)


class KLCCoinService(Web3CommonHandler):
    CURRENCY = KLC
    CHAIN_ID = KLC_CHAIN_ID
    GAS_LIMIT = KLC_TX_GAS_LIMIT
    SAFE_ADDR = settings.KLC_SAFE_ADDR
    RPC_URL = settings.KLC_RPC_URL
    TRANSACTION_CLASS = KLCTransaction

    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(self.RPC_URL))

    def get_latest_block_num(self) -> int:
        """
        Get latest block number
        """
        return self.web3.eth.block_number

    def get_block(self, block_id: int) -> dict:
        """
        Get block by id
        """
        return self.web3.eth.get_block(block_id, full_transactions=True)

    def get_transaction(self, tx_hash: str) -> Optional[dict]:
        """
        Get transaction by hash
        """
        try:
            return self.web3.eth.get_transaction(tx_hash)
        except Exception as e:
            log.exception(f'Error getting transaction {tx_hash}: {e}')
            return None

    def get_transaction_receipt(self, tx_hash: str) -> Optional[dict]:
        """
        Get transaction receipt by hash
        """
        try:
            return self.web3.eth.get_transaction_receipt(tx_hash)
        except Exception as e:
            log.exception(f'Error getting transaction receipt {tx_hash}: {e}')
            return None

    def get_balance(self, address: str) -> int:
        """
        Get balance for address
        """
        try:
            return self.web3.eth.get_balance(Web3.to_checksum_address(address))
        except Exception as e:
            log.exception(f'Error getting balance for {address}: {e}')
            return 0

    def get_gas_price(self) -> int:
        """
        Get current gas price
        """
        return self.web3.eth.gas_price 