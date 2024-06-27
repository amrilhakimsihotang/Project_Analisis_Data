# import library yang dibutuhkan

import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

# side bar
st.sidebar.image("data/bike.png",
caption="Amril Hakim Sihotang")

st.markdown("<h4 style='font-size: 30px;'>Bike Sharing Dashboard</h4>",
unsafe_allow_html=True)

#Load dataset day.csv

df_day = pd.read_csv('data/day.csv')
# df_day

#Load dataset hour.csv"""

df_hour = pd.read_csv('data/hour.csv')
# df_hour

# Hapus kolom yang tidak diperlukan
columns_to_drop_1 = ['instant', 'dteday', 'casual', 'registered']
df_day_cleaned_1 = df_day.drop(columns = columns_to_drop_1)


# Hapus kolom yang tidak diperlukan
columns_to_drop_2 = ['instant', 'dteday', 'cnt']
df_day_cleaned_2 = df_day.drop(columns = columns_to_drop_2)

# Hapus kolom yang tidak diperlukan
columns_to_drop_3 = ['instant', 'season', 'yr', 'mnth',
                     'holiday','weathersit','temp',
                     'atemp','hum','windspeed']
df_hour_cleaned_3 = df_hour.drop(columns = columns_to_drop_3)

# Hapus kolom yang tidak diperlukan
columns_to_drop_4 = ['instant', 'dteday', 'season', 'yr', 'mnth',
                     'holiday', 'weekday', 'workingday',
                     'weathersit', 'windspeed']
df_hour_cleaned_4 = df_hour.drop(columns = columns_to_drop_4)

groupby_1 = df_day_cleaned_1.groupby(['season', 'weathersit']).agg({
    'cnt': ['mean', 'sum'],
    'temp': 'mean',
    'atemp': 'mean',
    'hum': 'mean',
    'windspeed': 'mean'
}).reset_index()
# Merename/mengatur nama kolom hasil agregasi agar lebih jelas
groupby_1.columns = ['season', 'weathersit',
                     'cnt_mean', 'cnt_sum', 'temp_mean',
                     'atemp_mean', 'hum_mean', 'windspeed_mean']

# Mengatur style untuk plot
sns.set(style="whitegrid")

def create_plots_1():
    # Membuat grafik dengan subplot untuk jumlah rata-rata berdasarkan musim dan kondisi cuaca
    plt.figure(figsize=(8, 6))

    # Subplot pertama untuk jumlah rata-rata pengguna sepeda berdasarkan musim dan kondisi cuaca
    plt.subplot(2, 1, 1)
    bar1 = sns.barplot(x='season', y='cnt_mean', hue='weathersit', data=groupby_1, palette='viridis')
    plt.title('Total pengguna sepeda berdasarkan musim dan kondisi cuaca',fontsize=7)
    plt.xlabel('Season',fontsize=6)
    plt.ylabel('Jumlah rata-rata pengguna sepeda',fontsize=6)
    plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'],fontsize=6)
    legend1 = plt.legend(title='Weather Condition', labels=['Clear/Partly Cloudy', 'Mist/Cloudy', 'Light Snow/Rain'],fontsize=5)

    # Mengatur warna label untuk subplot pertama
    title_obj1 = plt.title('Jumlah rata-rata pengguna sepeda berdasarkan musim dan kondisi cuaca',fontsize=7)
    title_obj1.set_color('blue')
    xlabel_obj1 = plt.xlabel('Season',fontsize=6)
    xlabel_obj1.set_color('red')
    ylabel_obj1 = plt.ylabel('Jumlah rata-rata pengguna sepeda',fontsize=6)
    ylabel_obj1.set_color('green')

    # Mengubah warna teks di dalam legend untuk subplot pertama
    for text, color in zip(legend1.get_texts(), sns.color_palette('viridis', 3)):
        text.set_color(color)

    # Subplot kedua untuk jumlah total pengguna sepeda berdasarkan musim dan kondisi cuaca
    plt.subplot(2, 1, 2)
    bar2 = sns.barplot(x='season', y='cnt_sum', hue='weathersit', data=groupby_1, palette='viridis')
    plt.title('Total pengguna sepeda berdasarkan musim dan kondisi cuaca',fontsize=7)
    plt.xlabel('Season',fontsize=6)
    plt.ylabel('Jumlah total pengguna sepeda',fontsize=6)
    plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'],fontsize=6)
    legend2 = plt.legend(title='Weather Condition', labels=['Clear/Partly Cloudy', 'Mist/Cloudy', 'Light Snow/Rain'],fontsize=5)

    # Mengatur warna label untuk subplot kedua
    title_obj2 = plt.title('Jumlah total pengguna sepeda berdasarkan musim dan kondisi cuaca',fontsize=7)
    title_obj2.set_color('blue')
    xlabel_obj2 = plt.xlabel('Season',fontsize=6)
    xlabel_obj2.set_color('red')
    ylabel_obj2 = plt.ylabel('Jumlah total pengguna sepeda',fontsize=6)
    ylabel_obj2.set_color('green')

    # Mengubah warna teks di dalam legend untuk subplot kedua
    for text, color in zip(legend2.get_texts(), sns.color_palette('viridis', 3)):
        text.set_color(color)

    plt.tight_layout()
    st.pyplot(plt)

st.markdown("<h5 style='font-size: 20px;'>Faktor yang mempengaruhi jumlah pengguna sepeda setiap hari</h5>",
unsafe_allow_html=True)
create_plots_1()


groupby_2 = df_day_cleaned_2.groupby(['weathersit']).agg({
    'casual': ['mean', 'sum'],
    'registered': ['mean', 'sum'],
    'temp': 'mean',
    'atemp': 'mean',
    'hum': 'mean',
    'windspeed': 'mean'
}).reset_index()

# Merename/mengatur nama kolom hasil agregasi agar lebih jelas
groupby_2.columns = ['weathersit', 'casual_mean', 'casual_sum',
                     'registered_mean', 'registered_sum', 'temp_mean',
                     'atemp_mean', 'hum_mean', 'windspeed_mean']

# Mengatur style untuk plot
sns.set(style="whitegrid")

# Fungsi untuk membuat plot
def create_plots_2():
    plt.figure(figsize=(8, 5))

    # Bar plot untuk casual users
    plt.subplot(1, 2, 1)
    sns.barplot(x='weathersit', y='casual_mean', hue='weathersit', data=groupby_2, palette='viridis')
    plt.title('Jumlah rata-rata Casual Users berdasarkan Kondisi Cuaca',fontsize=7)
    plt.xlabel('Kondisi Cuaca',fontsize=6)
    plt.ylabel('Jumlah rata-rata Casual Users',fontsize=6)
    plt.xticks([0, 1, 2], ['Clear/Partly Cloudy', 'Mist/Cloudy', 'Light Snow/Rain'],fontsize=6)
    xlabel_obj1 = plt.xlabel('Kondisi Cuaca',fontsize=6)
    xlabel_obj1.set_color('red')
    ylabel_obj1 = plt.ylabel('Jumlah rata-rata Casual Users',fontsize=6)
    ylabel_obj1.set_color('green')

    # Bar plot untuk registered users
    plt.subplot(1, 2, 2)
    sns.barplot(x='weathersit', y='registered_mean', hue='weathersit', data=groupby_2, palette='viridis')
    plt.title('Jumlah rata-rata Registered Users berdasarkan Kondisi Cuaca',fontsize=7)
    plt.xlabel('Kondisi Cuaca',fontsize=6)
    plt.ylabel('Jumlah rata-rata Registered Users',fontsize=6)
    plt.xticks([0, 1, 2], ['Clear/Partly Cloudy', 'Mist/Cloudy', 'Light Snow/Rain'],fontsize=6)
    xlabel_obj2 = plt.xlabel('Kondisi Cuaca',fontsize=6)
    xlabel_obj2.set_color('red')
    ylabel_obj2 = plt.ylabel('Jumlah rata-rata Registered Users',fontsize=6)
    ylabel_obj2.set_color('green')
    
    plt.tight_layout()
    st.pyplot(plt)

# Pengaturan Streamlit
st.markdown("<h5 style='font-size: 20px;'>Analisis Pengguna Sepeda berdasarkan Kondisi Cuaca</h5>",
 unsafe_allow_html=True)
create_plots_2()

groupby_3 = df_hour_cleaned_3.groupby(['hr', 'weekday', 'workingday']).agg({
    'casual': 'sum',
    'registered': 'sum',
    'cnt': 'sum'
}).reset_index()

# Merename/mengatur nama kolom hasil agregasi agar lebih jelas
groupby_3.columns = ['hours', 'weekday','workingday', 'casual_sum',
                     'registered_sum', 'count_sum']


# Mengatur style untuk plot
sns.set(style="whitegrid")
def create_plots_3():
    workingday_data = groupby_3[groupby_3['workingday'] == 1]
    weekend_data = groupby_3[groupby_3['workingday'] == 0]

    plt.figure(figsize=(20, 7))

    # Hari kerja
    plt.subplot(1, 2, 1)
    sns.barplot(data=workingday_data, x='hours', y='count_sum', hue='weekday')
    plt.title('Penggunaan Sepeda pada Hari Kerja')
    plt.xlabel('Hour')
    plt.ylabel('Jumlah pengguna sepeda')
    title_obj1 = plt.title('Penggunaan Sepeda pada Hari Kerja')
    title_obj1.set_color('blue')
    xlabel_obj1 = plt.xlabel('Hour')
    xlabel_obj1.set_color('red')
    ylabel_obj1 = plt.ylabel('Jumlah pengguna sepeda')
    ylabel_obj1.set_color('green')

    # Akhir pekan
    plt.subplot(1, 2, 2)
    sns.barplot(data=weekend_data, x='hours', y='count_sum', hue='weekday')
    plt.title('Penggunaan Sepeda pada Akhir Pekan')
    plt.xlabel('Hour')
    plt.ylabel('Jumlah pengguna sepeda')
    title_obj2 = plt.title('Penggunaan Sepeda pada Akhir Pekan')
    title_obj2.set_color('blue')
    xlabel_obj2 = plt.xlabel('Hour')
    xlabel_obj2.set_color('red')
    ylabel_obj2 = plt.ylabel('Jumlah pengguna sepeda')
    ylabel_obj2.set_color('green')

    plt.tight_layout()
    st.pyplot(plt)
# Pengaturan Streamlit
st.markdown("<h5 style='font-size: 20px;'>Analisis variasi penggunaan sepeda selama hari kerja dan akhir pekan</h5>",
 unsafe_allow_html=True)
create_plots_3()

# Defisi rush hours (misal 7-9 AM dan 5-7 PM)
rush_hours = [7, 8, 9, 17, 18, 19]

# Filter data untuk rush hours
rush_hour_df4 =df_hour_cleaned_4[df_hour_cleaned_4['hr'].isin(rush_hours)]

# Data dikelompokkan berdasarkan hr, temp, dan hum.
groupby_4 = rush_hour_df4.groupby(['hr', 'temp', 'hum']).agg({
    'casual': 'sum',
    'registered': 'sum',
    'cnt': 'sum'
}).reset_index()

groupby_4.columns = ['hours', 'temp','hum', 'casual_sum',
                     'registered_sum', 'count_sum']


def create_plots_4():
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=groupby_4, x='temp', y='count_sum', hue='hours', palette='coolwarm')
    plt.title('Pengaruh Suhu terhadap Jumlah Pengguna Sepeda pada Jam Sibuk',fontsize =7)
    plt.xlabel('Suhu',fontsize =6)
    plt.ylabel('Jumlah Pengguna Sepeda',fontsize =6)
    plt.legend(title='Jam',fontsize =6)
    title_obj1 = plt.title('Pengaruh Suhu terhadap Jumlah Pengguna Sepeda pada Jam Sibuk',fontsize =6)
    title_obj1.set_color('blue')
    xlabel_obj1 = plt.xlabel('Suhu',fontsize =6)
    xlabel_obj1.set_color('red')
    ylabel_obj1 = plt.ylabel('Jumlah pengguna sepeda',fontsize =6)
    ylabel_obj1.set_color('green')
    st.pyplot(plt)

    # Visualisasi pengaruh kelembaban terhadap jumlah pengguna sepeda
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=groupby_4, x='hum', y='count_sum', hue='hours', palette='coolwarm')
    plt.title('Pengaruh Kelembaban terhadap Jumlah Pengguna Sepeda pada Jam Sibuk',fontsize =7)
    plt.xlabel('Kelembaban',fontsize =6)
    plt.ylabel('Jumlah Pengguna Sepeda',fontsize =6)
    plt.legend(title='Jam',fontsize =6)
    title_obj2 = plt.title('Pengaruh Kelembaban terhadap Jumlah Pengguna Sepeda pada Jam Sibuk',fontsize =6)
    title_obj2.set_color('blue')
    xlabel_obj2 = plt.xlabel('Kelembaban',fontsize =6)
    xlabel_obj2.set_color('red')
    ylabel_obj2 = plt.ylabel('Jumlah pengguna sepeda')
    ylabel_obj2.set_color('green')
    st.pyplot(plt)

st.markdown("<h5 style='font-size: 20px;'>Analisis Pengaruh Suhu dan Kelembaban terhadap Jumlah Pengguna Sepeda pada Jam Sibuk</h5>",
 unsafe_allow_html=True)
create_plots_4()



