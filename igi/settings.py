from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    base_dir: Path = Path(".")
    data_dir: Path = base_dir.joinpath("data")
    game_dir: Path = Path(r"C:\Program Files (x86)\GOG Galaxy\Games\IGI 2 - Covert Strike")


settings = Settings()
