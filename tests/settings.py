from dataclasses import dataclass


@dataclass
class Settings:
    url: str = "http://localhost:8000"
    operations: list = ["/select", "/insert", "/update", "/delete"]
