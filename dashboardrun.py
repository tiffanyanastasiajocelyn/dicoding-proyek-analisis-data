import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Set the path for the dataset (gunakan jalur absolut)
DATA_PATH = "C:\\Users\\User\\Downloads\\gabungan.csv"

# Load the dataset
data = pd.read_csv(DATA_PATH)

# Set the title of the dashboard
st.title("Dashboard Analisis Data Kualitas Udara dan Curah Hujan")

# Pertanyaan 1
st.markdown("## Pertanyaan 1: Bagaimana perbedaan rata-rata konsentrasi PM2.5 dan PM10 antara stasiun Guanyuan dan Gucheng selama periode 2013 hingga 2017?")

# Filter data untuk tahun 2013 hingga 2017
filtered_data_1 = data[(data['year'] >= 2013) & (data['year'] <= 2017)]
mean_pm = filtered_data_1[['PM2.5_guanyuan', 'PM10_guanyuan', 'PM2.5_gucheng', 'PM10_gucheng']].mean()

# Visualisasi
plt.figure(figsize=(10, 5))
sns.barplot(x=mean_pm.index, y=mean_pm.values)
plt.title('Rata-rata Konsentrasi PM2.5 dan PM10 (2013-2017)')
plt.ylabel('Konsentrasi (µg/m³)')
plt.xticks(rotation=45)
st.pyplot(plt)

# Pertanyaan 2
st.markdown("## Pertanyaan 2: Apakah ada perbedaan signifikan dalam curah hujan (RAIN) bulanan antara stasiun Guanyuan dan Gucheng selama periode 2015?")

# Filter data untuk tahun 2015
filtered_data_2 = data[data['year'] == 2015]
rain_monthly = filtered_data_2.groupby('month')[['RAIN_guanyuan', 'RAIN_gucheng']].mean().reset_index()

# Visualisasi
plt.figure(figsize=(10, 5))
sns.lineplot(data=rain_monthly, x='month', y='RAIN_guanyuan', label='Guanyuan', marker='o')
sns.lineplot(data=rain_monthly, x='month', y='RAIN_gucheng', label='Gucheng', marker='o')
plt.title('Curah Hujan Bulanan (2015)')
plt.ylabel('Curah Hujan (mm)')
plt.xlabel('Bulan')
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(plt)
