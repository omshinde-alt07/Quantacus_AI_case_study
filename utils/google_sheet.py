import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly"
]

REQUIRED_COLUMNS = {
    "Product Id",
    "image_url",
    "original_price",
    "sale_price",
}


#reading google sheet 

def get_sheet_dataframe(
    service_account_path,
    spreadsheet_id,
    worksheet_name,
):

    credentials = Credentials.from_service_account_file(
        service_account_path,
        scopes=SCOPES,
    )

    client = gspread.authorize(credentials)

    worksheet = (
        client
        .open_by_key(spreadsheet_id)
        .worksheet(worksheet_name)
    )

    df = pd.DataFrame(
        worksheet.get_all_records()
    )

    missing = REQUIRED_COLUMNS - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {', '.join(sorted(missing))}"
        )

    return df