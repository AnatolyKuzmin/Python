# finance_tracker/schemas.py
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    amount: float
    type: str
    user_id: int
    category_id: int

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    date: datetime
    class Config:
        orm_mode = True