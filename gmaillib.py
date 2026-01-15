import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage
import base64

from dotenv import load_dotenv

load_dotenv()
SCOPES = os.getenv('SCOPES')
# If modifying these scopes, delete the file token.json.

TOKEN_FILE = os.getenv('TOKEN_FILE')
CREDENTIALS_FILE = os.getenv('CREDENTIALS_FILE')

def get_gmail_service(scopes = SCOPES, token_file = TOKEN_FILE, credentials_file = CREDENTIALS_FILE):
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  print(token_file)
  if os.path.exists(token_file):
    creds = Credentials.from_authorized_user_file("token.json", scopes)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          credentials_file, scopes
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(token_file, "w") as token:
      token.write(creds.to_json())

    # Call the Gmail API
  service = build("gmail", "v1", credentials=creds)
  return service

# Build message body
def build_message(sender, to, subject, body_html):
    
    message = EmailMessage()
    message['To'] = to
    message['From'] = sender
    message['Subject'] = subject    
    message.add_alternative(body_html, subtype='html', charset='utf-8')
    return message

# Build draft on gmail
def send_message(service, message):
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    create_message = {
        'message': {
            'raw': encoded_message   
        }
    }
    draft = service.users().drafts().create(userId = "me",
                                            body = create_message).execute()
    service.users().drafts().send(body = {'id': draft['id']}, userId = 'me').execute()

    return draft
