from typing import Optional

import pandas as pd
from loguru import logger


def load_data(
    data_path: Optional[str] = "./testdaten/testdaten-excel.xlsx",
) -> pd.DataFrame | None:
    # Define the needed columns for the report creation
    df_entries = [
        "Woche",
        "Datum",
        "Gesamtverkäufe (€)",
        "Kosten (€)",
        "Anzahl der Verkäufe",
        "Rückgaben (€)",
        "Beschädigte Ware (€)",
    ]

    # Read the Excel file
    df = pd.read_excel(data_path)

    if len(df) == 0:
        logger.critical("No data found or empty excel file")
        return None

    # Check if all required columns are present
    missing_columns = [col for col in df_entries if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Select only the required columns, if more are provided they are ignored
    df = df[df_entries]

    # Get dates of rows with missing values
    rows_with_na = df[df.isna().any(axis=1)]
    if not rows_with_na.empty:
        logger.warning(
            f"Found rows with missing values for dates: {rows_with_na['Datum'].tolist()}"
        )

    return df


def load_test_data(
    data_path: Optional[str] = "./testdaten/testdaten.csv",
) -> pd.DataFrame | None:
    # Define the needed columns for the report creation
    df_entries = [
        "Woche",
        "Datum",
        "Gesamtverkäufe (€)",
        "Kosten (€)",
        "Anzahl der Verkäufe",
        "Rückgaben (€)",
        "Beschädigte Ware (€)",
    ]

    # Read the Excel file
    df = pd.read_csv(data_path)

    if len(df) == 0:
        logger.critical("No data found or empty excel file")
        return None

    # Check if all required columns are present
    missing_columns = [col for col in df_entries if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Select only the required columns, if more are provided they are ignored
    df = df[df_entries]

    # Get dates of rows with missing values
    rows_with_na = df[df.isna().any(axis=1)]
    if not rows_with_na.empty:
        logger.warning(
            f"Found rows with missing values for dates: {rows_with_na['Datum'].tolist()}"
        )

    return df
