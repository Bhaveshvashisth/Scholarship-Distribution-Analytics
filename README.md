# Scholarship Distribution Analytics

PBL project for **Foundations of Data Science (CCSDS0301)**, NIET Greater Noida.

**Student:** Bhavesh Vashisth
**Faculty:** Ms. Smriti Jaiswal
**SDG:** SDG 4 - Quality Education

## About the project
Scholarship records increase every year and checking them manually is slow and error-prone. This project cleans a sample student scholarship dataset and analyses how the scholarship amount is distributed across departments, categories and family income groups.

## Dataset
- Reference source: Global Scholarship Opportunities Dataset (Kaggle).
- A sample student-level dataset of 8 students was prepared for demonstration with these columns: Student ID, Department, Category, Family Income, Scholarship Amount and Status.
- `data/raw_scholarship_data.csv` contains the raw data (with inconsistent department names and one duplicate record).
- `data/cleaned_scholarship_data.csv` is created by the script after cleaning.

## FODS concepts used
Data types, data cleaning, data integration, data transformation, normalization, data aggregation, descriptive analytics and visualization.

## Workflow
Raw Data -> Cleaning -> Integration -> Transformation -> Normalization -> Analysis -> Visualization

1. Remove extra spaces and standardise names (CSE, C.S.E. and Computer Science become CSE).
2. Check for missing values and remove duplicate records.
3. Group family income into income bands and normalise the scholarship amount.
4. Calculate the number of students, total, average and percentage share for each department, category and income group.
5. Create charts and export the results to Excel.

## Results (sample data)
| Department | Students | Total Scholarship | Average |
|------------|----------|-------------------|---------|
| CSE | 3 | Rs. 75,000 | Rs. 25,000 |
| ECE | 2 | Rs. 55,000 | Rs. 27,500 |
| ME | 2 | Rs. 40,000 | Rs. 20,000 |
| Civil | 1 | Rs. 15,000 | Rs. 15,000 |
| **Total** | **8** | **Rs. 1,85,000** | **Rs. 23,125** |

| Category | Students | Total Scholarship | Average |
|----------|----------|-------------------|---------|
| General | 3 | Rs. 50,000 | Rs. 16,667 |
| OBC | 3 | Rs. 75,000 | Rs. 25,000 |
| SC | 2 | Rs. 60,000 | Rs. 30,000 |
| **Total** | **8** | **Rs. 1,85,000** | **Rs. 23,125** |

The dataset has only 8 sample records, so the results demonstrate the method and are not general conclusions.

## How to run
```
pip install -r requirements.txt
python analysis.py
```
The charts (`outputs/department_charts.png`, `outputs/category_charts.png`) and the Excel workbook (`outputs/scholarship_analysis.xlsx`) are saved in the `outputs` folder.

## Folder structure
```
Scholarship-Distribution-Analytics/
|-- analysis.py
|-- requirements.txt
|-- README.md
|-- data/
|   |-- raw_scholarship_data.csv
|   |-- cleaned_scholarship_data.csv
|-- outputs/
    |-- department_charts.png
    |-- category_charts.png
    |-- scholarship_analysis.xlsx
```

## Tools
Python (pandas, Matplotlib), Microsoft Excel, Git and GitHub.
