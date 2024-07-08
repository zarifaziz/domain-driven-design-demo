from dataclasses import dataclass, field
from typing import List


@dataclass
class EngineModel:
    engine_id: str
    horsepower: int
    _is_running: bool = field(default=False, init=False)

    def start(self):
        if not self._is_running:
            self._is_running = True
            print(f"Engine {self.engine_id} with {self.horsepower} HP started.")
        else:
            print(f"Engine {self.engine_id} is already running.")

    def stop(self):
        if self._is_running:
            self._is_running = False
            print(f"Engine {self.engine_id} stopped.")
        else:
            print(f"Engine {self.engine_id} is not running.")

    def set_running(self, is_running: bool):
        self._is_running = is_running

    @property
    def is_running(self):
        return self._is_running
