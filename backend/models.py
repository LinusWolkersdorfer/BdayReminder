from datetime import date
from sqlmodel import SQLModel, Field # pyright: ignore[reportMissingImports]

class BdayBase(SQLModel):
    birthday: date
    first_name: str
    last_name: str
    created_at: date
    updated_at: date


class Bday(BdayBase, table=True):
    id: int = Field(default=None, primary_key=True)


class BdayCreate(SQLModel):
    first_name: str
    last_name: str
    birthday: date
