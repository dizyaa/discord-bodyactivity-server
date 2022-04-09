from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import discord_integration
import crud
import models
import schemas
from database import SessionLocal, engine
from logger import logger

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/reports", response_model=schemas.Report)
def create_report(user: schemas.ReportCreate, db: Session = Depends(get_db)):
    logger.info(user.json())
    db_user = crud.get_report_by_timestamp(db, timestamp=user.time)
    if db_user:
        raise HTTPException(status_code=400, detail="Report already created")
    discord_integration.update(report=user)
    return crud.create_report(db=db, user=user)
