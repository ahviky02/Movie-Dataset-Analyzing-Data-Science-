import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Function to extract movie information
def movies_info(row):
    title = row["names"].values[0]
    release_date = row["date_x"].values[0]
    genre = row["genre"].values[0]
    rating = row["score"].values[0] / 10
    summary = row["overview"].values[0]
    budget = row["budget_x"].values[0]
    revenue = row["revenue"].values[0]
    country = row["country"].values[0]

    return [title, release_date, genre, rating, summary, budget, revenue, country]


def show_info(data, st):
    movie = st.selectbox("Select a movie:", data["names"])

    selected_movie_row = data[data["names"] == movie]

    info = movies_info(selected_movie_row)

    table = f"""<table style="border-collapse: collapse;border:0px solid black;">
    <tr>
        <td>Title </td>
        <td>{info[0]}</td>
    </tr>
    <tr>
        <td>Release date</td>
        <td>{info[1]}</td>
    </tr>
    <tr>
        <td>Genre</td>
        <td>{info[2]}</td>
    </tr>
    <tr>
        <td>Rating</td>
        <td>{info[3]}</td>
    </tr>
    <tr>
        <td>Country</td>
        <td>{info[7]}</td>
    </tr>
    <tr>
        <td>Budget</td>
        <td>{info[5]}</td>
    </tr>
    <tr>
        <td>Revenue</td>
        <td>{info[6]}</td>
    </tr>
    <tr>
        <td>Overview</td>
        <td>{info[4]}</td>
    </tr>
</table>"""

    st.markdown(table, unsafe_allow_html=True)
