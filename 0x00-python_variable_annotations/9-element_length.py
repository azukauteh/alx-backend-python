#!/usr/bin/env python3
"""Defines 9-element_length.py"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Return a list of tuples containing each element and its length."""
    return [(i, len(i)) for i in lst]
