import pandas as pd

import re
import pandas as pd

# Regex para fechas con o sin hora
DATE_REGEX = re.compile(r"""
^(
    \d{4}[-/]\d{2}[-/]\d{2}      # YYYY-MM-DD o YYYY/MM/DD
    |
    \d{2}[-/]\d{2}[-/]\d{4}      # DD-MM-YYYY o DD/MM/YYYY
)
(                                 # Opcional: hora
    \s+                           # espacio
    \d{2}:\d{2}                   # HH:MM
    (:\d{2})?                     # opcional: :SS
)?$
""", re.VERBOSE)

def detect_column_types(df):
    """Detecta el tipo de columnas de un DataFrame"""
    types = {}
    for col in df.columns:
        dtype = df[col].dtype

        if pd.api.types.is_numeric_dtype(dtype):
            types[col] = "numeric"

        elif pd.api.types.is_datetime64_any_dtype(dtype):
            types[col] = "datetime64"

        elif pd.api.types.is_string_dtype(dtype):
            # Verificar si la mayoría de los valores parecen fechas
            sample = df[col].dropna().astype(str).head(20)  # muestra de hasta 20 valores no nulos
            if all(DATE_REGEX.match(v.strip()) for v in sample if v.strip() != "") and not sample.empty:
                types[col] = "datetime"
            else:
                types[col] = "string"

        else:
            types[col] = "string"

    return types


def date_formatter(df,column):
    """Convertir columnas con cadena de texto a formato datetime."""
    df_copy = df.copy()
    output_format = "%Y-%m-%d"
    date_series = pd.to_datetime(df_copy[column], errors='coerce')
    df_copy[column] = date_series.dt.strftime(output_format).where(date_series.notna())
    return df_copy

def parse_columns(df,columns_values):
    """Verifica que las columnas cunplan con el formato establecido y formatea conforme al distinto tipo de dato."""
    df_copy = df.copy()
    types = columns_values["tipo"]
    for i,col in enumerate(df_copy.columns):
        if types[i] == "datetime":
            df_copy = date_formatter(df_copy,col)
        elif types[i] == "numeric":
            print("a")


    return df_copy