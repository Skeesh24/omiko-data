from abc import abstractclassmethod, ABC
from typing import Any

from app.models.validation import FilterRequestModel


class IRepository(ABC):
    @abstractclassmethod
    def get(
        self, limit: int, offset: int, document_id: str, where: FilterRequestModel
    ) -> Any:
        """
        ## Gets a document by id

        1. param limit - the number of documents to retrieve
        2. param offset - the offset to get the document
        3. param document_id: the id of the document from the generic collection
        4. param where - the filter to get the document

        ### returns a list of documents
        """
        pass

    @abstractclassmethod
    def add(self, element) -> None:
        """
        ## Adds a document in the generic collection

        1. param element: the document to add

        ### returns None or raises exception
        """
        pass

    @abstractclassmethod
    def update(self, document_id: str, element) -> None:
        """
        ## Updates document by the document's id

        1. param document_id: the id of the document from the generic collection
        2. param element: the source document for the update

        ### returns None or raises exception
        """
        pass

    @abstractclassmethod
    def remove(self, document_id: str) -> None:
        """
        ## Removes document by the document's id

        1. param document_id: the id of the document from the generic collection

        ### returns None or raises exception
        """
        pass
