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


@app.post("/reports")
def create_report(request: schemas.ReportCreate, db: Session = Depends(get_db)):
    logger.info(request.json())

    last_report = crud.get_last_report(db)

    heartRate = request.heartRate
    steps = request.steps
    activity = request.activity
    time = request.time

    if last_report:
        if not heartRate:
            heartRate = last_report.heartRate
        if not steps:
            steps = last_report.steps
        if not activity:
            activity = last_report.activity
        if not time:
            time = last_report.time

    report = schemas.ReportCreate(
        heartRate=heartRate,
        steps=steps,
        activity=activity,
        time=time,
    )

    discord_integration.update(report=report)
    crud.create_report(db, report)

    return HTTPException(status_code=200)
