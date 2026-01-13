import pandas as pd
import json

# Load Excel sheet into a DataFrame
excel_file = 'D:checklist-ap.xlsx'
df_excel = pd.read_excel(excel_file, sheet_name='Sheet1')

# Load JSON file
json_file = r"D:Product_Data.json"
with open(json_file, 'r', encoding='utf-8') as f:
    product_data = json.load(f)
    
def check_sku_id_from_excel():
    if 'Product_ID' in df_excel.columns:
        product_ids = df_excel['Product_ID'].tolist()
        
        for product_id in product_ids:
            row = df_excel[df_excel['Product_ID'] == product_id]
            if not row.empty:
                print("Product found in Excel file.")
                default_sku = row['DEFAULT_SKU'].values[0]
                print("Default SKU:", default_sku)
                
                product_info = product_data.get(product_id)
                if product_info:
                    skus = product_info['skus']
                    for sku in skus:
                        sku_id = sku['sku']
                        print("SKU ID:", sku_id)
                        if sku_id == default_sku:
                            print("This SKU matches the default SKU.")
                        else:
                            print("This SKU does not match the default SKU.")
                else:
                    print("Product ID not found in JSON data.")
            else:
                print("Product ID", product_id, "not found in Excel file.")
    else:
        print("Column 'Product_ID' not found in the Excel file.")

# Test the function
check_sku_id_from_excel()
