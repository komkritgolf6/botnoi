import pandas as pd

def get_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def calculate_grade(filename):
    
    df = pd.read_excel(filename)
    
    df['คะแนน'] = pd.to_numeric(df['คะแนน'], errors='coerce')
    
    df['เกรด'] = df['คะแนน'].apply(get_grade)
    
    df['เกรด'] = pd.Categorical(df['เกรด'], categories=['A', 'B', 'C', 'D', 'F'], ordered=True)
    df.sort_values(by='เกรด', inplace=True)

    df.to_excel(filename, index=False)
    
  


calculate_grade('grades_with_grades.xlsx')
