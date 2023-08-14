import streamlit as st
import pandas as pd
import requests
import wikipediaapi
from info import *
from filter import *


def main():
    # read data from pickle file
    data = pd.read_pickle("data.pickle")

    # Create a tab menu
    pages = ["Movie", "Filter", "Visualization"]
    Movie, Filter, Visualization = st.tabs(pages)

    with Movie:
        st.write(f"{pages[0]}")
        show_info(data, st)

    with Filter:
        genre(data, st)

    with Visualization:
        st.write(f"{pages[2]}")


if __name__ == "__main__":
    main()
