from sqlmodel import SQLModel
from models import Agent, Customer, Order
from database import engine

SQLModel.metadata.create_all(engine)
