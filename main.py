import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
import datetime

import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from db import create_database, create_session
create_database()

jsonf = "client.json"
sheet_api_key = os.environ.get("SHEET_CLIENT_SECRET")


def connect_gspread(jsonf,key):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonf, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
    return worksheet

def send_to_sheet(sheet_api_key):
    ws = connect_gspread(jsonf,sheet_api_key)
    dt = datetime.datetime.now()
    dt = str(dt.strftime('%Y-%m-%d %H:%M:%S'))
    data = [dt, "B6追加"]
    ws.append_row(data)

if __name__ == "__main__":
    send_to_sheet(sheet_api_key)
    print("send success")