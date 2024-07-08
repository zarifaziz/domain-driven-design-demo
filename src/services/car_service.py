# src/services/car_service.py

from ..domain.engine_model import EngineModel
from ..repository.base_engine_repository import BaseEngineRepository


class CarService:
    def __init__(self, engine_repository: BaseEngineRepository):
        self.engine_repository = engine_repository

    def add_engine(self, engine_id: str, horsepower: int) -> None:
        engine = EngineModel(engine_id=engine_id, horsepower=horsepower)
        self.engine_repository.add(engine)

    def start_engine(self, engine_id: str) -> None:
        engine = self.engine_repository.get(engine_id)
        if engine:
            engine.start()
            self.engine_repository.update(engine)
