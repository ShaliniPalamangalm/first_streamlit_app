import streamlit
streamlit.title("My Parents New Healthy Dinner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry oatmeal")
streamlit.text("Kale,Spinach and Rocket Smoothie")
streamlit.text("Hard boiled free range Menu")               
streamlit.text("Avacado Toastie")  

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
