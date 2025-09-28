# Replication Package for “The Economic Impact of Uncertainty about U.S. Regulations of the Energy Sector”

**Authors:** Xiaohan Ma & Zhoudan Xie  

---

## Overview

This repository provides the data and code to replicate the results from the paper titled *“The Economic Impact of Uncertainty about U.S. Regulations of the Energy Sector.”*

The package includes two main components:

1. `/measure_uncertainty`: Data and Python code for measuring regulatory uncertainty, as described in Section 2 of the paper.  
2. `/empirical_analysis`: Data and Stata code for generating empirical results, as described in Section 3 of the paper.  

Questions and comments can be directed to the authors at [xiaohan.ma@ttu.edu](mailto:xiaohan.ma@ttu.edu) or [zxie@gwu.edu](mailto:zxie@gwu.edu).  

---

## Data Availability and Provenance Statements

This paper analyzes the full text and metadata of newspaper articles from the U.S. Newsstream database, accessed through ProQuest’s TDM Studio. Due to copyright restrictions, the authors cannot distribute the full text of the news articles analyzed. However, this repository provides the ProQuest IDs and some metadata for all articles used in the analysis (available in `/measure_uncertainty/data/`). Researchers with access to ProQuest’s content can use this information to retrieve the full text and additional metadata of the articles.  

To demonstrate the textual analysis process, this repository includes demo data for five news articles in XML format (located in `/measure_uncertainty/data/nlp_demo/xml_examples`), along with the Python scripts for performing the textual analysis and estimating the uncertainty measures. The estimated uncertainty indexes using all articles are provided in the `/measure_uncertainty/data` subdirectory.  

Other economic data were obtained from publicly available data sources. See details in the **Data Source** section.  

---

## Details on Datasets and Data Sources

The data used in the paper are stored in two subdirectories:

- `/measure_uncertainty/data`: contains data files used in the creation, analysis and visualization of the uncertainty measures.  
- `/empirical_analysis`: contains data used in the baseline empirical analysis and robustness checks.  

A summary of all raw data and sources is available in **Table D1.1**. The raw data were cleaned and/or merged to create final analysis-ready datasets. **Table D1.2** lists all processed datasets constructed from the raw data and the name of the script that generated it.

### Table D1.1: Raw Data and Sources

| Data Name | Data File Location | Provided | Citation |
|-----------|--------------------|----------|----------|
| Demo news article text data | 282091173.xml; 331720143.xml; 391942977.xml; 902573990.xml; 2581635619.xml `/measure_uncertainty/data/nlp_demo/xml_examples` | TRUE | U.S. Newsstream (2022) |
| All news article text data | Not available | FALSE | U.S. Newsstream (2022) |
| Trade journal and magazine text data | Not available | FALSE | ProQuest Central (2023) |
| U.S. Energy Information Administration (EIA) glossary | eia_energy_glossary.xlsx `/measure_uncertainty/data/supplementary_data` | TRUE | EIA (2022) |
| Loughran and McDonald dictionary (2018 version) | lm_sentiment.csv `/measure_uncertainty/data/supplementary_data` | TRUE | Loughran and McDonald (2011) |
| U.S. Newsstream publication title list | us_newsstream_title_list.xls `/measure_uncertainty/data/supplementary_data` | TRUE | ProQuest (2022) |
| Fonts used in figures | coolvetica_rg.otf; palatinolinotype_roman.ttf `/measure_uncertainty/data/supplementary_data` | TRUE | dafont.com (2024); online-fonts.com (2024) |
| U.S. crude oil prices | WTISPLC.xls `/empirical_analysis/raw_data` | TRUE | Federal Reserve Bank of St. Louis and EIA (2022) |
| S&P 500 index | ^spx_m.csv `/empirical_analysis/raw_data` | TRUE | S&P Dow Jones Indices LLC (2022) |
| Federal funds effective rate | FEDFUNDS.xls `/empirical_analysis/raw_data` | TRUE | Board of Governors of the Federal Reserve System (2022) |
| Consumer Price Index (CPI) | CPIAUCSL.xls `/empirical_analysis/raw_data` | TRUE | U.S. Bureau of Labor Statistics (2022) |
| Industrial production | INDPRO.xls `/empirical_analysis/raw_data` | TRUE | Board of Governors of the Federal Reserve System (2022) |
| U.S. oil drilling | IPN213111S.xls `/empirical_analysis/raw_data` | TRUE | Board of Governors of the Federal Reserve System (2022) |
| U.S. oil production | MCRFPUS1m.xls `/empirical_analysis/raw_data` | TRUE | EIA (2022) |
| World oil production | globaloil.csv `/empirical_analysis/raw_data` | TRUE | EIA (2022) |
| Growth rate of world economic activity | igrea.xlsx `/empirical_analysis/raw_data` | TRUE | Kilian (2009) |
| California unemployment rate | CAUR.xls `/empirical_analysis/raw_data` | TRUE | BLS (2023) |
| Texas unemployment rate | TXUR.xls `/empirical_analysis/raw_data` | TRUE | BLS (2023) |
| New York unemployment rate | NYUR.xls `/empirical_analysis/raw_data` | TRUE | BLS (2023) |
| New Mexico unemployment rate | NMUR.xls `/empirical_analysis/raw_data` | TRUE | BLS (2023) |
| Political party of the U.S. president | party.pdf `/empirical_analysis/raw_data` | TRUE | U.S. House of Representatives (2023) |
| Macroeconomic uncertainty | MacroUncertainty.xlsx `/empirical_analysis/raw_data` | TRUE | Jurado et al. (2015) |
| Economic policy uncertainty (EPU) index | epu_index.xlsx `/empirical_analysis/raw_data` | TRUE | Baker et al. (2016) |
| Categorical EPU indexes | categorical_epu_index.xlsx `/measure_uncertainty/data/supplementary_data` | TRUE | Baker et al. (2016) |
| Climate policy uncertainty (CPU) index | cpu_index.csv `/measure_uncertainty/data/supplementary_data` | TRUE | Gavriilidis (2021) |
| Geopolitical risk (GPR) index | gpr_index.xls `/measure_uncertainty/data/supplementary_data` | TRUE | Caldara and Iacoviello (2022) |


### Table D1.2: Processed Data

| Data File | Location | How Created | Description | Provided |
|-----------|----------|-------------|-------------|----------|
| all_uncertainty_scores_baseline.csv | /measure_uncertainty/data | Calculated from sentiment analysis of relevant news article text data. Relevant articles were identified from all news articles in U.S. Newsstream through ProQuest TDM Studio, using the approach discussed in Section 2.2 of the paper. (Python code for identifying relevant articles and calculating uncertainty scores from demo text data is available in `/measure_uncertainty/python_code`). | Contains ProQuest ID, publication title, publication date, and uncertainty scores calculated based on different sections of a news article, including: “RegUncertaintyScore” (from regulatory section), “EconUncertaintyScore” (from economic section), and “UncertaintyScore” (from full text). | TRUE |
| all_uncertainty_scores_broadterm.csv | /measure_uncertainty/data | Calculated from sentiment analysis of an alternative set of relevant news article text data. Relevant articles were identified from all news articles in U.S. Newsstream through ProQuest TDM Studio, using a broader set of energy terms as discussed in Section 2.5 of the paper. (Python code for identifying relevant articles and calculating uncertainty scores from demo text data is available in `/measure_uncertainty/python_code`). | Contains ProQuest ID, publication title, publication date, and uncertainty score for each news article. | TRUE |
| all_uncertainty_scores_journal.csv | /measure_uncertainty/data | Calculated from sentiment analysis of trade journal and magazine article text data. Relevant articles were identified from trade journals and magazines in ProQuest Central through ProQuest TDM Studio, using the same approach as the baseline. (Python code for identifying relevant articles and calculating uncertainty scores from demo text data is available in `/measure_uncertainty/python_code`). | Contains ProQuest ID, publication title, publication date, and uncertainty score for each journal/magazine article. | TRUE |
| oil_regulatory_uncertainty_index_baseline.csv | /measure_uncertainty/data | Generated with `6_estimate_uncertainty_index.py`. The script reads in the pre-saved uncertainty scores (“RegUncertaintyScore”) in all_uncertainty_scores_baseline.csv and outputs the estimated baseline oil regulatory uncertainty index. | Estimated baseline oil regulatory uncertainty index (“RegUncertaintyIndex”). | TRUE |
| oil_regulatory_uncertainty_index_robust.csv | /measure_uncertainty/data | Generated with `6_estimate_uncertainty_index.py`. The script reads in the pre-saved uncertainty scores in all_uncertainty_scores_baseline.csv (“EconUncertaintyScore”), all_uncertainty_scores_broadterm.csv, and all_uncertainty_scores_journal.csv and outputs the estimated economic-adjusted oil regulatory uncertainty index, the broad-term-based index, and the journal-based index. | Contains three alternative indexes: “RegUncertaintyIndex_Econ” (economic-adjusted), “RegUncertaintyIndex_Broad” (broad-term-based), and “RegUncertaintyIndex_Journal” (journal-based). | TRUE |
| oil_supply_uncertainty_index.csv | /measure_uncertainty/data | Generated with `6_estimate_uncertainty_index.py`. The script reads in the pre-saved uncertainty scores (“UncertaintyScore”) in all_uncertainty_scores_baseline.csv and outputs the estimated oil supply uncertainty index. | Estimated general oil supply uncertainty index (“UncertaintyIndex”). | TRUE |
| noun_chunks_by_month_reg.csv | /measure_uncertainty/data | Identified from the news article text data used in the baseline analysis, using spaCy. (Python code for identifying top noun chunks from demo text data is available in `8_extract_noun_chunks.py`). | Contains all noun chunks and their occurrences from the regulatory sections with positive regulatory uncertainty scores that were published during a given month. | TRUE |
| noun_chunks_by_month_general.csv | /measure_uncertainty/data | Identified from the news article text data used in the baseline analysis, using spaCy. (Python code for identifying top noun chunks from demo text data is available in `8_extract_noun_chunks.py`). | Contains all noun chunks and their occurrences from the full news articles with positive uncertainty scores that were published during a given month. | TRUE |
| pub_title_newspaper.csv | /measure_uncertainty/data/supplementary_data | Created based on the title list in `us_newsstream_title_list.xls` by manually combining alternative titles for a newspaper. | Provides a crosswalk of publication titles and newspaper names; a newspaper name can correspond to multiple publication titles. | TRUE |
| wordcloud_mask.png | /measure_uncertainty/data/supplementary_data | Drawn using the Paint app in a Windows system. | Image used as the mask for generating the word cloud figures. | TRUE |
| data_2024.dta | /empirical_analysis | This file was manually compiled by copying and pasting data from the files listed in Table D1.1 and Table D1.2, with certain transformations applied (e.g., taking natural logs) in Excel. The file was then imported into Stata and saved as a `.dta` file. (See Table D2 for a description of each variable and how original data were transformed). | Clean dataset used for empirical analysis. | TRUE |

---

The data file data_2024.dta in `/empirical_analysis` combines the estimated oil 
regulatory uncertainty indexes with the economic data listed in Table D1.1 and Table D1.2. 
Table D2 provides a description of each variable in `data_2024.dta` along with its 
associated data file. 

### Table D2: Data in `data_2024.dta`

| Column | Description | Source |
|--------|-------------|--------|
| oilregunc2024 | Baseline oil regulatory uncertainty index | oil_regulatory_uncertainty_index_baseline.csv |
| oilregunc2024econ | Economic-adjusted oil regulatory uncertainty index | RegUncertaintyIndex_Econ in oil_regulatory_uncertainty_index_robust.csv |
| oilregunc_journal | Journal-based oil regulatory uncertainty index | RegUncertaintyIndex_Journal in oil_regulatory_uncertainty_index_robust.csv |
| logrwti | Natural log of U.S. crude oil prices deflated by CPI | WTISPLC.xls, CPIAUCSL.xls |
| logstock | Natural log of S&P 500 index | ^spx_m.csv |
| ffr | Federal funds effective rate | FEDFUNDS.xls |
| logcpi | Natural log of CPI | CPIAUCSL.xls |
| logipm | Natural log of industrial production | INDPRO.xls |
| logdrill | Natural log of U.S. oil drilling | IPN213111S.xls |
| logprodoil | Natural log of U.S. oil production | MCRFPUS1m.xls |
| logworldprodoil | Natural log of world oil production | globaloil.csv |
| kiliamindex_100 | Growth rate of world economic activity ÷ 100 | igrea.xlsx |
| caur | California unemployment rate | CAUR.xls |
| txur | Texas unemployment rate | TXUR.xls |
| nyur | New York unemployment rate | NYUR.xls |
| nmur | New Mexico unemployment rate | NMUR.xls |
| dum | Dummy = 1 Republican president, 0 Democrat | party.pdf |
| jurado | Macroeconomic uncertainty (h=12) | MacroUncertainty.xlsx |
| epu | Economic policy uncertainty index | epu_index.xlsx |
| epureg | EPU regulation index | categorical_epu_index.xlsx |
| cpu | Climate policy uncertainty index | cpu_index.csv |
| gpr | Geopolitical risk index | gpr_index.xls |

---

## Programs and Code

The `/measure_uncertainty/python_code` subdirectory contains Python code to create, 
analyze, and visualize the uncertainty indexes. The `/empirical_analysis` subdirectory 
contains Stata code used in the empirical analysis. 

### Python Code (in `/measure_uncertainty/python_code`)

- **master.py**: A master file to execute all Python scripts in this subdirectory.  
- **1_parse_xml.py**: Parses the full text and metadata of each news article from XML files (executed on demo data).  
- **2_clean_data.py**: Cleans the parsed data and drops duplicates (executed on demo data).  
- **3_match_keywords.py**: Searches energy keywords in the full text to determine relevance of articles (executed on demo data).  
- **4_extract_regulatory_sections.py**: Extracts “regulatory sections” from news articles (executed on demo data).  
- **5_quantify_uncertainty.py**: Calculates uncertainty scores for each regulatory section and the full text of each article (executed on demo data).  
- **6_estimate_uncertainty_index.py**: Estimates the baseline oil regulatory uncertainty index, alternative oil regulatory uncertainty indexes, and general oil supply uncertainty index.  
- **7_visualize_indexes.py**: Plots oil regulatory uncertainty indexes, general oil supply uncertainty index, and other comparable indexes.  
- **8_extract_noun_chunks.py**: Extracts noun chunks and their occurrences from text (executed on demo data).  
- **9_plot_word_clouds.py**: Plots word clouds of top noun chunks from select articles.  

A summary of the inputs and outputs for each Python script is available in Table D3.

### Table D3: Inputs and Outputs of Python Scripts

| Script | Input | Output |
|--------|-------|--------|
| 1_parse_xml.py | XML demo files | parsed_xml.pkl |
| 2_clean_data.py | parsed_xml.pkl | parsed_xml_clean.pkl |
| 3_match_keywords.py | parsed_xml_clean.pkl | parsed_xml_clean.pkl |
| 4_extract_regulatory_sections.py | parsed_xml_clean.pkl | parsed_xml_clean.pkl |
| 5_quantify_uncertainty.py | parsed_xml_clean.pkl | parsed_xml_clean.pkl |
| 6_estimate_uncertainty_index.py | all_uncertainty_scores_baseline.csv; broadterm.csv; journal.csv | oil_regulatory_uncertainty_index_baseline.csv; oil_regulatory_uncertainty_index_robust.csv; oil_supply_uncertainty_index.csv |
| 7_visualize_indexes.py | oil_regulatory_uncertainty_index.csv; oil_supply_uncertainty_index.csv | figure1.jpg; figure3.jpg; appendixC.jpg; appendixD.jpg |
| 8_extract_noun_chunks.py | parsed_xml_clean.pkl | N/A |
| 9_plot_word_clouds.py | noun_chunks_by_month_reg.csv; noun_chunks_by_month_general.csv | figure2.jpg; figure4.jpg |

### Stata Code (in `/empirical_analysis`)

- **var_energy2024_baseline.do**: Produces the baseline VAR using data from `data_2024.dta`.  
- **var_energy2024_robust.do**: Produces robustness checks using alternative VAR specifications and data from `data_2024.dta`.  
- **LPoil2024.do**: Produces robustness checks with oil production using local projections and data from `data_2024.dta`.  
- **LPoil2024drill.do**: Produces robustness checks with oil drilling using local projections and data from `data_2024.dta`.  

---

## List of Figures and Programs 

### Table D4: Figures and Programs

| Figure | Program | Lines | Output |
|--------|---------|-------|--------|
| Fig.1 | 7_visualize_indexes.py | 46–133 | figure1.jpg |
| Fig.2 | 9_plot_word_clouds.py | 42–86 | figure2.jpg |
| Fig.3 | 7_visualize_indexes.py | 149–222 | figure3.jpg |
| Fig.4 | 9_plot_word_clouds.py | 89–137 | figure4.jpg |
| Fig.5 | var_energy2024_baseline.do | 14–31 | figure5.eps |
| Fig.6 | var_energy2024_baseline.do | 14–31 | figure6.eps |
| Fig.7a,b | var_energy2024_baseline.do | 34–44 | figure7a.eps, figure7b.eps |
| Fig.8 | var_energy2024_baseline.do | 47–59 | figure8.eps |
| Appendix C | 7_visualize_indexes.py | 237–293 | appendixC.jpg |
| Appendix D | 7_visualize_indexes.py | 364–441 | appendixD.jpg |
| Appendix E.1.1–E.1.2 | var_energy2024_robust.do | 125–136 | figureE11.eps, figureE12.eps |
| Appendix E.2.1–E.2.2 | var_energy2024_robust.do | 12–24 | figureE21.eps, figureE22.eps |
| Appendix G.1.1–G.1.2 | var_energy2024_robust.do | 27–38 | figureG11.eps, figureG12.eps |
| Appendix G.2.1–G.2.2 | var_energy2024_robust.do | 41–52 | figureG21.eps, figureG22.eps |
| Appendix G.3.1–G.3.2 | var_energy2024_robust.do | 55–66 | figureG31.eps, figureG32.eps |
| Appendix G.4.1–G.4.2 | var_energy2024_robust.do | 69–80 | figureG41.eps, figureG42.eps |
| Appendix G.5.1–G.5.2 | var_energy2024_robust.do | 83–94 | figureG51.eps, figureG52.eps |
| Appendix G.6.1–G.6.2 | var_energy2024_robust.do | 97–108 | figureG61.eps, figureG62.eps |
| Appendix G.7.1–G.7.2 | var_energy2024_robust.do | 111–122 | figureG71.eps, figureG72.eps |
| Appendix H.1 | LPoil2024.do | all | figureH1.eps |
| Appendix H.2 | LPoil2024drill.do | all | figureH2.eps |

---

## Computational Requirements

### Software Requirements

- ✔ The replication package contains one or more programs to install all dependencies and set up the necessary directory structure.  
- **Python 3.10+**  
  - A virtual Python environment should be created using `requirements.txt` in the home directory.  
  - Please run:  
    ```bash
    pip install -r requirements.txt
    ```  
  - See the [pip user guide on ensuring repeatability](https://pip.pypa.io/en/stable/user_guide/#ensuring-repeatability) for further instructions on creating and using the `requirements.txt` file.  
- **Stata (last run with version 18)**  
  - Requires the `var` package (as of April 2023).  

---

## Instructions to Replicators

1. Download the replication package  
2. Set up environment (see above)  
3. Run `master.py` to reproduce outputs  
4. Run Stata `.do` files for empirical analysis  

---

## References

- Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring economic policy uncertainty. *Quarterly Journal of Economics*, 131(4), 1593–1636.  
- Baker, S. R., Bloom, N., & Davis, S. J. (2016). *Categorical U.S. EPU Indexes*. Retrieved July 24, 2024, from [https://www.policyuncertainty.com/categorical_epu.html](https://www.policyuncertainty.com/categorical_epu.html).  
- Caldara, D., & Iacoviello, M. (2022). Measuring geopolitical risk. *American Economic Review*, 112(4), 1194–1225.  
- Caldara, D., & Iacoviello, M. (2022). *Geopolitical Risk Index*. Retrieved August 8, 2024, from [https://www.matteoiacoviello.com/gpr.htm](https://www.matteoiacoviello.com/gpr.htm).  
- Federal Reserve Bank of St. Louis & U.S. Energy Information Administration (2022). *Spot Crude Oil Price: West Texas Intermediate (WTI)*. Retrieved April 6, 2022, from [https://fred.stlouisfed.org/series/WTISPLC](https://fred.stlouisfed.org/series/WTISPLC).  
- Gavriilidis, K. (2021). Measuring climate policy uncertainty. SSRN 3847388.  
- Gavriilidis, K. (2021). *Climate Policy Uncertainty (CPU) Index*. Retrieved December 28, 2024, from [https://www.policyuncertainty.com/climate_uncertainty.html](https://www.policyuncertainty.com/climate_uncertainty.html).  
- Jurado, K., Ludvigson, S. C., & Ng, S. (2015). Measuring uncertainty. *American Economic Review*, 105(3), 1177–1216.  
- Jurado, K., Ludvigson, S. C., & Ng, S. (2015). *Total Macro Uncertainty, 12-Month Forecast Horizon*. Retrieved February 2, 2023, from [https://www.sydneyludvigson.com/macro-and-financial-uncertainty-indexes](https://www.sydneyludvigson.com/macro-and-financial-uncertainty-indexes).  
- Kilian, L. (2009). Not all oil price shocks are alike: Disentangling demand and supply shocks in the crude oil market. *American Economic Review*, 99(3), 1053–69.  
- Kilian, L. (2009). *Index of global real economic activity*. Retrieved April 6, 2022, from [https://www.dallasfed.org/research/igrea](https://www.dallasfed.org/research/igrea).  
- Loughran, T., & McDonald, B. (2011). When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. *The Journal of Finance*, 66(1), 35–65.  
- Loughran-McDonald Master Dictionary with Sentiment Word Lists. Retrieved May 21, 2020, from [https://sraf.nd.edu/loughranmcdonald-master-dictionary/](https://sraf.nd.edu/loughranmcdonald-master-dictionary/).  
- ProQuest (2022). *Title Lists System*. Retrieved July 2, 2022, from [https://about.proquest.com/en/customer-care/title-lists/](https://about.proquest.com/en/customer-care/title-lists/).  
- ProQuest Central (2023). Database accessed through ProQuest TDM Studio. Retrieved May 12, 2023, from [https://tdmstudio.proquest.com/home](https://tdmstudio.proquest.com/home).  
- S&P Dow Jones Indices LLC (2022). *S&P 500 Index, Monthly Close Price*. Retrieved April 11, 2022, from [https://finance.yahoo.com/quote/%5EGSPC/history/?frequency=1mo](https://finance.yahoo.com/quote/%5EGSPC/history/?frequency=1mo).  
- U.S. Bureau of Labor Statistics (2022). *Consumer Price Index for All Urban Consumers*. Retrieved April 11, 2022, from [https://fred.stlouisfed.org/series/CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL).  
- U.S. Bureau of Labor Statistics (2023). *Unemployment Rate in California*. Retrieved February 2, 2023, from [https://fred.stlouisfed.org/series/CAUR](https://fred.stlouisfed.org/series/CAUR).  
- U.S. Bureau of Labor Statistics (2023). *Unemployment Rate in Texas*. Retrieved February 2, 2023, from [https://fred.stlouisfed.org/series/TXUR](https://fred.stlouisfed.org/series/TXUR).  
- U.S. Bureau of Labor Statistics (2023). *Unemployment Rate in New York*. Retrieved February 2, 2023, from [https://fred.stlouisfed.org/series/NYUR](https://fred.stlouisfed.org/series/NYUR).  
- U.S. Bureau of Labor Statistics (2023). *Unemployment Rate in New Mexico*. Retrieved February 2, 2023, from [https://fred.stlouisfed.org/series/NMURN](https://fred.stlouisfed.org/series/NMURN).  
- U.S. Energy Information Administration (2022). *Glossary of Energy Terms*. Retrieved February 18, 2022, from [https://www.eia.gov/tools/glossary/](https://www.eia.gov/tools/glossary/).  
- U.S. Energy Information Administration (2022). *Field Production of Crude Oil*. Retrieved April 6, 2022, from [https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=MCRFPUS1&f=M](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=MCRFPUS1&f=M).  
- U.S. Energy Information Administration (2022). *World Crude Oil Production (including lease condensate)*. Retrieved April 6, 2022, from [https://www.eia.gov/international/data/world/petroleum-and-other-liquids/monthly-petroleum-and-other-liquids-production](https://www.eia.gov/international/data/world/petroleum-and-other-liquids/monthly-petroleum-and-other-liquids-production).  
- U.S. House of Representatives: History, Arts & Archives (2023). *Party Government Since 1857*. Retrieved February 2, 2023, from [https://history.house.gov/Institution/Presidents-Coinciding/Party-Government/](https://history.house.gov/Institution/Presidents-Coinciding/Party-Government/).  
- U.S. Newsstream (2022). Database accessed through ProQuest TDM Studio. Retrieved May 17, 2022, from [https://tdmstudio.proquest.com/home](https://tdmstudio.proquest.com/home).  
- dafont.com (2024). *Coolvetica* font. Retrieved December 28, 2024, from [https://www.dafont.com/coolvetica.font](https://www.dafont.com/coolvetica.font).  
- online-fonts.com (2024). *Palatino Linotype* font. Retrieved December 28, 2024, from [https://online-fonts.com/fonts/palatino-linotype](https://online-fonts.com/fonts/palatino-linotype).  

---

## Acknowledgements

The README template recommended by the journal was used to generate this document:  

Lars Vilhuber, Connolly, M., Koren, M., Llull, J., & Morrow, P. (2022). *A template README for social science replication packages*. Social Science Data Editors. [https://social-science-data-editors.github.io/template_README/](https://social-science-data-editors.github.io/template_README/)

