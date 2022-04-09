from sqlalchemy.orm import Session

import models
import schemas


def get_report_by_id(db: Session, identifier: int):
    return db.query(models.Report).filter(models.Report.id == identifier).first()


def get_report_by_timestamp(db: Session, timestamp: int):
    return db.query(models.Report).filter(models.Report.time == timestamp).first()


def create_report(db: Session, user: schemas.ReportCreate):
    db_report = models.Report(
        heartRate=user.heartRate,
        steps=user.steps,
        time=user.time
    )
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report
