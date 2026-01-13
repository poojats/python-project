import pandas as pd
import json
import os

# Load the JSON data from the "data.json" file
with open(r"D:example.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

# Create empty lists to store the data
item_nos = []
atg_default_categories = []
ancestor_ids = []

# Iterate through all products in the JSON data
for product_id, product_info in json_data.items():
    item_no = product_info.get("itemNo", "")
    atg_default_category = product_info["attributes"].get("ATG_DEFAULT_CATEGORY", "")
    
    ancestors = product_info.get("ancestors", [])
    ancestor_id = ancestors[0] if ancestors else None  # Set ancestor_id to None if "ancestors" is empty

    # Append the data to the respective lists
    item_nos.append(item_no)
    atg_default_categories.append(atg_default_category)
    ancestor_ids.append(ancestor_id)

# Create a DataFrame to store the data
result_df = pd.DataFrame({
    "Item No": item_nos,
    "ATG Default Category": atg_default_categories,
    "Ancestor ID": ancestor_ids
})

# Specify the output file path
output_file_path = r"D:example.xlsx"

# Export the results to an Excel file
result_df.to_excel(output_file_path, index=False)

# Check if the file was successfully created
if os.path.exists(output_file_path):
    print(f"Data has been saved to {output_file_path}")
else:
    print("An error occurred while saving the data.")
