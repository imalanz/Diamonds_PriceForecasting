import streamlit as st
import pandas as pd

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
    st.title("Diamonds Price Forecasting")
    st.text("This is a small project to develope a model that best fits the values and predict the best")


with dataset:
    st.header("Diamons price dataset")
    st.text("I got this dataset on Kaggle, .....")

    diamond_data = pd.read_csv("csv/diamond_price2022")
    st.write(diamond_data.head())



