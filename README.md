# Pediatric PK Data Repository – Multi-Drug Preterm Populations

## Overview
This project builds a **curated pediatric PK data repository** for neonates, infants, children, and adults, supporting downstream PBPK modeling and EMA-aligned evaluation.

## Objective
Aggregate and organize pediatric PK data for Voriconazole (CYP2C19), Levetiracetam (renal), Clopidogrel (prodrug), and Etanercept (biologic), including **preterm neonates** and multiple formulations (oral, IV).

## Tools
- Python / R for data cleaning, aggregation, and visualization
- pandas, numpy, matplotlib, seaborn (Python)
- tidyverse, ggplot2 (R)

## Innovation / Twists
- Inclusion of **preterm neonates**
- Multiple **formulations** (oral suspension, capsule, IV)
- Polypharmacy scenarios
- Metadata includes **age, weight, route, elimination pathway, enzyme involvement**

## Deliverables
- `/data/curated_pediatric_pk.csv`
- `/data/DATA_DICTIONARY.md`
- `/analysis/exploratory_analysis.ipynb` with plots for dataset coverage by age, route, and pathway

## EMA Alignment
Supports **Stage 1**: data aggregation and preparation for pediatric PBPK modeling.
