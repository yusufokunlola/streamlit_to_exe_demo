# import libraries
import streamlit as st
import pandas as pd

# Set up page configuration
st.set_page_config(page_title="Streamlit to EXE App Demo", page_icon="🧑🏻‍💻")

# Create app title
st.title("Streamlit to EXE App Demo 🧑🏻‍💻")

# Sidebar
st.sidebar.write("**App Information**")
st.sidebar.write(
    """
    This application allows users to calculate the square of a number and preview the contents of an uploaded `CSV` file. 
    """ )

st.sidebar.write("#### Usage Guide")
st.sidebar.write(
    """
    1. Move the slider to select a number, and the square of that number will be displayed.
    2. Click the **Browse files** button to select a `CSV` file, or simply drag and drop it onto the screen. The contents of the file will be shown below.
    """
)

st.sidebar.write("**Created by: [Yusuf Okunlola](https://www.linkedin.com/in/yusufokunlola/)**")
st.sidebar.write("#### `December 18, 2024`")


# Create a slider that calculates the square of a number
st.write("**Square of a number**")
x = st.slider("Select a value", min_value=1, max_value=500, step=1)
st.write(f"The square of **{x}** is **{x ** 2}**.")

# file uploader
uploaded_file = st.file_uploader("**Upload CSV File**", type=["csv"])

if uploaded_file:
    # Load the uploaded file into a DataFrame
    df = pd.read_csv(uploaded_file)
    st.write("**Uploaded Data**")
    st.dataframe(df)  
    
else:
    st.warning("Please upload a CSV file.")