import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()


with header:
    st.title("Diamonds Price Forecasting")
    st.text("This is a small project to develope a model that best fits the values and predict the best")

with dataset:
    st.header("Diamons price dataset")
    st.text("I got this dataset on Kaggle, .....")

    diamond_data = pd.read_csv("csv\diamonds_price2022.csv")
    st.write(diamond_data.head())


with features:
    st.header("Features")
    st.markdown("* **first feature:** I create this thing because of the invastigating...")
    st.markdown("* **second feature:** I create this thing because of the invastigating...")



with model_training:
    st.header("Model_training")
    st.text("explain what i did ...")

    sel_col, disp_col = st.columns(2)
    
    sel_col.subheader("imput")
    