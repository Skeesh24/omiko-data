from typing import Generic, List, TypeVar
from fireo.models import Model
from fireo.database import Database
from app.database.firebase import get_db
from app.models.repositories.fields import fields
from app.models.repositories.repository_interface import IRepository
from fastapi.exceptions import HTTPException

from google.cloud.firestore_v1.collection import CollectionReference

from app.models.validation import FilterRequestModel


_T = TypeVar("_T", bound=Model)


class FirebaseRepository(Generic[_T], IRepository):

    """
    ## This repository provides access to the firebase

    1. get - returns a document with the given id
    2. add - adds a document
    3. update - updates a document by the given id
    4. remove - removes a document by the given id
    """

    def __init__(self) -> None:
        self.db = get_db()

    def connect(self) -> CollectionReference:
        type = self.__orig_class__.__args__[0]
        return self.db.conn.collection(type.collection_name)

    def get(
        self, limit: int, offset: int, document_id: str, where: FilterRequestModel
    ) -> List[_T]:
        """
        ## Gets a document by id

        1. param limit - the number of documents to retrieve
        2. param offset - the offset to get the document
        3. param document_id: the id of the document from the generic collection
        4. param where - the filter to get the document

        ### returns a list of documents
        """
        query = self.connect()
        try:
            if document_id == "":
                if where:
                    query = query.where(**where.dict(exclude_defaults=True))
                query = query.limit(limit).offset(offset)
            else:
                query = query.document(document_id=document_id)
        except:
            raise HTTPException(status_code=400)

        return query.get()

    def add(self, element: _T) -> None:
        """
        ## Adds a document in the generic collection

        1. param element: the document to add

        ### returns None or raises exception
        """
        query = self.connect()

        try:
            query.add(element.dict(exclude_defaults=True))
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
            d: dict = element.dict(exclude_defaults=True)
            d[fields.ID] = document_id
            self.connect().add(d)

        except Exception:
            raise HTTPException(status_code=400)

    def remove(self, document_id: str, where: FilterRequestModel) -> None:  # TODO debug
        """
        ## Removes document by the document's id

        1. param document_id: the id of the document from the generic collection
        2. param where: the filter to remove the documents

        ### returns None or raises exception
        """
        if (document_id == "") and (not where):
            return

        query = self.connect()

        try:
            if document_id != "":
                query.document(document_id).delete()
                return
            if where:
                keys = [
                    doc.id
                    for doc in query.where(**where.dict(exclude_defaults=True)).get()
                ]
                [query.document(key).delete() for key in keys]
                return
        except Exception as e:
            raise HTTPException(status_code=400)
