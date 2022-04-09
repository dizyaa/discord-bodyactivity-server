import pypresence
import schemas

RPC = pypresence.Presence("949059085515517982")


def start():
    print("Connecting to discord presence...")
    RPC.connect()


def update(report: schemas.ReportBase):
    RPC.update(
        state="Steps: {}".format(report.steps),
        details='Heart rate: {}'.format(report.heartRate),
        large_image="bird"
    )
