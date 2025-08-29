#!/usr/bin/env python3
"""
1_data_cleaning.py
------------------
Script to clean and merge pediatric PK raw data into a curated master dataset.

Inputs:
    /data/raw/*.csv   (drug-specific raw CSVs)

Outputs:
    /data/curated/pediatric_pk_master.csv
    /data/curated/data_dictionary.csv

Usage:
    python scripts/1_data_cleaning.py
"""

import os
import pandas as pd

# Define directories
RAW_DIR = "/data/raw"
CURATED_DIR = "/data/curated"
CURATED_FILE = os.path.join(CURATED_DIR, "pediatric_pk_master.csv")
DATA_DICT_FILE = os.path.join(CURATED_DIR, "data_dictionary.csv")

def main():
    os.makedirs(CURATED_DIR, exist_ok=True)

    # Load all raw CSVs
    dfs = []
    for fn in os.listdir(RAW_DIR):
        if fn.endswith("_raw.csv"):
            fpath = os.path.join(RAW_DIR, fn)
            df = pd.read_csv(fpath)
            df["source_file"] = fn
            dfs.append(df)

    if not dfs:
        raise RuntimeError(f"No raw CSVs found in {RAW_DIR}")

    # Concatenate into one master dataframe
    master = pd.concat(dfs, ignore_index=True)

    # Standardize column names (lowercase, underscores)
    master.columns = [c.lower().strip().replace(" ", "_") for c in master.columns]

    # Save curated master dataset
    master.to_csv(CURATED_FILE, index=False)
    print(f"✅ Curated master dataset saved to {CURATED_FILE}")

    # Build data dictionary
    descriptions = {
        "study_id": "Study identifier (short label)",
        "drug": "Drug name",
        "subject_id": "Unique subject ID if available",
        "visit": "Study visit label if multiple per subject",
        "age_years": "Age in years (float, can be fractional)",
        "age_days": "Age in days (optional, numeric)",
        "age_group": "Reported age group label from study",
        "weight_kg": "Body weight in kg if available",
        "cl_l_per_h_per_kg": "Clearance normalized to kg (L/h/kg)",
        "cl_l_per_h": "Clearance in L/h",
        "cl_ml_per_min_per_kg": "Clearance in mL/min/kg",
        "t_half_h": "Elimination half-life (hours)",
        "cmin_ng_per_ml": "Minimum concentration (ng/mL)",
        "auc_mg_h_per_l": "Area under curve (mg*h/L)",
        "cmax_mg_per_l": "Maximum concentration (mg/L)",
        "dose_mg": "Dose administered (mg)",
        "route": "Route of administration (oral, iv, etc.)",
        "aggregated_row": "True if row represents aggregated group summary expanded into pseudo-patient rows",
        "notes": "Notes on how data was derived",
        "source": "Literature or regulatory source (URL, PubMed ID)",
        "source_file": "Origin raw CSV filename"
    }

    data_dict = []
    for col in master.columns:
        data_dict.append({
            "column": col,
            "dtype": str(master[col].dtype),
            "description": descriptions.get(col, "N/A")
        })

    dd = pd.DataFrame(data_dict)
    dd.to_csv(DATA_DICT_FILE, index=False)
    print(f"✅ Data dictionary saved to {DATA_DICT_FILE}")

if __name__ == "__main__":
    main()
