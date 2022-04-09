import pypresence
import schemas

RPC = pypresence.Presence("949059085515517982")


def start():
    print("Connecting to discord presence...")
    RPC.connect()


def update(report: schemas.ReportBase):
    states = {
        "UNKNOWN": "Unknown",
        "EXERCISE": "Exercising",
        "PASSIVE": "Idling",
        "ASLEEP": "Sleeping"
    }

    RPC.update(
        state='Status: {}'.format(states.get(report.activity)),
        details='Heart rate: {}'.format(report.heartRate),
        large_image="heart"
    )
