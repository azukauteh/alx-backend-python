#!/usr/bin/env python3
"""Defines 2-measure_runtime.py"""
import asyncio
import time
import random
from typing import List
from concurrent.futures import ProcessPoolExecutor


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds.

    :param max_delay: Maximum delay in seconds (default is 10).
    :return: The random delay.
    """

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n
    times with the specified max_delay.

    :param n: Number of times to spawn wait_random.
    :param max_delay: Maximum delay in seconds for
                     wait_random (default is 10).
    :return: List of delays in ascending order.
    """
    delays = []

    """ Use asyncio.gather to concurrently execute wait_random"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    """ Sort the results in ascending order"""
    delays = sorted(results)

    return delays


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return total_time / n.

    :param n: Number of times to spawn wait_random.
    :param max_delay: Maximum delay in seconds for wait_random.
    :return: Average time per iteration.
    """
    start_time = time.time()


async def run_wait_n(n, max_delay):
    """
    Run wait_n asynchronously.
    """
    await wait_n(n, max_delay)

    """ Use ProcessPoolExecutor to run the event loop in a separate process"""
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as executor:
        loop.run_until_complete(loop.run_in_executor(executor, run_wait_n))

    end_time = time.time()
    total_time = end_time - start_time

    """ Return average time per iteration"""
    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
