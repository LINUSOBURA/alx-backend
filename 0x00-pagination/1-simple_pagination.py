#!/usr/bin/env python3
"""
simple pagination
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Function that calculates the start and end
    indices based on the page number and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data from the dataset.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        range_tuple = index_range(page, page_size)
        if range_tuple[1] > len(self.dataset()):
            return []
        return self.dataset()[range_tuple[0]:range_tuple[1]]
