from sqlalchemy.orm import Session

import models
import schemas


def get_report_by_id(db: Session, identifier: int):
    return db.query(models.Report).filter(models.Report.id == identifier).first()


def get_report_by_timestamp(db: Session, timestamp: int):
    return db.query(models.Report).filter(models.Report.time == timestamp).first()


def get_last_report(db: Session):
    return db.query(models.Report).order_by(models.Report.id.desc()).first()


def create_report(db: Session, report: schemas.ReportCreate):
    db_report = models.Report(
        heartRate=report.heartRate,
        steps=report.steps,
        time=report.time,
        activity=report.activity
    )
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report
