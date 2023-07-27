from fireo.models import Model
from app.database.firebase import get_db
from app.models.repositories.fields import fields
from app.models.repositories.repository_interface import IRepository
from fastapi.exceptions import HTTPException
from fireo.database import Database


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

    def __init__(self) -> None:  # TODO debug
        pass

    def connect(self):
        self.db = get_db()
        type = self.__orig_class__.__args__[0]

        return self.db.conn.collection(type.collection_name)

    def get(self, document_id: str) -> _T | None:
        """
        ## Get a document by id

        1. param document_id: the id of the document from the generic collection

        ### returns document of generic type or None if no document
        """

        element = self.connect().document(document_id=document_id)
        # element = self.connect().where(fields.ID, signs.EQ, document_id).get()
        return element

    def get_all(self) -> List[_T] | None:  # TODO debug
        """
        ## Gets all documents from the generic collection

        ### returns list of documents or None if no documents
        """

        elements: List = self.connect().get()
        # assert elements is list
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
            dict[fields.ID] = document_id
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
