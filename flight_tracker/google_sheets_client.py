import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GoogleSheetsClient:

  SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

  def __init__(self, token_path='token.json', creds_path='credentials.json'):
    self.token_path = token_path
    self.creds_path = creds_path
    self.creds = self.get_credentials()
    self.service = build('sheets', 'v4', credentials=self.creds)

  def get_credentials(self):
    creds = None
    if os.path.exists(self.token_path):
      creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
          self.creds_path, self.SCOPES)
        creds = flow.run_local_server(port=0)
      with open(self.token_path, 'w') as token:
        token.write(creds.to_json())
    return creds

  def read_spreadsheet(self, spreadsheet_id, range_name):
    sheet = self.service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id,
                  range=range_name).execute()
    values = result.get('values', [])
    return values

  def write_spreadsheet(self, spreadsheet_id, range_name, values):
    sheet = self.service.spreadsheets()
    body = {
      'values': values
    }
    result = sheet.values().update(
      spreadsheetId=spreadsheet_id, range=range_name,
      valueInputOption='USER_ENTERED', body=body).execute()
    return result

  def append_spreadsheet(self, spreadsheet_id, range_name, values):
    sheet = self.service.spreadsheets()
    body = {
      'values': values
    }
    result = sheet.values().append(
      spreadsheetId=spreadsheet_id, range=range_name,
      valueInputOption='USER_ENTERED', body=body).execute()
    return result

  def clear_spreadsheet(self, spreadsheet_id, range_name):
    sheet = self.service.spreadsheets()
    result = sheet.values().clear(
      spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result

  def create_spreadsheet(self, title):
    spreadsheet = {
      'properties': {
        'title': title
      }
    }
    spreadsheet = self.service.spreadsheets().create(body=spreadsheet,
                                    fields='spreadsheetId').execute()
    return spreadsheet.get('spreadsheetId')

  def delete_spreadsheet(self, spreadsheet_id):
    self.service.spreadsheets().delete(spreadsheetId=spreadsheet_id).execute()
