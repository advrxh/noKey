from pathlib import Path
import json
from pprint import pformat


class Selectors:
    def __init__(self) -> None:
        self.SELECTORS_PATH = Path(Path(__file__).parent.resolve(), "selectors.json")

        with self.SELECTORS_PATH.open("r+", encoding="utf-8") as selectorsFile:
            self.SELECTORS = json.load(selectorsFile)

    def __call__(self) -> dict:
        return self.SELECTORS
