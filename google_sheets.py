from googleapiclient.discovery import build
from google.oauth2 import service_account


class gsheets():

    def __init__(self,Id):
        """
        

        Parameters
        ----------
        Id : str
            ID represents the sheet Id that can be possibly noted down 
            from the url when a google sheet is opened in the browser.

        Returns
        -------
        None.

        """
        service_account_file = 'credentials.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        credentials = None
        credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes = SCOPES)
        service = build('sheets', 'v4', credentials=credentials)
        # Call the Sheets API
        self.sheet = service.spreadsheets()
        self.SAMPLE_SPREADSHEET_ID = Id
        
    def sheet_read(self,read_range):
        """
        

        Parameters
        ----------
        read_range : str
            read_range refers to the range of cells that are intended to scrape 
            for reading.

        Returns
        -------
        Returns the content in the cells from the range provided.

        """
        self.SAMPLE_RANGE_NAME = read_range
        result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                    range=self.SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        return(values)
    
    def sheet_write(self,values,write_range):
        """
        

        Parameters
        ----------
        values : str
            content to be written onto the sheets.
        write_range : str
            range of cells that are intended to be written with the content provided.

        Returns
        -------
        None.

        """
        self.wr = write_range
        self.vals = values
        request = self.sheet.values().update(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, 
            range= self.wr, valueInputOption='USER_ENTERED', body={'values':self.vals}).execute()
        return()

