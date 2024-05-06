import pandas as pd

df = pd.read_csv ( "/Users/deboraheunice/Desktop/lab_exam_practice/Deborah Eunice Arinaza - Exam_Table.csv")
df = df['Scientific Name'].unique()
df.to_csv('/Users/deboraheunice/Desktop/lab_exam_practice/Arinaza_B3_answer/b3_output3.csv')
