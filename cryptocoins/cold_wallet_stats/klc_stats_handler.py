from cryptocoins.cold_wallet_stats.base_stats_handler import BaseStatsHandler
from cryptocoins.coins.klc.klc import klc_manager
from cryptocoins.coins.klc.consts import KLC
from cryptocoins.utils.commons import get_amount_from_base_denomination


class KlcStatsHandler(BaseStatsHandler):
    CURRENCY = KLC
    BLOCKCHAIN_CURRENCY = KLC

    def get_current_balance(self):
        return get_amount_from_base_denomination(
            klc_manager.get_wallet_balance(klc_manager.get_keeper_wallet()),
            self.CURRENCY
        ) 