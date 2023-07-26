from app.database.firebase import get_db
from app.models.repositories.fields import signs, fields
from app.models.repositories.functions import type_asscociation
from app.models.repositories.repository_interface import IRepository
from typing import Generic, Iterable, List, TypeVar
from fastapi.exceptions import HTTPException


_T = TypeVar("_T")


class FirebaseRepository(Generic(_T), IRepository):

    """
    ## This repository provides access to the firebase

    1. get - returns a document with the given id
    2. get_all - returns all documents
    3. add - adds a document
    4. update - updates a document by the given id
    5. remove - removes a document by the given id
    """

    def __init__(self) -> None:  # TODO debug
        self.db = get_db()
        self.collection_name = type_asscociation(_T)
        self.collection = self.db.conn.collection(self.collection_name)

    def get(self, document_id: str) -> _T | None:
        """
        ## Get a document by id

        1. param document_id: the id of the document from the generic collection

        ### returns document of generic type or None if no document
        """

        element: _T = self.collection.where(fields.ID, signs.EQ, id).get()
        return element

    def get_all(self) -> List[_T] | None:  # TODO debug
        """
        ## Gets all documents from the generic collection

        ### returns list of documents or None if no documents
        """

        elements = self.collection.get()
        assert elements is Iterable, "is not a list"  # is that correct?
        if len(elements) == 0:
            return None
        return elements

    def add(self, element: _T) -> None:
        """
        ## Adds a document in the generic collection

        1. param element: the document to add

        ### returns None or raises exception
        """

        try:
            self.collection.add(element.to_dict(exclude_defaults=True))
        except Exception as e:
            raise HTTPException(status_code=400)

    def update(self, document_id: str, element: _T) -> None:  # TODO debug
        """
        ## Updates document by the document's id

        1. param document_id: the id of the document from the generic collection
        2. param element: the source document for the update

        ### returns None or raises exception
        """

        try:
            self.remove_by_id(document_id)
            dict = element.to_dict(exclude_defaults=True)
            dict[fields.ID] = id
            self.collection.add(dict)

        except Exception as e:
            raise HTTPException(status_code=400)

    def remove(self, document_id: str) -> None:  # TODO debug
        """
        ## Removes document by the document's id

        1. param document_id: the id of the document from the generic collection

        ### returns None or raises exception
        """

        try:
            self.db.conn.document(document_id).delete()
        except Exception as e:
            raise HTTPException(status_code=400)
