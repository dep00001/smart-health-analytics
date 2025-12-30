import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Deepak00_00",
    database="health_analytics"
)

print("Connected to MySQL successfully")

query = """
SELECT disease, COUNT(*) AS total_cases
FROM visits
GROUP BY disease
"""

df = pd.read_sql(query, conn)

plt.figure()
plt.bar(df['disease'], df['total_cases'])
plt.title("Disease-wise Patient Count")
plt.xlabel("Disease")
plt.ylabel("Number of Patients")
plt.show()

query = """
SELECT hospital, COUNT(*) AS total_visits
FROM visits
GROUP BY hospital
"""

df = pd.read_sql(query, conn)

plt.figure()
plt.bar(df['hospital'], df['total_visits'])
plt.title("Hospital Load Analysis")
plt.xlabel("Hospital")
plt.ylabel("Total Visits")
plt.show()

query = """
SELECT MONTH(visit_date) AS month, COUNT(*) AS visits
FROM visits
GROUP BY month
ORDER BY month
"""

df = pd.read_sql(query, conn)

plt.figure()
plt.plot(df['month'], df['visits'], marker='o')
plt.title("Monthly Patient Visits")
plt.xlabel("Month")
plt.ylabel("Visits")
plt.show()

query = "SELECT patient_id, sugar_level, blood_pressure FROM patients"
df = pd.read_sql(query, conn)

def risk_level(row):
    if row['sugar_level'] > 180 and row['blood_pressure'] > 160:
        return "High Risk"
    elif row['sugar_level'] > 140 or row['blood_pressure'] > 140:
        return "Medium Risk"
    else:
        return "Low Risk"

df['risk'] = df.apply(risk_level, axis=1)

print(df['risk'].value_counts())

conn.close()
