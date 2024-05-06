import pandas as pd

df = pd.read_csv ( "/Users/deboraheunice/Desktop/lab_exam_practice/Deborah Eunice Arinaza - Exam_Table.csv")
print(df['Scientific Name', 'Count'].mean('Pomacentrus adelus', ''))