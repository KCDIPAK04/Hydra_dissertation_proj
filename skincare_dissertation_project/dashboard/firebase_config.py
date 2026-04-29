import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(
    "hydra-skincare-firebase-adminsdk-fbsvc-1789de040f.json"
)

firebase_admin.initialize_app(cred)