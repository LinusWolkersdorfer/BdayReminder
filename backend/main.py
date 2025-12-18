from fastapi import FastAPI, Depends, HTTPException # pyright: ignore[reportMissingImports]
from datetime import date
from contextlib import asynccontextmanager
from sqlmodel import Session, select # pyright: ignore[reportMissingImports]

from db import init_db, get_session
from models import Bday, BdayCreate
from fastapi.middleware.cors import CORSMiddleware # type: ignore


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/bdays")
async def get_all_bdays(session: Session = Depends(get_session)):
    bdays = session.exec(select(Bday)).all()

    if bdays is None:
        raise HTTPException(status_code=404, detail="Database empty")

    return bdays


@app.post("/bdays")
async def create_bday(bday_data: BdayCreate, session: Session = Depends(get_session)):
    today = date.today()
    if bday_data.birthday is None:
        print("test123123123")
        raise HTTPException(status_code=404, detail="birthday empty, Expected format: YYYY-MM-DD")
    if bday_data.first_name is None:
        raise HTTPException(status_code=404, detail="firstname empty")
    if bday_data.last_name is None:
        raise HTTPException(status_code=404, detail="lastname empty")

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
    
    if (bday_data.first_name is None and bday_data.last_name is None and bday_data.birthday is None):
        raise HTTPException(status_code=400, detail="at least one change is required")

    if bday_data.first_name is not None:
        bday.first_name = bday_data.first_name
    if bday_data.last_name is not None:
        bday.last_name = bday_data.last_name
    if bday_data.birthday is not None:
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
