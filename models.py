from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Agent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    working_area: str
    commission: int = Field(gt=0, lt=10)


class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str
    phone: str
    agent_code: Optional[int] = Field(default=None, foreign_key="agent.id")


class Order(SQLModel, table=True):
    num: Optional[int] = Field(default=None, primary_key=True)
    date: str
    description: str
    cust_code: Optional[int] = Field(default=None, foreign_key="customer.id")
    agent_code: Optional[int] = Field(default=None, foreign_key="agent.id")
