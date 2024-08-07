#!/usr/bin/env python3
""" The basics of async """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn task_wait_random n times with the specified max_delay.
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)
    return results
