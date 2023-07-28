from dataclasses import dataclass
from typing import List


@dataclass
class Settings:
    URL: str = "http://localhost:8000"
    GET: str = "/select"
    POST: str = "/insert"
    PUT: str = "/update"
    DELETE: str = "/delete"

    