#!/usr/bin/env python3
"""
Helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Function that calculates the start and end
    indices based on the page number and page size.

    Parameters:
    - page: an integer representing the current
    page number
    - page_size: an integer representing the number
    of items per page

    Returns:
    - A tuple containing the start index and end
    index for the given page and page size
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
