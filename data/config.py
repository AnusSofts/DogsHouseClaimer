# api id, hash
API_ID = 28124383
API_HASH = '6cf394155b051bcd4d329996dabd5c44'

REF_LINK = 'https://t.me/dogshouse_bot/join?startapp=nd9o9bkYTIulNajLpeh3Nw'

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
}

PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "socks5",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "socks5"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}

# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30

SOFT_INFO = f"""{"Dogs 🦴".center(40)}
Soft for https://t.me/dogshouse_bot; claim reward

The soft also collects statistics on accounts and uses proxies from {f"the {PROXY['PROXY_PATH']} file" if PROXY['USE_PROXY_FROM_FILE'] else "the accounts.json file"}
"""
