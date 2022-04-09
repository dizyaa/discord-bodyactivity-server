import pypresence
import schemas
import config

RPC = pypresence.Presence(config.DISCORD_PRESENCE_ID)


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
        large_image="heart",
        buttons=[{"label": "GitHub", "url": "https://github.com/dizyaa/discord-bodyactivity-android"}]
    )
