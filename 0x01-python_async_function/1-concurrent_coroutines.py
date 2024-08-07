#!/usr/bin/env python3
""" The basics of async """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay.
    """
    tasks:list = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    
    # await tasks
    results = await asyncio.gather(*tasks)
    results.sort()
    return results

