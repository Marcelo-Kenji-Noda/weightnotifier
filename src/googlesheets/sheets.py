from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os.path

from config import get_config

def get_credentials(config):
    HOME = os.path.dirname(os.path.relpath(__file__))
    creds = None
    if os.path.exists(os.path.join(HOME,config['paths']['token'])):
        creds = Credentials.from_authorized_user_file(
            os.path.join(HOME,config['paths']['token']),
            config['api']['scopes']
        )
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join(HOME,config['paths']['credentials']), config['api']['scopes'])
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(os.path.join(HOME,config['paths']['token']), 'w') as token:
            token.write(creds.to_json())
    return creds

def get_values():
    config = get_config()
    creds = get_credentials(config)
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=config['sheets']['sheet_id'],
            range=config['sheets']['range']).execute()
        values = result.get('values', [])
        if not values:
            print('No data found.')
            return
        return values
    except HttpError as err:
        print(err)