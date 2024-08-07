#!/usr/bin/env python3

""" Async Comprehensions """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions """
    start = time()
    # tasks = [async_comprehension() for i in range(4)]
    # await gather(*tasks)
    # for i in range(1):
    await async_comprehension()
    end = time()
    return (end - start)
