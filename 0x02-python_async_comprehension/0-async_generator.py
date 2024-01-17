#!/usr/bin/env python3
"""Defines 0-async_generator.py"""
import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields a random number between 0 and 10
    after asynchronously waiting for 1 second.
    This process is repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    """
    Asynchronously iterates over the values yielded by the async_generator
    and prints the result.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(f"Function looped {len(result)} times.")

asyncio.run(print_yielded_values())
