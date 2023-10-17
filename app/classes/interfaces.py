from abc import ABC, abstractclassmethod
from typing import Any, List, Union

from classes.validation import FilterRequestModel


class IRepository(ABC):

    """
    ## This interface provides access to the repository abstraction

    1. get - returns a document or list[document] by the given id
    2. add - adds a document in the end of collecttion
    3. update - updates a document by the given id
    4. remove - removes a document by the given id
    """

    @abstractclassmethod
    def get(self, limit: int, offset: int, **kwargs) -> Union[List[Any], Any]:
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

        1. param element: the element to add

        ### returns None or raises exception
        """
        pass

    @abstractclassmethod
    def update(self, id: str, element) -> None:
        """
        ## Updates document by the elements's id

        1. param id: the id of the element from the generic collection
        2. param element: the element to update

        ### returns None or raises exception
        """
        pass

    @abstractclassmethod
    def remove(self, id: str) -> None:
        """
        ## Removes document by the element's id

        1. param id: the id of the element from the generic collection

        ### returns None or raises exception
        """
        pass
