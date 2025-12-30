# Smart Health Analytics Project

This is an end-to-end **Healthcare Data Analytics project** built using **Python, MySQL, SQL, Pandas, Matplotlib, and Tkinter GUI**.

The project analyzes patient health data, identifies disease trends, calculates health risk levels, and provides an interactive desktop-based GUI for visualization and reporting.

---

## Features

- Disease-wise patient analysis  
- Hospital-wise patient load analysis  
- Patient health risk classification (Low / Medium / High)  
- Interactive charts using Python (Matplotlib)  
- Desktop GUI application using Tkinter  
- MySQL database integration  
- CSV data generation using Python  
- Excel report export  

---

## Technologies Used

- **Python**
- **MySQL**
- **SQL**
- **Pandas**
- **Matplotlib**
- **Tkinter**
- **Git & GitHub**

---
Health_Analytics_Project/
│
├── analysis/
│ └── health_sql_analysis.py
│
├── data/
│ ├── patients.csv
│ └── visits.csv
│
├── gui/
│ └── health_app.py
│
├── generate_health_data.py
└── README.md

---

## How to Run the Project

### 1️ Clone the repository
```bash
git clone https://github.com/dep00001/smart-health-analytics.git
cd smart-health-analytics
2️ Install required Python libraries
pip install pandas matplotlib mysql-connector-python openpyxl

3️ Setup MySQL Database
CREATE DATABASE health_analytics;

Import the CSV files:
patients.csv
visits.csv

4️ Run Python Scripts
Generate data
python generate_health_data.py

Run SQL analysis
python analysis/health_sql_analysis.py

Run GUI application
python gui/health_app.py

---

## Health Risk Logic

Patient risk is calculated using:
- BMI
- Blood Pressure
- Sugar Level
- Cholesterol
- Heart Rate

Risk categories:
- Low Risk  
- Medium Risk  
- High Risk  

---

## Use Case

This project simulates a real-world hospital health analytics system that helps:
- Doctors analyze patient health  
- Hospitals monitor disease trends  
- Management generate reports  
- Data analysts practice healthcare analytics  

---

## Author

**Deepak Adhikari**  
Aspiring Data Analyst | Python | SQL | Healthcare Analytics
