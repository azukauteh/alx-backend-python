#!/usr/bin/env python3
"""Defines 7-to_kv.py"""
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square of int/float v."""
    return k, float(v ** 2)
