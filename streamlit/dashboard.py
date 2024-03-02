#Dashboard Streamlit

#By : Kamal Ibrahim
#ID Dicoding : https://www.dicoding.com/users/kamalibrahim62/
#Email : m295d4ky1852@bangkit.academy

# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# LOAD DATA

@st.cache_resource
def load_data():
    data = pd.read_csv("./dataset/hour.csv")
    return data


data = load_data()


# TITLE DASHBOARD
# Set page title
st.title("Bike Sharing Analysis Dashboard")

# SIDEBAR
st.sidebar.title("Contact Person:")
st.sidebar.markdown("**• Kamal Ibrahim**")
st.sidebar.markdown(
    "**• Email: [m295d4ky1852@bangkit.academy](m295d4ky1852@bangkit.academy)**")
st.sidebar.markdown(
    "**• ID Dicoding: [kamalibrahim62](https://www.dicoding.com/users/kamalibrahim62/)**")
st.sidebar.markdown(
    "**• LinkedIn: [Kamal Ibrahim](https://www.linkedin.com/in/kamal-ibrahim-a67116221/)**")



st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://www.kaggle.com/code/ramanchandra/bike-sharing-data-analysis)")


# VISUALIZATION


# yearly bike share count
# st.subheader("Hourly Bike Share Count")
yearly_count = data.groupby("yr")["cnt"].sum().reset_index()
fig_yearly_count = px.line(
    yearly_count, x="yr", y="cnt", title="Jumlah Jam Penyewaan Sepeda per Tahun")
st.plotly_chart(fig_yearly_count, use_container_width=True,
                height=400, width=600)

# daily bike share count
# st.subheader("Hourly Bike Share Count")
dteday_count = data.groupby("dteday")["cnt"].sum().reset_index()
fig_dteday_count = px.line(
    dteday_count, x="dteday", y="cnt", title="Jumlah Penyewaan Sepeda per Tanggal")
st.plotly_chart(fig_dteday_count, use_container_width=True,
                height=400, width=600)


# Show data source and description
st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan visualisasi untuk sekumpulan data Bike Share. "
                "Dataset ini mengandung informasi mengenai penyewaan sepeda berdasarkan berbagai variabel seperti musim, suhu, kelembaban, dan faktor lainnya.")
