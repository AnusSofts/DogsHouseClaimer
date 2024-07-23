from utils.dogs import DogsHouse
from utils.core import logger
import datetime
import pandas as pd
from utils.core.telegram import Accounts
import asyncio
import os


async def start(thread: int, session_name: str, phone_number: str, proxy: [str, None]):
    dogs = DogsHouse(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)
    account = session_name + '.session'
    try:
        balance, age, last_seen_str = await dogs.login()
        logger.success(f'Thread {thread} | {account} | Account age: {age}; Balance: {balance}')

        if '.' in last_seen_str:
            last_seen_str = last_seen_str[:last_seen_str.index('.') + 7]
        last_seen = datetime.datetime.fromisoformat(last_seen_str.replace('Z', '+00:00'))

        now = datetime.datetime.utcnow()

        next_day = last_seen + datetime.timedelta(days=1)
        time_to_wait = (next_day - now).total_seconds()

        if time_to_wait > 0:
            logger.info(
                f'Thread {thread} | {account} | Waiting for {time_to_wait} seconds before claiming daily rewards')
            await asyncio.sleep(time_to_wait)

        daily, total = await dogs.get_daily()
        logger.success(f'Thread {thread} | {account} | Daily claim: {daily}; Total: {total}')
        await dogs.logout()
    except Exception as e:
        logger.error(f'Thread {thread} | {account} | Error: {e}')


async def stats():
    accounts = await Accounts().get_accounts()

    tasks = []
    for thread, account in enumerate(accounts):
        session_name, phone_number, proxy = account.values()
        tasks.append(asyncio.create_task(DogsHouse(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy).stats()))

    data = await asyncio.gather(*tasks)

    path = f"statistics/statistics_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"
    columns = ['Phone number', 'Name', 'Balance', 'Leaderboard', 'Age', 'Referrals', 'Referral link', 'Proxy (login:password@ip:port)']

    if not os.path.exists('statistics'): os.mkdir('statistics')
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(path, index=False, encoding='utf-8-sig')

    logger.success(f"Saved statistics to {path}")
