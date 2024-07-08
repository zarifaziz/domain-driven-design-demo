# src/repository/base_engine_repository.py

from abc import ABC, abstractmethod
from typing import List

from ..domain.engine_model import EngineModel


class BaseEngineRepository(ABC):
    @abstractmethod
    def add(self, engine: EngineModel) -> None:
        pass

    @abstractmethod
    def get(self, engine_id: str) -> EngineModel:
        pass

    @abstractmethod
    def update(self, engine: EngineModel) -> None:
        pass

    @abstractmethod
    def delete(self, engine_id: str) -> None:
        pass

    @abstractmethod
    def list(self) -> List[EngineModel]:
        pass
