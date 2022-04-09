from pydantic import BaseModel


class ReportBase(BaseModel):
    heartRate: int
    steps: int
    time: int


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: int

    class Config:
        orm_mode = True
