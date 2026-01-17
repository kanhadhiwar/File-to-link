import firebase_admin
from firebase_admin import credentials, db

# 1. Service account key (same folder me rakhi ho)
cred = credentials.Certificate("firebase_key.json")

# 2. Firebase initialize with databaseURL
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://html-e256d-default-rtdb.asia-southeast1.firebasedatabase.app"
})

# 3. Reference (HTML pages data)
html_ref = db.reference("html_pages")
