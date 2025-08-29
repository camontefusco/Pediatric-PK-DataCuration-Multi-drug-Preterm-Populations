# Pediatric PK Data Repository - Comprehensive Project Report

## 1. Executive Summary

The Pediatric PK Data Repository aggregates and harmonizes pediatric pharmacokinetic (PK) data for six model drugs (midazolam, morphine, gentamicin, metoprolol, zidovudine, simvastatin) across neonates, infants, children, adolescents, and adults. The goal is to create a modular, reproducible, and EMA-aligned dataset suitable for pediatric PBPK modeling. Key conclusions include the availability of multi-age group PK data, coverage across multiple elimination pathways, and derivation of PBPK-ready inputs, including polypharmacy scenarios.

---

## 2. Data Sources

| Study ID                         | Drug        | Source File           | Pathway                   | Elimination   | Formulation | Notes                            |
| -------------------------------- | ----------- | --------------------- | ------------------------- | ------------- | ----------- | -------------------------------- |
| genta\_neonate\_2013\_agg        | gentamicin  | gentamicin\_raw\.csv  | renal                     | renal         | iv          | Neonatal clearance               |
| metoprolol\_fda\_bpca\_agg       | metoprolol  | metoprolol\_raw\.csv  | CYP2D6 hepatic metabolism | hepatic/renal | oral        | Pediatric summary Cmin/Cmax      |
| vet\_et\_al\_2014\_agg           | midazolam   | midazolam\_raw\.csv   | CYP3A4 hepatic metabolism | hepatic       | iv          | Critically ill neonates/children |
| morph\_iv\_surgery\_1998\_agg    | morphine    | morphine\_raw\.csv    | UGT2B7 hepatic metabolism | hepatic       | iv          | Postoperative infants            |
| simva\_pbpk\_children\_2019\_agg | simvastatin | simvastatin\_raw\.csv | hepatic/biliary           | hepatic       | oral        | Children/adolescents PBPK model  |
| zidovudine\_preterm\_2005\_agg   | zidovudine  | zidovudine\_raw\.csv  | UGT/renal                 | hepatic/renal | oral        | Preterm neonates                 |

Sources include literature, FDA/EMA reports, and supplementary tables. Patient-level data was extracted where available.

---

## 3. Data Processing Workflow

1. **Metadata Fetching:** `0_fetch_and_store_metadata.py` extracted study-level information.
2. **Data Cleaning:** `1_data_cleaning.py` harmonized column names, units, and removed duplicates.
3. **Harmonization:** `2_data_harmonization.ipynb` standardized age, route, pathway, and units.
4. **PBPK Input Preparation:** `4_pbpk_input_preparation.ipynb` assigned age groups and generated PBPK-ready inputs.
5. **Polypharmacy Inputs:** `6_polypharmacy_pbpk_inputs.ipynb` flagged subjects with multiple drugs and prepared multi-drug PBPK input tables.

Decisions included handling missing values (NA), averaging group-level clearance for individual simulations, and assigning unknown age groups where age\_years missing.

---

## 4. Data Overview

* Harmonized master dataset (`pediatric_pk_master_harmonized.csv`) includes columns: study\_id, drug, subject\_id, age\_years, age\_days, weight\_kg, cl\_l\_per\_h\_per\_kg, t\_half\_h, route, pathway, aggregated\_row, notes, source, source\_file, age\_group\_pbpk, polypharmacy.
* Age group coverage, route coverage, and pathway coverage were summarized in regulatory tables and visualized as heatmaps and barplots.

### Figures

* **Age Group Coverage Heatmap**: illustrates subject counts per drug and pediatric age group.
* **Route Coverage Bar Plot**: shows IV vs oral data per drug.
* **Elimination Pathway Heatmap**: visualizes distribution of metabolic/renal pathways per drug.

---

## 5. PBPK Inputs

* Single-drug inputs: average PK parameters per age group and drug.
* Polypharmacy inputs: flagged subjects with multiple drugs, mean CL and weight.
* Saved under `/data/curated/pbpk_inputs/` for single-drug and `/polypharmacy/` for multi-drug scenarios.
* Columns required for PBPK simulations: age\_group\_pbpk, weight\_kg, cl\_l\_per\_h\_per\_kg, t\_half\_h, route, pathway.

Assumptions: For group-level data without subject IDs, multiple rows were expanded to simulate individual-level PBPK input.

---

## 6. EMA Alignment

* Dataset covers multiple age groups (preterm neonate → adult).
* Includes multiple elimination pathways (hepatic, renal, CYP, UGT).
* Formulations include IV and oral.
* Polypharmacy scenarios prepared for multi-drug simulations.
* Limitations: some drugs have sparse data in certain age groups, assumptions made for group-level data.

---

## 7. Usability

* **PBPK simulations:** ready for Simcyp, PK-Sim, or GastroPlus. CSVs can be imported directly.
* **Exploratory analysis:** notebooks allow filtering by drug, age, and pathway.
* **Regulatory submission:** summary tables and figures provide coverage documentation.
* Notebooks are modular and can be re-run from raw data.

---

## 8. Conclusions

* Harmonization enables consistent analysis across drugs and age groups.
* PBPK-ready inputs facilitate both single-drug and polypharmacy simulations.
* The dataset meets EMA pediatric PBPK objectives and can support regulatory submissions.
* Future work could include additional drugs, critically ill populations, and extended polypharmacy modeling.

---

## 9. Appendices

* Metadata file: `/data/raw/metadata.csv`
* Data dictionary: `/data/curated/data_dictionary.md`
* Scripts and notebooks for processing and analysis.
* Source references for each drug/study.
