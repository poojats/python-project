import pandas as pd

# Load the Excel file
file_path = "D:Products.xlsx"
df = pd.read_excel(file_path)

# Ensure your Excel sheet has columns named 'item_no' and 'default_sku'
item_numbers = df['item_no'].tolist()
default_skus = df['default_sku'].tolist()

# Base URL
base_url = "https://www.example.com/productDetails/"

# Generate URLs
urls = [f"{base_url}{item_no}?skuid={skuid}" for item_no, skuid in zip(item_numbers, default_skus)]

# Add URLs to the DataFrame
df['URL'] = urls

# Save the updated DataFrame to a new Excel file
output_file_path = "D:create_URL.xlsx"
df.to_excel(output_file_path, index=False)

print(f"URLs have been written to {output_file_path}")
