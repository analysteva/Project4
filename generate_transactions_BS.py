import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)

# Define account details
accounts = [
    ('Cash', 200),
    ('Accounts Receivable', 201),
    ('Inventory', 202),
    ('Investments for Sale', 205),
    ('Equipment', 206),
    ('Plant', 207),
    ('Property', 208),
    ('Accounts Payable', 210),
    ('Bonds', 211),
    ('Long Term Debt', 212),
    ('Share Capital', 220),
    ('Retained Earnings', 221),
    ('Other Reservers', 222)
]

# Generate data for each day from Jan 1 to Dec 31, 2022
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

records = []
current_date = start_date

while current_date <= end_date:
    for account_name, account_key in accounts:
        base_amount = random.randint(3000, 20000)
        local_amount = int(base_amount * 1.05)  # ~5% higher
        usd_amount = round(local_amount * 1.08, 2)
        record = {
            'Source Name': f"{current_date.strftime('%d/%m/%Y')} {account_name}.csv",
            'OrganizationKey': 1,
            'Date': current_date.strftime('%d/%m/%Y'),
            'Mapping': 'Balance Sheet',
            'Gross Sales': local_amount,
            'Rate': 1.08,
            'USD Amount': usd_amount,
            'Account Key': account_key
        }
        records.append(record)
    current_date += timedelta(days=1)

# Create DataFrame and save to Excel
df = pd.DataFrame(records, columns=[
    'Source Name', 'OrganizationKey', 'Date', 'Mapping',
    'Gross Sales', 'Rate', 'USD Amount', 'Account Key'
])

df.to_excel("BS_Trans_Jan_Dec_2022.xlsx", index=False)
print("✅ File saved as 'BS_Trans_Jan_Dec_2022.xlsx'")
