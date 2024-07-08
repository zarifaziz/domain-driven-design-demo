# src/main.py

from .domain.engine_model import EngineModel
from .orm.setup import SessionLocal, init_db
from .repository.sql_alchemy_engine_repository import \
    SQLAlchemyEngineRepository


def main():
    init_db()
    session = SessionLocal()
    repository = SQLAlchemyEngineRepository(session)

    # Add a new engine
    new_engine = EngineModel(engine_id="ENG1234", horsepower=300)
    repository.add(new_engine)
    session.commit()

    # Retrieve and print engine details
    engine = repository.get("ENG1234")
    if engine:
        print(
            f"Retrieved Engine: {engine.engine_id} with {engine.horsepower} HP, running: {engine.is_running}"
        )

    # Update engine status
    engine.set_running(True)
    repository.update(engine)
    session.commit()

    # List all engines
    engines = repository.list()
    for eng in engines:
        print(
            f"Engine: {eng.engine_id}, HP: {eng.horsepower}, Running: {eng.is_running}"
        )

    # Delete the engine
    repository.delete("ENG1234")
    session.commit()
    print(f"Deleted Engine: ENG1234")

    session.close()


if __name__ == "__main__":
    main()
