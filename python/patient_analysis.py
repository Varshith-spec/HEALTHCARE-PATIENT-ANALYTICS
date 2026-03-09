import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/hospital_data.csv')

# Remove duplicates
df = df.drop_duplicates()

# Fill missing wait times
df['wait_time_minutes'] = df['wait_time_minutes'].fillna(df['wait_time_minutes'].median())

# Average wait time by department
wait_time = df.groupby('department')['wait_time_minutes'].mean()
print(wait_time)

# Readmission rate
readmission_rate = df['readmission_flag'].mean()
print("Readmission Rate:", readmission_rate)

# Patient admissions trend
df['department'].value_counts().plot(kind='bar')

plt.title("Patient Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Patients")
plt.show()
