import pandas as pd

def detect_column_types(df):
    """Detecta el tipo de columnas de un DataFrame"""
    types = {}
    for col in df.columns:
        dtype = df[col].dtype

        if pd.api.types.is_numeric_dtype(dtype):
            types[col] = "numeric"
        elif pd.api.types.is_string_dtype(dtype):
            types[col] = "string"
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            types[col] = "datetime64"
        else:
            types[col] = "string"
    print(types)
    return types