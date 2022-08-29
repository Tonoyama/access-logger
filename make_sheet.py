from apiclient.discovery import build 
#from apiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
#from googleapiclient.http import MediaIoBaseDownload
#import io
import sys
sys.path.append("../")
from config import *
 
 
SCOPES = ['https://www.googleapis.com/auth/drive', "https://www.googleapis.com/auth/spreadsheets"]
 
 
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'userData/service_account_key.json', SCOPES
)
http_auth = credentials.authorize(Http())
 
drive_service = build('drive', 'v3', http=http_auth)
sheet_service = build('sheets', 'v4', http=http_auth)

class drive:
    class create:
        @staticmethod
        def folder(name, parent):
            file_metadata = {
                'name': name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [parent]
            }
            file = drive_service.files().create(body=file_metadata,fields='id').execute()
            return file
        
        def spreadSheet(name, parent):
            file_metadata = {
                'name': name,
                'mimeType': 'application/vnd.google-apps.spreadsheet',
                'parents': [parent]
            }
            file = drive_service.files().create(body=file_metadata,fields='id').execute()
            return file

    @staticmethod
    def copy(fileID, parent, name=None):
        metadata = {
            "name":name,
            "parents":[parent]
        }
        file = drive_service.files().copy(
            fileId=fileID, body=metadata
        ).execute()
        return file
        
    @staticmethod
    def get(q=None):
        results = drive_service.files().list(
            q=q,
            pageSize=30, 
            fields="files(id, name, mimeType)"
        ).execute()
        items = results.get('files', [])
        return items

    @staticmethod
    def delete(fileID):
        file = drive_service.files().delete(
            fileId=fileID
        ).execute()
        return file
    
    
class spreadSheet:
    @staticmethod
    def get(fileID, range):
        value = sheet_service.spreadsheets().values().get(
            spreadsheetId=fileID, range=range
        ).execute()
        return value
    
    @staticmethod
    def append(fileId, data, range):
        try:
            if not range:
                raise Exception("範囲が指定されていません")
            range += "!A1"
            sheet_service.spreadsheets().values().append(
                spreadsheetId=fileId,
                range=range,
                valueInputOption="USER_ENTERED",
                insertDataOption="INSERT_ROWS",
                body=data
            ).execute()
            return True
        except Exception as e:
            print("Google Spread Sheet Error:",e.args[0])
            return False
        except:
            return False