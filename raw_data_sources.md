# Pediatric PK Data Repository – Raw Data Sources

## 1. Overview

This report documents the origin of all raw datasets included in the Pediatric PK Data Repository, including literature sources, regulatory reports, and supplementary tables. It describes how the data were collected, patient populations, age ranges, formulations, and elimination pathways.

---

## 2. Raw Datasets Summary

| Study ID                         | Drug        | Source                   | Type                | Age Range            | Formulation | Elimination Pathway | Notes                                                                     |
| -------------------------------- | ----------- | ------------------------ | ------------------- | -------------------- | ----------- | ------------------- | ------------------------------------------------------------------------- |
| genta\_neonate\_2013\_agg        | gentamicin  | PMC3948203               | Supplementary table | Neonates             | IV          | Renal               | Neonatal clearance, critically ill patients                               |
| metoprolol\_fda\_bpca\_agg       | metoprolol  | FDA BPCA Pediatric Label | Summary table       | Infants to children  | Oral        | Hepatic/CYP2D6      | Cmin/Cmax values reported, pediatric PK summary                           |
| vet\_et\_al\_2014\_agg           | midazolam   | PMC3948203               | Literature          | Neonates & Children  | IV          | Hepatic/CYP3A4      | Critically ill population, median clearance                               |
| morph\_iv\_surgery\_1998\_agg    | morphine    | Anesth Analg 1998        | Supplementary table | Infants              | IV          | Hepatic/UGT2B7      | Postoperative subjects, group-level data expanded to simulate individuals |
| simva\_pbpk\_children\_2019\_agg | simvastatin | PBPK publication         | Literature          | Children/Adolescents | Oral        | Hepatic/Biliary     | PBPK modeling input, population-based data                                |
| zidovudine\_preterm\_2005\_agg   | zidovudine  | Literature               | Supplementary table | Preterm neonates     | Oral        | Hepatic/Renal       | Data extracted from preterm neonatal population                           |

---

## 3. Data Acquisition Notes

* **Literature sources:** Downloaded PDFs and supplementary tables; patient-level data extracted when available.
* **Regulatory sources:** FDA Pediatric Labeling (BPCA) PDFs, EMA reports; PK summary tables digitized.
* **Data formatting:** Converted to CSV files in `/data/raw/` with original columns preserved; additional metadata captured in `metadata.csv`.
* **Special handling:** Group-level summaries were expanded into individual-level rows to support PBPK simulations; missing values noted as NA.

---

## 4. References

1. Vet et al., 2014 – PMC3948203 – Midazolam PK in neonates and children
2. Anesth Analg, 1998 – Morphine clearance in postoperative infants
3. FDA BPCA Pediatric Label – Metoprolol
4. Simvastatin PBPK publication, 2019
5. Zidovudine preterm neonates, 2005
