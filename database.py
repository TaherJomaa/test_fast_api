from sqlmodel import SQLModel, create_engine
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
path_database = 'sqlite:///' + os.path.join(BASE_DIR, 'shop.db')
print(path_database)
engine = create_engine(path_database, echo=True)