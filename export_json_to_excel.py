import json
import openpyxl

# Replace with the path to your JSON file
json_file_path = r"C:example.json"

# Read JSON data from file and clean invalid control characters
with open(json_file_path, 'r', encoding='utf-8') as file:
    json_data_str = file.read()

# Remove invalid control characters
cleaned_json_data_str = ''.join(char for char in json_data_str if char.isprintable())

# Load the cleaned JSON data into a dictionary
json_data = json.loads(cleaned_json_data_str)

# Create Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Product Data"

# Write headers for the main sheet
base_headers = [
    'Item No', 'DEFAULT_SKU', 'ATG_DEFAULT_CATEGORY', 'DESCRIPTION_PRODUCT',
    'DESCRIPTION_PRODUCT_SHORT', 'DESCRIPTION_PRODUCT_SHORT_VN', 'PRODUCT_TYPE',
    'MATERIAL', 'INSTALLATION_TYPE'
]
sku_headers = [
    'SKU', 'SKU_ID', 'LIST_PRICE', 'COLOR_FINISH_CODE', 'COLOR_FINISH_NAME',
    'IMG_SWATCH', 'IMG_ITEM_ISO', 'WEB_INCLUDED', 'RETAILER_1_IMG',
    'RETAILER_1_URL', 'RETAILER_2_IMG', 'RETAILER_2_URL'
]

# Dynamically create SKU columns for up to 5 SKUs (adjust as needed)
max_skus = 15  # Adjust based on maximum number of SKUs you expect
dynamic_headers = base_headers + [
    f"{header}_SKU_{i+1}" for i in range(max_skus) for header in sku_headers
]
sheet.append(dynamic_headers)

# Populate Excel with data
for item_id, item_data in json_data.items():
    item_no = item_data.get('itemNo')
    default_sku = item_data.get('attributes', {}).get('DEFAULT_SKU')
    default_category = item_data.get('attributes', {}).get('ATG_DEFAULT_CATEGORY')
    description_product = item_data.get('attributes', {}).get('DESCRIPTION_PRODUCT')
    description_product_short = item_data.get('attributes', {}).get('DESCRIPTION_PRODUCT_SHORT')
    description_product_short_vn = item_data.get('attributes', {}).get('DESCRIPTION_PRODUCT_SHORT_VN')
    product_type = item_data.get('attributes', {}).get('PRODUCT_TYPE')
    material = item_data.get('attributes', {}).get('MATERIAL')
    
    # Safely extract INSTALLATION_TYPE
    installation_type_data = item_data.get('attributes', {}).get('INSTALLATION_TYPE', {})
    installation_type = ', '.join(installation_type_data.values()) if isinstance(installation_type_data, dict) else installation_type_data

    # Start building row data
    row_data = [
        item_no, default_sku, default_category, description_product,
        description_product_short, description_product_short_vn, product_type,
        material, installation_type
    ]

    # Process SKUs
    skus = item_data.get('skus', [])
    for i in range(max_skus):
        if i < len(skus):
            sku_data = skus[i]
            sku = sku_data.get('sku', '')
            sku_id = sku_data.get('id', '')
            sku_attributes = sku_data.get('skuAttributes', {})
            list_price = sku_attributes.get('LIST_PRICE', '')
            color_finish_code = sku_attributes.get('COLOR_FINISH_CODE', '')
            color_finish_name = sku_attributes.get('COLOR_FINISH_NAME', '')
            img_swatch = sku_attributes.get('IMG_SWATCH', '')
            img_item_iso = sku_attributes.get('IMG_ITEM_ISO', '')
            web_included = sku_attributes.get('WEB_INCLUDED', '')
            retailer_1_img = sku_attributes.get('RETAILER_1_IMG', '')
            retailer_1_url = sku_attributes.get('RETAILER_1_URL', '')
            retailer_2_img = sku_attributes.get('RETAILER_2_IMG', '')
            retailer_2_url = sku_attributes.get('RETAILER_2_URL', '')

            row_data.extend([
                sku, sku_id, list_price, color_finish_code, color_finish_name,
                img_swatch, img_item_iso, web_included, retailer_1_img,
                retailer_1_url, retailer_2_img, retailer_2_url
            ])
        else:
            # Fill empty columns if fewer SKUs exist
            row_data.extend([''] * len(sku_headers))

    # Append the row to the sheet
    sheet.append(row_data)

# Save Excel file
excel_file_path = r'C:example.xlsx'
workbook.save(excel_file_path)

print(f"Successfully created and saved Excel file: {excel_file_path}")
