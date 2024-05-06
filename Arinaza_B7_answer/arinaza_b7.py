import pandas as pd

df = pd.read_csv ( "/Users/deboraheunice/Desktop/lab_exam_practice/Deborah Eunice Arinaza - Exam_Table.csv")
df = df.T
df.to_csv('b7_output1.csv')