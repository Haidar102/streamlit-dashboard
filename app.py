#Here we go!
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Titanic Dashboard")

st.set_page_config(layout="wide")

df = pd.read_csv("titanic_data.csv")

df['Embarked']= df['Embarked'].fillna('Unknown')

#get unique values for embarked port

embarked_port = df['Embarked'].unique().tolist()
geneder = list(df['Sex'].unique())

col1, col2 = st.columns([1,1])
selected_port = col1.selectbox(options=embarked_port, label="Select a Port")
selected_gender = col2.selectbox(options=geneder, label="Select a Gender")

#filter data based on selection
df_plot = df[(df['Embarked'] == selected_port)]
df_plot = df_plot[(df_plot['Sex'] == selected_gender)]


plot = px.histogram(data_frame=df_plot, x='Age', color='Survived', barmode='group',
                    title="Age Distribution of Age",template='seaborn',facet_col='Survived')

col1.plotly_chart(plot)