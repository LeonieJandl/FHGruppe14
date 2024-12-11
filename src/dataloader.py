import pandas
import logging
from typing import Optional
from loguru import logger

def load_data(data_path: Optional[str] = "./testdaten/testdaten-excel.xlsx") -> pandas.DataFrame:
    df_entries = ["Woche",
            "Datum",
            "Gesamtverkäufe (€)",
            "Kosten (€)",
            "Anzahl der Verkäufe",
            "Rückgaben (€)",
            "Beschädigte Ware (€)"
            ]

    df = pandas.read_excel(data_path, usecols=df_entries)
    
    # Store original number of rows
    original_rows = len(df)
    
    # Get dates of rows with missing values
    rows_with_na = df[df.isna().any(axis=1)]
    if not rows_with_na.empty:
        logger.warning(f"Found rows with missing values for dates: {rows_with_na['Datum'].tolist()}")
    
    if len(df) == 0:
        logger.critical("No data found or empty excel file")
        return None

    return df