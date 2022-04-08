from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/reports", response_model=schemas.Report)
def create_report(user: schemas.ReportCreate, db: Session = Depends(get_db)):
    db_user = crud.get_report_by_timestamp(db, timestamp=user.time)
    if db_user:
        raise HTTPException(status_code=400, detail="Report already created")
    return crud.create_report(db=db, user=user)

