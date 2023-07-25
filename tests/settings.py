from dataclasses import dataclass
from typing import List


@dataclass
class Settings:
    url: str = "http://localhost:8000"
    get: str = "/select"
    post: str = "/insert"
    put: str = "/update"
    delete: str = "/delete"
