import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Smart Health Analytics System")
root.geometry("500x400")


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Deepak00_00",
        database="health_analytics"
    )
def show_risk_summary():
    conn = get_connection()
    query = "SELECT sugar_level, blood_pressure FROM patients"
    df = pd.read_sql(query, conn)

    def risk_level(row):
        if row['sugar_level'] > 180 and row['blood_pressure'] > 160:
            return "High Risk"
        elif row['sugar_level'] > 140 or row['blood_pressure'] > 140:
            return "Medium Risk"
        else:
            return "Low Risk"

    df['risk'] = df.apply(risk_level, axis=1)
    summary = df['risk'].value_counts().to_string()

    messagebox.showinfo("Risk Summary", summary)
    conn.close()

def show_disease_chart():
    conn = get_connection()
    query = """
    SELECT disease, COUNT(*) AS total_cases
    FROM visits
    GROUP BY disease
    """
    df = pd.read_sql(query, conn)
    print(df) 

    plt.figure()
    plt.bar(df['disease'], df['total_cases'])
    plt.title("Disease-wise Patient Count")
    plt.xlabel("Disease")
    plt.ylabel("Patients")
    plt.show()

    conn.close()

def show_hospital_load():
    conn = get_connection()
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
    plt.ylabel("Visits")
    plt.show()

    conn.close()


title = tk.Label(
    root,
    text="Smart Health Analytics Dashboard",
    font=("Segoe UI", 18, "bold"),
    bg="#f4f6f7",
    fg="#2c3e50"
)
title.pack(pady=15)

info = tk.Label(
    root,
    text="Python + MySQL + Data Analytics",
    font=("Segoe UI", 11),
    bg="#f4f6f7",
    fg="#34495e"
)
info.pack(pady=5)

btn_style = {
    "font": ("Segoe UI", 11),
    "width": 28,
    "bg": "#3498db",
    "fg": "white"
}

btn_risk = tk.Button(root, text="Show Risk Summary",
                     command=show_risk_summary, **btn_style)
btn_risk.pack(pady=6)

btn_disease = tk.Button(root, text="Disease-wise Chart",
                        command=show_disease_chart, **btn_style)
btn_disease.pack(pady=6)

btn_hospital = tk.Button(root, text="Hospital Load Chart",
                         command=show_hospital_load, **btn_style)
btn_hospital.pack(pady=6)

exit_btn = tk.Button(
    root, text="Exit", command=root.destroy,
    font=("Segoe UI", 11),
    width=28, bg="#e74c3c", fg="white"
)
exit_btn.pack(pady=12)

def export_excel_report():
    conn = get_connection()

    # Queries
    q_patients = "SELECT * FROM patients"
    q_visits = "SELECT * FROM visits"

    df_patients = pd.read_sql(q_patients, conn)
    df_visits = pd.read_sql(q_visits, conn)

    # Risk calculation
    def risk_level(row):
        if row['sugar_level'] > 180 and row['blood_pressure'] > 160:
            return "High Risk"
        elif row['sugar_level'] > 140 or row['blood_pressure'] > 140:
            return "Medium Risk"
        else:
            return "Low Risk"

    df_patients['risk'] = df_patients.apply(risk_level, axis=1)

    # Save Excel
    file_path = "reports/Health_Analytics_Report.xlsx"
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df_patients.to_excel(writer, sheet_name="Patients", index=False)
        df_visits.to_excel(writer, sheet_name="Visits", index=False)

    conn.close()
    messagebox.showinfo("Export Success",
                        f"Excel report saved:\n{file_path}")

btn_export = tk.Button(
    root,
    text="Export Excel Health Report",
    command=export_excel_report,
    font=("Segoe UI", 11),
    width=28,
    bg="#27ae60",
    fg="white"
)
btn_export.pack(pady=8)


root.mainloop()
