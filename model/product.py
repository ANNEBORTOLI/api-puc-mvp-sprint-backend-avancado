from sqlalchemy import DECIMAL, Column, Integer, String
from model import Base


class Product(Base):
    __tablename__ = "product"

    id = Column("pk_product", Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    size = Column(String(10), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=True)
    description = Column(String(250), nullable=True)

    def __init__(self, title: str, size: str, price: float, description: str):
        self.title = title
        self.size = size
        self.price = price
        self.description = description


    def setProduct(self, title: str, size: str, price: float, description: str):

        self.title = title
        self.size = size
        self.price = price
        self.description = description
