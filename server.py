from flask import Flask, abort, Response
from pyrogram import Client
import json, asyncio

API_ID = 123456
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

app = Flask(__name__)

tg = Client(
    "server",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def load_db():
    with open("data.json") as f:
        return json.load(f)

@app.route("/view/<key>")
def view_html(key):
    db = load_db()
    if key not in db:
        abort(404)

    async def fetch():
        await tg.start()
        msg = await tg.get_messages("me", file_id=db[key])
        file = await msg.download(in_memory=True)
        return file.getvalue()

    html = asyncio.run(fetch())
    return Response(html, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
