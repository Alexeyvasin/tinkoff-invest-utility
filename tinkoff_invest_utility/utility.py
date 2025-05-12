
import asyncio
from tinkoff.invest import AsyncClient

async def get_instrument(token, ticker):
    
    async with AsyncClient(token) as client:
        futures_task = client.instruments.futures()
        futures = await asyncio.gather(futures_task)

    instruments = futures[0].instruments

    for instrument in instruments:
        if instrument.ticker == ticker:
            return instrument
    return None
