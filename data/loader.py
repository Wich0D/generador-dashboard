import pandas as pd

def load_data(file):
    """Carga CSV o Excel en un DataFrame"""
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    elif file.name.endswith(".xlsx") or file.name.endswith(".xls"):
        return pd.read_excel(file)
    else:
        raise ValueError("Formato no soportado. Usa CSV o Excel.")
