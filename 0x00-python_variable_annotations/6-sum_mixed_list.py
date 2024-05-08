#!/usr/bin/env python3
"""contains a function  which takes
a list of integers and floats and returns their sum as a float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of lists as a float"""
    return sum(mxd_lst)
