from django.conf import settings

# Currency code and ID
KLC = 28  # Next available ID after MATIC (27)
CODE = 'KLC'
DECIMALS = 18

# Network configuration
KLC_CHAIN_ID = 3888
KLC_CURRENCY_DECIMALS = 18
KLC_TX_GAS_LIMIT = 21000
KLC_TOKEN_TRANSFER_GAS_LIMIT = 65000  # Higher gas limit for token transfers
KLC_SAFE_ADDR = settings.KLC_SAFE_ADDR
KLC_BLOCK_TIME = 2  # Block time in seconds
KLC_REQUIRED_CONFIRMATIONS = 12  # Number of confirmations required for deposit

# Block explorer URLs
KLC_EXPLORER_ADDR = 'https://kalyscan.io'
KLC_EXPLORER_TX_URL = f'{KLC_EXPLORER_ADDR}/tx/'
KLC_EXPLORER_ADDRESS_URL = f'{KLC_EXPLORER_ADDR}/address/'
KLC_EXPLORER_TOKEN_URL = f'{KLC_EXPLORER_ADDR}/token/'

# RPC settings
KLC_CURRENCY = {
    'id': KLC,
    'name': 'KalyCoin',
    'symbol': CODE,
    'blockchain_currency': CODE,
    'withdrawal_fee': '0.001',
    'blockchain': CODE,
    'decimals': KLC_CURRENCY_DECIMALS,
    'explorer_url': KLC_EXPLORER_ADDR,
    'required_confirmations': KLC_REQUIRED_CONFIRMATIONS,
}

# Token lists for KLC20 tokens
KLC20_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# KLC20 Token Configuration
KLC_TOKENS = {
    'USDT': {
        'name': 'Tether USD',
        'symbol': 'USDT',
        'address': '0x2CA775C77B922A51FcF3097F52bFFdbc0250D99A',
        'decimals': 6,
        'blockchain_currency': CODE,
        'withdrawal_fee': '1',
        'required_confirmations': KLC_REQUIRED_CONFIRMATIONS,
    },
    'USDC': {
        'name': 'USD Coin',
        'symbol': 'USDC',
        'address': '0x9cAb0c396cF0F4325913f2269a0b72BD4d46E3A9',
        'decimals': 6,
        'blockchain_currency': CODE,
        'withdrawal_fee': '1',
        'required_confirmations': KLC_REQUIRED_CONFIRMATIONS,
    },
    'DAI': {
        'name': 'Dai Stablecoin',
        'symbol': 'DAI',
        'address': '0x6E92CAC380F7A7B86f4163fad0df2F277B16Edc6',
        'decimals': 18,
        'blockchain_currency': CODE,
        'withdrawal_fee': '1',
        'required_confirmations': KLC_REQUIRED_CONFIRMATIONS,
    },
}

# Common token settings
for token_symbol, token_data in KLC_TOKENS.items():
    token_data.update({
        'id': token_symbol,
        'blockchain': CODE,
        'explorer_url': KLC_EXPLORER_ADDR,
        'token_explorer_url': f"{KLC_EXPLORER_TOKEN_URL}{token_data['address']}",
        'abi': KLC20_ABI,
    }) 