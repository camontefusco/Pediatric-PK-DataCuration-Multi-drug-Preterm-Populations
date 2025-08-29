# Pediatric PK Data Repository - Data Dictionary

This data dictionary describes all columns in the harmonized and PBPK-ready pediatric PK dataset.

| Column                    | Description                                | Units      | Notes                                                                                     |
| ------------------------- | ------------------------------------------ | ---------- | ----------------------------------------------------------------------------------------- |
| study\_id                 | Unique identifier for the study            | string     | Matches `metadata.csv` entry                                                              |
| drug                      | Drug name                                  | string     | One of: midazolam, morphine, gentamicin, metoprolol, zidovudine, simvastatin              |
| subject\_id               | Unique subject identifier                  | string     | Generated if original data aggregated; empty if group-level only                          |
| age\_years                | Age of the subject in years                | years      | Converted from age\_days if necessary                                                     |
| age\_days                 | Age of the subject in days                 | days       | Used for precise neonatal age assignment                                                  |
| weight\_kg                | Body weight                                | kg         | Average weight if group-level data                                                        |
| cl\_l\_per\_h\_per\_kg    | Clearance normalized by weight             | L/h/kg     | Derived from study or calculated from CL and weight                                       |
| t\_half\_h                | Half-life                                  | hours      | Optional, missing if not reported                                                         |
| route                     | Route of administration                    | string     | As reported in the study (iv, oral, etc.)                                                 |
| pathway                   | Elimination pathway                        | string     | As reported: renal, hepatic, CYP, UGT, etc.                                               |
| aggregated\_row           | Flag if row represents group-level summary | TRUE/FALSE | TRUE if originally reported as group summary                                              |
| notes                     | Additional information                     | string     | Study-specific or data-specific notes                                                     |
| source                    | Source reference                           | string     | Full citation or URL                                                                      |
| source\_file              | Raw CSV filename                           | string     | Matches `/data/raw/` file name                                                            |
| age\_group\_pbpk          | Pediatric age group                        | string     | Preterm neonate, term neonate, infant, child, adolescent, adult. Generated for PBPK input |
| polypharmacy              | Flag for multiple drugs administered       | TRUE/FALSE | TRUE if subject has more than one drug in dataset                                         |
| cl\_l\_per\_h             | Clearance in L/h                           | L/h        | Calculated from weight-normalized clearance                                               |
| cl\_ml\_per\_min\_per\_kg | Clearance in mL/min/kg                     | mL/min/kg  | Optional, derived from cl\_l\_per\_h\_per\_kg                                             |
| cmin\_ng\_per\_ml         | Minimum concentration                      | ng/mL      | Optional, reported in some studies                                                        |
| cmax\_mg\_per\_l          | Maximum concentration                      | mg/L       | Optional, reported in some studies                                                        |
| auc\_mg\_h\_per\_l        | Area under curve                           | mg\*h/L    | Optional, reported in some studies                                                        |
| dose\_mg                  | Administered dose                          | mg         | Optional, used for PBPK scaling                                                           |
| visit                     | Visit or sampling time                     | string     | Optional, extracted from source if available                                              |

**Notes:**

* Columns `age_group_pbpk` and `polypharmacy` were generated during PBPK input preparation.
* Missing values are represented as NA.
* Group-level data rows were expanded to simulate individual subjects for PBPK simulations.
* This dictionary applies to both `/data/curated/pediatric_pk_master_harmonized.csv` and PBPK-ready input tables in `/pbpk_inputs/`.
