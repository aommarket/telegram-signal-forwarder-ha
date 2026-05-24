import re
from telethon import TelegramClient, events

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]

SOURCE = "WallstreetQueenOfficialViP"
TARGET = "wqovip"

client = TelegramClient("userbot", API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE))
async def handler(event):

    text = event.raw_text or ""

    # Skip SHORT signals
    if re.search(r"Direction\s*:\s*Short", text, re.IGNORECASE):
        return

    # Convert leverage line to Spot
    text = re.sub(
        r"Leverage\s*:\s*[0-9\-]+x",
        "Spot",
        text,
        flags=re.IGNORECASE
    )

    # If photo exists, only send caption text
    if event.photo:
        if text.strip():
            await client.send_message(
                TARGET,
                text,
                link_preview=False
            )
        return

    # Normal text post
    if text.strip():
        await client.send_message(
            TARGET,
            text,
            link_preview=False
        )

client.start()
client.run_until_disconnected()
