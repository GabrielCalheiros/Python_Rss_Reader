from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from app import db

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id_category = Column(Integer, primary_key=True)
    category_name = Column(String(255), nullable=False)

    feeds = relationship("Feed", back_populates="category")

class Subcategory(Base):
    __tablename__ = 'subcategory'
    id_subcategory = Column(Integer, primary_key=True)
    name_subcategory = Column(String(255), nullable=False)
    id_view = Column(Integer, ForeignKey('view.id_view'), nullable=False)

    view = relationship("View", back_populates="subcategories")
    feeds = relationship("Feed", back_populates="subcategory")
    entries = relationship("Entry", back_populates="subcategory")

class View(Base):
    __tablename__ = 'view'
    id_view = Column(Integer, primary_key=True)
    view_name = Column(Integer, nullable=False)

    subcategories = relationship("Subcategory", back_populates="view")

class Feed(Base):
    __tablename__ = 'feeds'
    id_feed = Column(Integer, primary_key=True)
    id_category = Column(Integer, ForeignKey('category.id_category'), nullable=False)
    id_subcategory = Column(Integer, ForeignKey('subcategory.id_subcategory'), nullable=False)
    feed_name = Column(String(255), nullable=False)
    html_url = Column(String(255), nullable=False)
    xml_url = Column(String(255), nullable=False)
    feed_icon = Column(String(255), nullable=False)

    category = relationship("Category", back_populates="feeds")
    subcategory = relationship("Subcategory", back_populates="feeds")

class Entry(Base):
    __tablename__ = 'entries'
    id_entry = Column(Integer, primary_key=True)
    id_subcategory = Column(Integer, ForeignKey('subcategory.id_subcategory'), nullable=False)
    title = Column(String(255), nullable=False)
    subtitle = Column(String(255), nullable=False)
    link = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    published = Column(TIMESTAMP, nullable=False)
    tags = Column(String(255), nullable=False)
    summary = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    comments = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    rating = Column(String(255), nullable=False)
    statistics = Column(String(255), nullable=False)
    duration = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    publisher = Column(String(255), nullable=False)

    subcategory = relationship("Subcategory", back_populates="entries")
