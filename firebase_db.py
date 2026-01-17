import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase_key.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://YOUR_PROJECT_ID-default-rtdb.asia-southeast1.firebasedatabase.app"
})

html_ref = db.reference("html_pages")
