def clean_columns(df):
    """Estandariza nombres de columnas"""
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df
