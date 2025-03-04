# finance_tracker/tests/test_crud.py
import pytest
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import crud, models

@pytest.fixture(scope="module")
def db():
    # Создание тестовой базы данных
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_create_user(db: Session):
    user = crud.create_user(db, name="Alice", email="alice@example.com")
    assert user.id is not None
    assert user.name == "Alice"

def test_add_transaction(db: Session):
    user = crud.create_user(db, name="Bob", email="bob@example.com")
    category = crud.create_category(db, name="Еда")
    transaction = crud.add_transaction(db, user_id=user.id, category_id=category.id, amount=50, transaction_type="expense")
    assert transaction.id is not None
    assert transaction.amount == 50