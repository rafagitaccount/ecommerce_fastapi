from code import interact
from tkinter import CASCADE
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text, column
from sqlalchemy.orm import relationship

from db import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    product = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    quantity = Column(Integer)
    description = Column(Text)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey(
        "category.id", ondelete="CASCADE"))
    category = relationship("Category", back_populates="product")
