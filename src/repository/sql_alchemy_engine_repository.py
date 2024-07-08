# src/repository/sql_alchemy_engine_repository.py
from typing import List

from sqlalchemy.orm import Session

from ..domain.engine_model import EngineModel
from .base_engine_repository import BaseEngineRepository


class SQLAlchemyEngineRepository(BaseEngineRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, engine: EngineModel) -> None:
        self.session.add(engine)
        self.session.commit()

    def get(self, engine_id: str) -> EngineModel:
        return (
            self.session.query(EngineModel)
            .filter(EngineModel.engine_id == engine_id)
            .first()
        )

    def update(self, engine: EngineModel) -> None:
        existing_engine = self.get(engine.engine_id)
        if existing_engine:
            existing_engine.horsepower = engine.horsepower
            existing_engine.set_running(
                engine.is_running
            )  # Use the public method to update the attribute
            self.session.commit()

    def delete(self, engine_id: str) -> None:
        engine = self.get(engine_id)
        if engine:
            self.session.delete(engine)
            self.session.commit()

    def list(self) -> List[EngineModel]:
        return self.session.query(EngineModel).all()
