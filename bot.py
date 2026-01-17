from pyrogram import Client, filters
import json, uuid

BOT_TOKEN = "YOUR_BOT_TOKEN"
API_ID = 123456
API_HASH = "YOUR_API_HASH"
CHANNEL_ID = -1001234567890
DOMAIN = "https://your-domain.com"

app = Client(
    "html_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def load_db():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_db(db):
    with open("data.json", "w") as f:
        json.dump(db, f)

@app.on_message(filters.document)
async def handle_html(client, message):
    if not message.document.file_name.endswith(".html"):
        await message.reply("❌ Sirf .html file allowed hai")
        return

    sent = await message.copy(CHANNEL_ID)
    file_id = sent.document.file_id

    key = uuid.uuid4().hex[:8]
    db = load_db()
    db[key] = file_id
    save_db(db)

    link = f"{DOMAIN}/view/{key}"
    await message.reply(f"✅ HTML uploaded\n🔗 Link:\n{link}")

app.run()
