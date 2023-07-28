from typing import Generic, List, TypeVar
from fireo.models import Model
from app.database.firebase import get_db
from app.models.repositories.fields import fields
from app.models.repositories.repository_interface import IRepository
from fastapi.exceptions import HTTPException

from app.models.validation import FilterRequestModel


_T = TypeVar("_T", bound=Model)


class FirebaseRepository(Generic[_T], IRepository):

    """
    ## This repository provides access to the firebase

    1. get - returns a document with the given id
    2. get_all - returns all documents
    3. add - adds a document
    4. update - updates a document by the given id
    5. remove - removes a document by the given id
    """

    def __init__(self) -> None:
        pass

    def connect(self):
        self.db = get_db()
        type = self.__orig_class__.__args__[0]

        return self.db.conn.collection(type.collection_name)

    def get(
        self, limit: int, offset: int, document_id: str, where: FilterRequestModel
    ) -> List[_T]:
        """
        ## Get a document by id

        1. param limit - the number of documents to retrieve
        2. param offset - the offset to get the document
        3. param document_id: the id of the document from the generic collection

        ### returns a list of documents
        """
        element = self.connect()
        if document_id == "":
            element = element.limit(limit).offset(offset)
            if where:
                element = element.where(**where.dict(exclude_defaults=True))
        else:
            element = element.document(document_id=document_id)

        # element = self.connect().where(fields.ID, signs.EQ, document_id).get()
        return element.get()

    def get_all(self) -> List[_T] | None:  # TODO debug
        """
        ## Gets all documents from the generic collection

        ### returns list of documents
        """

        elements: List[_T] = self.connect().get()
        return elements

    def add(self, element: _T) -> None:
        """
        ## Adds a document in the generic collection

        1. param element: the document to add

        ### returns None or raises exception
        """

        try:
            self.connect().add(element.to_dict(exclude_defaults=True))
        except Exception:
            raise HTTPException(status_code=400)

    def update(self, document_id: str, element: _T) -> None:  # TODO debug
        """
        ## Updates document by the document's id

        1. param document_id: the id of the document from the generic collection
        2. param element: the source document for the update

        ### returns None or raises exception
        """

        try:
            self.remove(document_id)
            d: dict = element.to_dict(exclude_defaults=True)
            d[fields.ID] = document_id
            self.connect().add(dict)

        except Exception:
            raise HTTPException(status_code=400)

    def remove(self, document_id: str) -> None:  # TODO debug
        """
        ## Removes document by the document's id

        1. param document_id: the id of the document from the generic collection

        ### returns None or raises exception
        """

        try:
            self.connect().document(document_id).delete()
        except Exception:
            raise HTTPException(status_code=400)
