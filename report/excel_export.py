import pandas as pd

def generate_excel_report(equipment_data):
    df = pd.DataFrame(equipment_data)
    df.to_excel('equipment_report.xlsx', index=False)
