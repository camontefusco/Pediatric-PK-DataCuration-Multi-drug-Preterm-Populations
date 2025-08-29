# Pediatric PK Data Repository

## Overview

This repository aggregates, harmonizes, and curates pediatric pharmacokinetic (PK) data for six model drugs: midazolam, morphine, gentamicin, metoprolol, zidovudine, and simvastatin. The dataset spans neonates, infants, children, adolescents, and adults, and is prepared for PBPK modeling, including polypharmacy scenarios. The repository is designed to support regulatory submissions and EMA pediatric PBPK qualification objectives.

## Folder Structure

```
/data/raw/                 # Original raw CSVs and metadata
/data/curated/             # Harmonized master dataset
/data/curated/pbpk_inputs/ # PBPK-ready input tables, including polypharmacy
/data/curated/pbpk_inputs/polypharmacy/ # Polypharmacy PBPK input CSVs
/data/curated/regulatory_summary/ # Coverage tables per drug and age group
/figures/                  # Figures (EDA, regulatory, PBPK visualization)
/notebooks/                # Analysis and data preparation notebooks
/scripts/                  # Python scripts for processing
/docs/                     # Reports and documentation (data sources, data dictionary)
```

## Notebooks and Scripts

* `0_fetch_and_store_metadata.py`: Extract study metadata and create `metadata.csv`
* `1_data_cleaning.py`: Clean raw datasets, harmonize units and columns
* `2_data_harmonization.ipynb`: Standardize age, route, pathway, and units; merge datasets
* `3_generate_figures.ipynb`: Create exploratory figures for single drugs
* `4_pbpk_input_preparation.ipynb`: Prepare PBPK-ready input tables for single-drug scenarios
* `5_regulatory_summary_figures.ipynb`: Generate regulatory summary figures (age coverage, routes, pathways)
* `6_polypharmacy_pbpk_inputs.ipynb`: Generate PBPK inputs for subjects with multiple drugs

## Data Files

* `/data/raw/metadata.csv`: Metadata for all studies
* `/data/curated/pediatric_pk_master_harmonized.csv`: Harmonized dataset
* `/data/curated/pbpk_inputs/`: PBPK-ready tables for single-drug modeling
* `/data/curated/pbpk_inputs/polypharmacy/`: PBPK-ready polypharmacy input CSVs

  * `pbpk_polypharmacy_inputs.csv` – all subjects with multiple drugs
  * `pbpk_polypharmacy_preterm_neonate.csv` – preterm neonates
  * `pbpk_polypharmacy_term_neonate.csv` – term neonates
  * `pbpk_polypharmacy_infant.csv` – infants
  * `pbpk_polypharmacy_child.csv` – children
  * `pbpk_polypharmacy_adolescent.csv` – adolescents
* `/data/curated/regulatory_summary/`: Tables summarizing age group, route, and elimination pathway coverage

## Usage

1. Clone the repository.
2. Ensure all required Python packages are installed (see `requirements.txt`).
3. Run notebooks in order: `0` → `1` → `2` → `3` → `4` → `5` → `6` to reproduce data cleaning, harmonization, figures, and PBPK inputs.
4. Explore figures and tables in `/figures/` and `/data/curated/regulatory_summary/`.
5. PBPK-ready CSVs in `/pbpk_inputs/` can be imported into platforms such as Simcyp, PK-Sim, or GastroPlus.

## EMA Alignment

* Age coverage: preterm neonates → adults
* Elimination pathways: hepatic, renal, CYP, UGT
* Formulations: IV and oral
* Polypharmacy scenarios prepared

## Optional Extensions

* Additional drugs and critically ill populations
* Extended polypharmacy modeling
* Integration scripts for PBPK platforms

## References and Documentation

* See `/docs/raw_data_sources.md` for detailed source information.
* See `/docs/data_dictionary.md` for full description of all dataset columns.
* Figures and tables provide coverage and summary analyses.

## 📬 Contact
Carlos Montefusco
📧 cmontefusco@gmail.com
🔗 GitHub: /camontefusco
