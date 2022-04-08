import pypresence
import time

RPC = pypresence.Presence("949059085515517982")
isEnabled = True


def start():
    RPC.connect()
    print("Starting discord_integration...")

    while isEnabled:
        time.sleep(5)
        update()


def update():
    updates = RPC.update(
        state="123",
        details="321"
    )
    print(updates)
