from cryptocoins.cold_wallet_stats.base_stats_handler import BaseStatsHandler
from cryptocoins.coins.klc.manager import klc_manager
from cryptocoins.coins.klc.consts import KLC
from core.currency import Currency
from cryptocoins.utils.commons import get_amount_from_base_denomination


class UsdtKlcStatsHandler(BaseStatsHandler):
    CURRENCY = Currency.get('USDT')
    BLOCKCHAIN_CURRENCY = KLC

    def get_current_balance(self):
        token = klc_manager.get_token_by_symbol(self.CURRENCY)
        return get_amount_from_base_denomination(
            token.get_balance(klc_manager.get_keeper_wallet()),
            self.CURRENCY
        ) 