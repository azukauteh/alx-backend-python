#!/usr/bin/env python3
import asyncio
from typing import Union


def wait_random(max_delay: int = 10) -> float:
    import random
    random_delay = random.uniform(0, max_delay)
    return random_delay

async def run_wait_random(max_delay: int, future: asyncio.Future) -> None:
    result = wait_random(max_delay)
    future.set_result(result)

def task_wait_random(max_delay: int) -> asyncio.Future[Union[None, float]]:
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    
    asyncio.ensure_future(run_wait_random(max_delay, future))
    
    return future
