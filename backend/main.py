from http.client import HTTPException
from fastapi import FastAPI, Depends # pyright: ignore[reportMissingImports]
from datetime import date
from contextlib import asynccontextmanager
from sqlmodel import Session, select # pyright: ignore[reportMissingImports]

from db import init_db, get_session
from models import Bday, BdayCreate


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root1():
    return ["Hello,", " World!"]


@app.post("/")
def root2():
    return ["Hello,", " World!"]


@app.get("/bdays")
async def get_all_bdays(session: Session = Depends(get_session)):
    bdays = session.exec(select(Bday)).all()
    return bdays


@app.post("/bdays")
async def create_bday(bday_data: BdayCreate, session: Session = Depends(get_session)):
    today = date.today()
    bday = Bday(birthday=bday_data.birthday, first_name=bday_data.first_name, last_name=bday_data.last_name, created_at=today, updated_at=today)
    session.add(bday)
    session.commit()
    session.refresh(bday)

    return bday


@app.get("/bdays/{bday_id}")
async def get_bday_by_id(bday_id: int, session: Session = Depends(get_session)):
    bday = session.get(Bday, bday_id)
    
    if bday is None:
        raise HTTPException(status_code=404, detail="Bday not found")
    
    return bday


@app.put("/bdays/{bday_id}")
async def update_bday_by_id(bday_id: int, bday_data: BdayCreate, session: Session = Depends(get_session)):
    bday = session.get(Bday, bday_id)
    
    if bday is None:
        raise HTTPException(status_code=404, detail="Bday not found")

    bday.first_name = bday_data.first_name
    bday.last_name = bday_data.last_name
    bday.birthday = bday_data.birthday
    bday.updated_at = date.today()

    session.commit()
    session.refresh(bday)

    return bday


@app.delete("/bdays/{bday_id}")
async def delete_bday_by_id(bday_id: int, session: Session = Depends(get_session)):
    bday = session.get(Bday, bday_id)
    
    if bday is None:
        raise HTTPException(status_code=404, detail="Bday not found")

    session.delete(bday)
    session.commit()
    
    return {"detail": f"Bday with ID {bday_id} has been deleted"}
