# tests/services/test_car_service.py

import unittest

from src.domain.engine_model import EngineModel
from src.repository.base_engine_repository import BaseEngineRepository
from src.services.car_service import CarService


class FakeEngineRepository(BaseEngineRepository):
    def __init__(self):
        self.engines = {}

    def add(self, engine: EngineModel) -> None:
        self.engines[engine.engine_id] = engine

    def get(self, engine_id: str) -> EngineModel:
        return self.engines.get(engine_id)

    def update(self, engine: EngineModel) -> None:
        if engine.engine_id in self.engines:
            self.engines[engine.engine_id] = engine

    def delete(self, engine_id: str) -> None:
        if engine_id in self.engines:
            self.engines.pop(engine_id)

    def list(self) -> list[EngineModel]:
        return list(self.engines.values())


class TestCarService(unittest.TestCase):
    def setUp(self):
        self.engine_repository = FakeEngineRepository()
        self.car_service = CarService(self.engine_repository)

    def test_add_engine(self):
        self.car_service.add_engine("engine1", 100)
        engine = self.engine_repository.get("engine1")
        self.assertIsInstance(engine, EngineModel)
        self.assertEqual(engine.horsepower, 100)

    def test_start_engine(self):
        self.car_service.add_engine("engine1", 100)
        self.car_service.start_engine("engine1")
        engine = self.engine_repository.get("engine1")
        self.assertTrue(engine.is_running)


if __name__ == "__main__":
    unittest.main()
