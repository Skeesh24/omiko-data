from typing import List, Union

from classes.interfaces import IRepository
from database.mysql.entities import Cabinet, Office, Order, Product, Product_Category
from database.sqlalchemy import get_session
from fastapi import HTTPException, status

domain_names = Union[Office, Cabinet, Product, Product_Category, Order]


class MysqlRepository(IRepository):
    def __init__(self, cls: domain_names) -> None:
        self.db = get_session()
        self.cls = cls

    def get(
        self, limit: int = 5, offset: int = 0, **kwargs
    ) -> Union[
        List[Office],
        List[Cabinet],
        List[Order],
        List[Product],
        List[Product_Category],
        Office,
        Cabinet,
        Order,
        Product,
        Product_Category,
    ]:
        query = self.db.query(self.cls)

        if len(kwargs) > 0 and all(
            [getattr(self.cls, k[0], None) for k in kwargs.items()]
        ):
            try:
                for k, v in kwargs.items():
                    query = query.filter(self.cls.__getattribute__(self.cls, k) == v)
            except AttributeError:
                return []

        return (
            [x.__dict__ for x in query.limit(limit).offset(offset).all()]
            if limit > 1
            else query.limit(limit).offset(offset).first().__dict__
        )

    def add(self, elem) -> domain_names:
        try:
            d = self.cls(**elem.__dict__)
            self.db.add(d)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        self.db.commit()

    def update(self, id: str, update_elem: domain_names) -> domain_names:
        elem = self.cls(id=id, **update_elem.__dict__)
        old = self.get(limit=1, offset=0, id=id)
        try:
            self.remove(old)
            self.add(elem)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        self.db.commit()
        return elem

    def remove(self, elem) -> None:
        try:
            self.db.delete(elem)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        self.db.commit()
