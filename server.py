from pyrogram import Client, filters
import uuid, time
from firebase_db import html_ref

API_ID = 123456
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = -1001234567890
DOMAIN = "https://your-domain.com"

app = Client(
    "html_upload_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.document)
async def upload_html(client, message):
    if not message.document.file_name.lower().endswith(".html"):
        await message.reply("❌ Sirf .html file allowed hai")
        return

    sent = await message.copy(CHANNEL_ID)
    file_id = sent.document.file_id

    key = uuid.uuid4().hex[:8]

    html_ref.child(key).set({
        "file_id": file_id,
        "created_at": int(time.time())
    })

    await message.reply(
        f"✅ HTML uploaded successfully\n\n"
        f"🔗 Link:\n{DOMAIN}/view/{key}"
    )

print("🤖 Bot started")
app.run()
