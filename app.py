import streamlit as st
import pandas as pd

df = pd.read_csv('titanic_data.csv')


def main():
   st.title("Curso de Streamlit")
   st.header("Dataframe:")
   st.dataframe(df)


if __name__ == '__main__':
    main()