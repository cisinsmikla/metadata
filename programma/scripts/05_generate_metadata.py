import pandas as pd
import json


df = pd.read_csv('../output/final_names_fixed.csv')
print("Dati ielādēti:", df.shape)

def map_dtype(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return 'integer'
    elif pd.api.types.is_float_dtype(dtype):
        return 'float'
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return 'date'
    else:
        return 'string'

descriptions = {
    'Patient_Name': 'Pacienta pilns vārds',
    'Blood_Group': 'Asins grupa',
    'Medical_Condition': 'Hroniska slimība vai diagnoze',
    'Age': 'Pacienta vecums (gados)',
    'Medication': 'Izrakstītās zāles',
    'Gender': 'Pacienta dzimums',
    'Date_of_Birth': 'Dzimšanas datums' 
}

metadata = {}
for col in df.columns:
    metadata[col] = {
        'type': map_dtype(df[col].dtype),
        'description': descriptions.get(
            col,
            f"Lauks: {col.replace('_', ' ')} (automātiski ģenerēts)"
        )
    }

with open('../output/metadata.json', 'w', encoding='utf-8') as f:
    json.dump(metadata, f, ensure_ascii=False, indent=4)

print("✅ Metadati saglabāti: output/metadata.json")
