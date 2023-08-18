import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import requests
import wikipediaapi
from info import *
from filter import *
from visualize import *
from collections import Counter
import math
import matplotlib.ticker as ticker


def main():
    # read data from pickle file
    data = pd.read_pickle("data.pickle")

    # Create a tab menu
    pages = ["Movie", "Filter", "Genre", "Language", "Year", "About Us", "Contact Us"]
    Movie, Filter, Genre, Language, Year, About, Contact = st.tabs(pages)

    with Movie:
        st.subheader(f"{pages[0]}")
        show_info(data, st)

    with Filter:
        st.subheader(f"{pages[1]}")
        genre(data, st)

    with Genre:
        st.subheader(f"{pages[2]}")
        # Language selection
        selected_language = st.checkbox("Select Language")
        if selected_language:
            vllang = st.selectbox("Select Language", data["orig_lang"].unique())
            vlcount = st.radio(
                "Select results",
                [3, 5, 8, 10, 15],
                horizontal=True,
                format_func=lambda x: f"{x} genre",
            )
            chart = ["Pie", "Bar", "No"]
            vlchart = st.radio(
                "Select chart type",
                chart,
                horizontal=True,
                format_func=lambda x: f"{x} Chart",
            )

            genlist = vgenlang(data, vllang)
            genre_counts = Counter(genlist)
            genres = list(genre_counts.keys())
            charvalue = genre_counts.most_common()[0:vlcount]
            X = list()
            Y = list()
            for gen, value in charvalue:
                X.append(value)
                Y.append(gen)
            # Check the selected chart type
            if vlchart == "Pie":
                st.subheader(f"Top {vlcount} Genre in {vllang}")
                plt.close()
                vl = plt
                vl.figure(figsize=(13, 9))
                patches, texts, autotexts = vl.pie(
                    X,
                    labels=Y,
                    radius=0.9,
                    autopct="%1.1f%%",
                )
                for autotext in autotexts:
                    autotext.set_fontsize(12)
                vl.title("Pie Chart with Percentages")
                st.pyplot(vl)
            elif vlchart == "Bar":
                vlb = sns
                vlb.set_theme()
                plt.figure(figsize=(13, 9))
                ax = vlb.barplot(x=Y, y=X)
                plt.title("Bar Chart with Values")

                # Add percentage labels on top of bars
                total = sum(X)
                for p in ax.patches:
                    percentage = (p.get_height() / total) * 100
                    ax.annotate(
                        f"{percentage:.1f}%",
                        (p.get_x() + p.get_width() / 2.0, p.get_height()),
                        ha="center",
                        va="bottom",
                        fontsize=10,
                    )

                st.pyplot(plt)
        else:
            vllang = 0
            vlcount = st.radio(
                "Select results",
                [3, 5, 8, 10, 15],
                horizontal=True,
                format_func=lambda x: f"{x} genre",
            )
            chart = ["Pie", "Bar", "No"]
            vlchart = st.radio(
                "Select chart type",
                chart,
                horizontal=True,
                format_func=lambda x: f"{x} Chart",
            )

            genlist = vgenlang(data, vllang)
            genre_counts = Counter(genlist)
            genres = list(genre_counts.keys())
            charvalue = genre_counts.most_common()[0:vlcount]
            X = list()
            Y = list()
            for gen, value in charvalue:
                X.append(value)
                Y.append(gen)
            # Check the selected chart type
            st.subheader(f"Top {vlcount} Genre in All Languages")
            if vlchart == "Pie":
                vl = plt
                vl.figure(figsize=(13, 9))
                patches, texts, autotexts = vl.pie(
                    X,
                    labels=Y,
                    radius=0.9,
                    autopct="%1.1f%%",
                )
                for autotext in autotexts:
                    autotext.set_fontsize(12)
                vl.title("Pie Chart with Percentages")
                st.pyplot(vl)
            elif vlchart == "Bar":
                vlb = sns
                vlb.set_theme()
                plt.figure(figsize=(13, 9))
                ax = vlb.barplot(x=Y, y=X)
                plt.title("Bar Chart with Values")

                # Add percentage labels on top of bars
                total = sum(X)
                for p in ax.patches:
                    percentage = (p.get_height() / total) * 100
                    ax.annotate(
                        f"{percentage:.1f}%",
                        (p.get_x() + p.get_width() / 2.0, p.get_height()),
                        ha="center",
                        va="bottom",
                        fontsize=10,
                    )

                st.pyplot(plt)

    with Language:
        st.subheader(f"{pages[3]}")
        st.subheader("Choose For Which Element Based Want to Show Result")
        lbase = st.radio(
            "Select", ["Rating", "Most Used", "Budget", "Revenue"], horizontal=True
        )
        lcount = st.radio(
            "Select No of Result",
            [3, 5, 8, 10, 15],
            horizontal=True,
            format_func=lambda x: f"{x} language",
        )
        ulang = data["orig_lang"].value_counts()
        language = ulang.head(lcount)

        if lbase == "Rating":
            st.subheader(f"{lbase} Based Top {lcount} Languages")
            ulang_rate = list()
            for item in ulang.index:
                score = data[data["orig_lang"] == item]
                mean_score = score["score"].mean()
                ulang_rate.append(mean_score)
            # st.write()
            plt.close()
            plt.figure(figsize=(13, 9))
            plt.pie(
                ulang_rate[0:lcount], labels=ulang.index[0:lcount], autopct="%1.1f%%"
            )
            st.pyplot(plt)

        elif lbase == "Most Used":
            st.subheader(f"{lbase} Based Top {lcount} Languages")
            plt.close()
            plt.figure(figsize=(13, 9))
            plt.pie(language, labels=language.index, autopct="%1.1f%%")
            st.pyplot(plt)

        elif lbase == "Budget":
            st.subheader(f"{lbase} Based Top {lcount} Languages")
            ulang_rate = list()
            for item in ulang.index:
                score = data[data["orig_lang"] == item]
                mean_score = score["budget_x"].mean()
                ulang_rate.append(mean_score)
            # st.write()
            plt.close()
            plt.figure(figsize=(13, 9))
            plt.pie(
                ulang_rate[0:lcount], labels=ulang.index[0:lcount], autopct="%1.1f%%"
            )
            st.pyplot(plt)

        elif lbase == "Revenue":
            st.subheader(f"{lbase} Based Top {lcount} Languages")
            ulang_rate = list()
            for item in ulang.index:
                score = data[data["orig_lang"] == item]
                mean_score = score["revenue"].mean()
                ulang_rate.append(mean_score)
            # st.write()
            plt.close()
            plt.figure(figsize=(13, 9))
            plt.pie(
                ulang_rate[0:lcount], labels=ulang.index[0:lcount], autopct="%1.1f%%"
            )
            st.pyplot(plt)

    with Year:
        st.subheader(f"{pages[4]}")
        st.header("Year Wise Relation Between Budget and Revenue")
        option = st.radio(
            "Select The Type of Year", ["Year", "All", "Range"], horizontal=True
        )
        if option == "Year":
            year = st.selectbox(
                "Select The Yaer", np.sort(data["date_x"].str[-5:].astype(int).unique())
            )

            b = data[data["date_x"].str.contains(str(year))]
            budget = b["budget_x"].mean()
            revenue = b["revenue"].mean()
            plt.close()
            plt.figure(figsize=(8, 5))

            # Create a bar chart with labels and X-axis ticks
            plt.bar(["Budget", "Revenue"], [budget, revenue], width=0.2)
            ax = plt.gca()
            total_count = budget + revenue
            for i, count in enumerate([budget, revenue]):
                percentage = (count / total_count) * 100
                ax.text(i, count, f"{percentage:.1f}%", ha="center", va="bottom")
            # Add labels and title
            plt.xlabel("Ammount in Cr")
            plt.ylabel("Budget & Revenue")
            plt.title("Mean Budget and Revenue Comparison")
            st.pyplot(plt)

        elif option == "All":
            b = data
            budget = b["budget_x"].mean()
            revenue = b["revenue"].mean()
            plt.close()
            plt.figure(figsize=(8, 5))

            # Create a bar chart with labels and X-axis ticks
            plt.bar(["Budget", "Revenue"], [budget, revenue], width=0.2)
            ax = plt.gca()
            total_count = budget + revenue
            for i, count in enumerate([budget, revenue]):
                percentage = (count / total_count) * 100
                ax.text(i, count, f"{percentage:.1f}%", ha="center", va="bottom")
            # Add labels and title
            plt.xlabel("Ammount in Cr")
            plt.ylabel("Budget & Revenue")
            plt.title("Mean Budget and Revenue Comparison")
            st.pyplot(plt)

        elif option == "Range":
            lower = st.selectbox(
                "Select The Lower Yaer",
                np.sort(data["date_x"].str[-5:].astype(int).unique()),
            )
            upper = st.selectbox(
                "Select The Upper Yaer",
                np.sort(data["date_x"].str[-5:].astype(int).unique()),
            )

            aggregated_data = []
            for year in range(lower, upper + 1):
                b = data[data["date_x"].str.contains(str(year))]
                budget_mean = b["budget_x"].mean()
                revenue_mean = b["revenue"].mean()
                aggregated_data.append(
                    {"year": year, "budget": budget_mean, "revenue": revenue_mean}
                )

            df = pd.DataFrame(aggregated_data)
            df.dropna(inplace=True)

            plt.close()
            plt.figure(figsize=(10, 5))

            plt.plot(df["year"], df["budget"], label="Total Budget", linewidth=3)
            plt.plot(df["year"], df["revenue"], label="Total Revenue", linewidth=3)

            # Adding labels and title
            plt.xlabel("Year")
            plt.ylabel("Amount")
            plt.title("Total Budget vs Total Revenue")

            # Adding a legend to differentiate the two lines
            plt.legend()

            def crore_formatter(x, pos):
                return f"{x/1e7:.0f} Cr"

            # Adding ticker to show the year on the x-axis as integers
            plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(10))
            plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(crore_formatter))
            st.pyplot(plt)

    with About:
        st.subheader(f"About Us")
        st.write(
            f"   We have a dataset related to movies named 'movie.csv.' Our goal is to analyze the data and determine which types of movies are in high demand among the public and which types of movies can potentially gain maximum profits. "
        )

        st.header("Conclusion")
        st.subheader("1.Language Preference:")
        st.write(
            " The dataset highlights the English language as the dominant choice for movies, indicating its widespread usage in the global film industry. This insight underscores the importance of producing English-language films to cater to a broader international audience."
        )
        st.subheader("2.Popular Movie Genres:")
        st.write(
            " Our analysis has revealed five movie genres that have consistently garnered high popularity and strong public demand. These genres have the potential to attract large audiences and lead to commercial success."
        )

        st.subheader("3.Financial Performance Over Time: ")
        st.write(
            "Our year-wise examination of movie budgets and revenues from 2004 to 2023 has shown fluctuations in both aspects. Despite these variations, the film industry has demonstrated overall profitability, with revenues exhibiting a positive upward trend over the years. This data reflects the resilience of the movie business and its ability to remain financially viable even in the face of budget fluctuations."
        )

        st.write(
            "By harnessing these valuable insights, filmmakers, producers, and investors can make data-driven decisions to maximize their chances of success in the ever-evolving film industry. Understanding language preferences, genre trends, and financial patterns empowers stakeholders to create compelling movies that resonate with audiences and yield substantial returns on investment."
        )

    with Contact:
        st.subheader(f"Contact Us")
        st.subheader("My name is Avdhesh Kumar Yadav. I'm owener of this website..")
        st.write(
            "Linkedn Id : https://www.linkedin.com/in/avdhesh-kumar-yadav-62514b243/"
        )
        st.write("Email Id : ahviy2002@outlook.com")


if __name__ == "__main__":
    main()
