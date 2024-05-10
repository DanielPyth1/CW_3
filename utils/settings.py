from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath('data')
PROFESSIONS_JSON_PATH = DATA_PATH.joinpath('operations.json')