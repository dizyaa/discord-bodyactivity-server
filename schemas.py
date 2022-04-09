from pydantic import BaseModel, Field


class ReportBase(BaseModel):
    heartRate: int | None = Field(None, title="Heart Rate")
    steps: int | None = Field(None, title="Steps")
    activity: str | None = Field(None, title="User activity")
    time: int | None = Field(None, title="Timestamp")


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: int

    class Config:
        orm_mode = True
