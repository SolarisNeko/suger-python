from typing import Callable, Iterable, Dict, Any, Set


class Stream:
    def __init__(self, data: Iterable) -> None:
        self.data = data

    def sort(self, sortedFunc=None, reverse=False):
        return Stream(sorted(self.data, key=sortedFunc, reverse=reverse))

    def map(self, func: Callable) -> "Stream":
        return Stream(func(item) for item in self.data)

    def flatMap(self, func: Callable) -> "Stream":
        return Stream(item for sublist in self.data for item in func(sublist))

    def filter(self, func: Callable) -> "Stream":
        return Stream(item for item in self.data if func(item))

    def first(self) -> Any:
        return next(iter(self.data), None)

    def count(self) -> int:
        return sum(1 for _ in self.data)

    def toList(self) -> list:
        return list(self.data)

    def toDictionary(self, key_func: Callable, value_func: Callable) -> Dict:
        return {key_func(item): value_func(item) for item in self.data}

    def toSet(self) -> Set:
        return set(self.data)
