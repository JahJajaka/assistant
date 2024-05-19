from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path
import csv
from datetime import datetime, timedelta

# If modifying these SCOPES, delete the file etl/token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds_path = "creds_web.json"
    token_path = "token.json"
    """Authenticate the Gmail API and return the service."""
    creds = None
    # The file etl/token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_path, SCOPES)
            creds = flow.run_local_server()
            #creds = flow.run_console()
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service


def save_historical_messages(service, email_address, csv_filename):
    """List messages in a specific email address from the last 7 days and save them to a CSV file."""
    # Calculate date 7 days ago formatted as 'YYYY/MM/DD'
    date_query = (datetime.now() - timedelta(days=7)).strftime('%Y/%m/%d')
    
    # Get messages from the last 7 days
    results = service.users().messages().list(userId='me', q=f'after:{date_query}', maxResults=500).execute()
    messages = results.get('messages', [])
    
    if not messages:
        print(f'No messages found in {email_address} for the last 7 days.')
    else:
        with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date Received', 'From', 'Subject', 'Snippet'])
            
            print(f'Messages in {email_address} from the last 7 days:')
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
                
                # Extract headers for 'From', 'Date', and 'Subject'
                headers = msg['payload']['headers']
                date_received = next((header['value'] for header in headers if header['name'] == 'Date'), None)
                from_who = next((header['value'] for header in headers if header['name'] == 'From'), None)
                subject = next((header['value'] for header in headers if header['name'] == 'Subject'), None)
                snippet = msg.get('snippet', '')
                
                writer.writerow([date_received, from_who, subject, snippet])
                print(f"Message snippet: {snippet}")

def main():
    service = authenticate_gmail()
    email_address = 'r2e4d6@example.com'
    save_historical_messages(service, email_address, f"emails_{datetime.now().strftime('%Y_%m_%d')}.csv")

if __name__ == '__main__':
    main()