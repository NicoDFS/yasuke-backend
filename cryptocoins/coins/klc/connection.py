from web3 import Web3
from django.conf import settings


def get_w3_klc_connection():
    """
    Get Web3 connection for KalyChain
    """
    return Web3(Web3.HTTPProvider(settings.KLC_RPC_URL)) 