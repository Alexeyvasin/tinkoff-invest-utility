
import asyncio
from tinkoff.invest import AsyncClient

async def get_itstrument(token, tiker):
    
    async with AsyncClient(token) as client:
        futures_task = client.instruments.futures()
        futures = await asyncio.gather(futures_task)

    instruments = futures[0].instruments
    # print(type(instruments[0]))

    for instrument in instruments:
        if instrument.ticker == tiker:
            return instrument
