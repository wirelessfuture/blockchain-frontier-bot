import abc
from typing import Protocol


class ResponseP(Protocol):
    data: dict


class ResponseParserT(abc.ABC):
    @abc.abstractmethod
    def transform(self, request: dict) -> any:
        pass