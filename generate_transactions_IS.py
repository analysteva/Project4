import pandas as pd
import random
from datetime import datetime, timedelta

rate = 1.08
num_transactions = 10
account_keys = {
    "Revenue": [101, 102, 103],
    "COGS": [124],
    "Operating Expenses": [114, 115, 116, 117, 118, 119, 120],
    "Amortization": [122],
    "Depreciation": [121],
    "Interests": [126],
    "Tax": [125]
}

columns = ["Source Name", "OrganizationKey", "Date", "Mapping", "Gross Sales", "Rate", "USD Amount", "Account Key"]
all_records = []

for month in range(1, 13):  # January to December 2022
    for i in range(num_transactions):
        transaction_date = datetime(2022, month, 1) + timedelta(days=random.randint(0, 27))
        date_str = transaction_date.strftime("%d/%m/%Y")
        file_date_str = transaction_date.strftime("%Y-%m-%d")

        def add_record(source, amount, key):
            usd = round(amount * rate, 2)
            all_records.append([f"{file_date_str} {source}.csv", 1, date_str, "Income Statement", amount, rate, usd, key])

        add_record("Revenue", int(random.randint(3000, 20000) * 1.05), random.choice(account_keys["Revenue"]))
        add_record("COGS", int(random.randint(1000, 5000) * 1.05), account_keys["COGS"][0])
        add_record("Operating expences", int(random.randint(100, 1000) * 1.05), random.choice(account_keys["Operating Expenses"]))
        add_record("Amortization", int(random.randint(200, 600) * 1.05), account_keys["Amortization"][0])
        add_record("Depreciation", int(random.randint(300, 800) * 1.05), account_keys["Depreciation"][0])
        add_record("Interests", int(random.randint(50, 200) * 1.05), account_keys["Interests"][0])
        add_record("Tax", int(random.randint(100, 500) * 1.05), account_keys["Tax"][0])

df = pd.DataFrame(all_records, columns=columns)
df.to_excel("IS_Trans_Jan_Dec_2022.xlsx", index=False)
print("✅ File saved as 'IS_Trans_Jan_Dec_2022.xlsx'")
