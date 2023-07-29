from abc import abstractclassmethod, ABC
from typing import Any

from app.models.validation import FilterRequestModel


class IRepository(ABC):
    @abstractclassmethod
    def get(
        self, limit: int, offset: int, document_id: str, where: FilterRequestModel
    ) -> Any:
        pass

    @abstractclassmethod
    def add(self, element) -> None:
        pass

    @abstractclassmethod
    def update(self, document_id: str, element) -> None:
        pass

    @abstractclassmethod
    def remove(self, document_id: str, where: FilterRequestModel) -> None:
        pass