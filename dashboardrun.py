import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ubah direktori kerja
os.chdir('C:/Users/User/Downloads')

# Set the title of the dashboard
st.title("Dashboard Analisis Data Kualitas Udara")

# Load the data
data = pd.read_csv('gabungan.csv')

# Filter data for the required questions
data['date'] = pd.to_datetime(data[['year', 'month', 'day']])
data_guanyuan = data[['date', 'PM2.5_guanyuan', 'PM10_guanyuan']].set_index('date')
data_gucheng = data[['date', 'PM2.5_gucheng', 'PM10_gucheng']].set_index('date')

# Pertanyaan 1
st.markdown("### Pertanyaan 1: Bagaimana perbedaan rata-rata konsentrasi PM2.5 dan PM10 antara stasiun Guanyuan dan Gucheng selama periode 2013 hingga 2017?")
average_pm25_guanyuan = data_guanyuan['PM2.5_guanyuan'].mean()
average_pm10_guanyuan = data_guanyuan['PM10_guanyuan'].mean()
average_pm25_gucheng = data_gucheng['PM2.5_gucheng'].mean()
average_pm10_gucheng = data_gucheng['PM10_gucheng'].mean()

# Create a bar chart for average PM2.5 and PM10
labels = ['Guanyuan PM2.5', 'Guanyuan PM10', 'Gucheng PM2.5', 'Gucheng PM10']
values = [average_pm25_guanyuan, average_pm10_guanyuan, average_pm25_gucheng, average_pm10_gucheng]

fig1, ax1 = plt.subplots()
ax1.bar(labels, values, color=['blue', 'blue', 'orange', 'orange'])
ax1.set_ylabel('Rata-rata Konsentrasi (µg/m³)')
ax1.set_title('Rata-rata Konsentrasi PM2.5 dan PM10')

# Display the chart in the Streamlit app
st.pyplot(fig1)

# Pertanyaan 2
st.markdown("### Pertanyaan 2: Apakah ada perbedaan signifikan dalam curah hujan (RAIN) bulanan antara stasiun Guanyuan dan Gucheng selama periode 2015?")
rain_guanyuan = data[data['year'] == 2015].groupby('month')['RAIN_guanyuan'].mean()
rain_gucheng = data[data['year'] == 2015].groupby('month')['RAIN_gucheng'].mean()

# Create a line plot for monthly rain
plt.figure(figsize=(10, 5))
plt.plot(rain_guanyuan.index, rain_guanyuan.values, label='Guanyuan', marker='o')
plt.plot(rain_gucheng.index, rain_gucheng.values, label='Gucheng', marker='o')
plt.title('Curah Hujan Bulanan 2015')
plt.xlabel('Bulan')
plt.ylabel('Curah Hujan (mm)')
plt.xticks(rain_guanyuan.index)
plt.legend()

# Display the chart in the Streamlit app
st.pyplot(plt.gcf())
