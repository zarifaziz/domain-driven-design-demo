# src/orm/mapper.py
# responsible for defining table schema and mapping the domain model to the table

from sqlalchemy import Boolean, Column, Integer, MetaData, String, Table
from sqlalchemy.orm import mapper

from ..domain.engine_model import EngineModel

metadata = MetaData()

engines = Table(
    "engines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("engine_id", String(255), unique=True, nullable=False),
    Column("horsepower", Integer, nullable=False),
    Column("is_running", Boolean, default=False),
)


def start_mappers():
    mapper(EngineModel, engines)
