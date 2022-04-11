import asyncio
import crud
import schemas
import discord_integration
from hypercorn.asyncio import serve
from hypercorn.config import Config
from database import SessionLocal

import server


def init_first_report():
    last_report = crud.get_last_report(SessionLocal())

    report = schemas.ReportCreate(
        heartRate=last_report.heartRate,
        steps=last_report.steps,
        activity=last_report.activity,
        time=last_report.time,
    )

    discord_integration.update(report=report)


def run_server():
    config = Config()
    config.bind = ["0.0.0.0:8000"]

    asyncio.run(serve(server.app, config))


if __name__ == '__main__':
    discord_integration.start()
    init_first_report()
    run_server()
