
import os

class Settings:
    def __init__(self):
        self.DEBUG = os.getenv("DEBUG", "False") == "True"

        if self.DEBUG:
            self.TELEGRAM_BOT_TOKEN = "7309813282:AAFeJzOMokJdwE3IV3383GASYuB_FA7PWdI"
            self.GSPREAD_CREDENTIALS = os.path.join(os.path.dirname(__file__), "../secrets/pgpractice-adce347384eb.json")
        else:
            self.TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
            self.GSPREAD_CREDENTIALS = {
            "type": "service_account",
            "project_id": os.getenv("GSPREAD_PROJECT_ID"),
            "private_key_id": os.getenv("GSPREAD_PRIVATE_KEY_ID"),
            "private_key": os.getenv("GSPREAD_PRIVATE_KEY").replace("\\n", "\n"),
            "client_email": os.getenv("GSPREAD_CLIENT_EMAIL"),
            "client_id": os.getenv("GSPREAD_CLIENT_ID"),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": os.getenv("GSPREAD_CLIENT_X509_CERT_URL"),
            "universe_domain": "googleapis.com"
        }

settings = Settings()