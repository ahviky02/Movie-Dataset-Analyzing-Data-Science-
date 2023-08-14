from collections import Counter


# this for selct unique genre
def unique_genre(data):
    data["new_genre"] = data["genre"].str.replace("\xa0", "")
    genlist = []
    for item in data["new_genre"]:
        genres_list = item.split(",")
        for gen in genres_list:
            genlist.append(gen.strip())
    genre_counts = Counter(genlist)
    genres = list(genre_counts.keys())
    return genres, genre_counts


# this for selct unique language


def unique_lang(data):
    return data["orig_lang"].unique()


def gen_res(selected_genre, selected_lang, selected_count_g, data):
    x = data[data["orig_lang"] == selected_lang]
    y = x[x["new_genre"].str.contains(selected_genre)]  # Fixed filtering by genre
    y_sorted = y.sort_values(by="score", ascending=False)
    return y_sorted["names"].head(selected_count_g).to_list()


def genre(data, st):
    st.header("Genre")
    selected_genre = st.selectbox("Select a genre", unique_genre(data)[0])
    st.write(f"You selected: {selected_genre}")

    st.header("Language")
    selected_lang = st.selectbox("Select a Language", unique_lang(data))
    st.write(f"You selected: {selected_lang}")

    st.header("Top Result")
    count = [3, 5, 10, 15, 20]
    selected_count_g = st.radio(
        "Select Top Result",
        count,
        index=2,
        horizontal=True,
        format_func=lambda x: f"{x} movies",
    )
    st.write(f"You selected: {selected_count_g}")

    st.header(f"Top {selected_count_g} {selected_genre} {selected_lang} Movies:")
    st.write(gen_res(selected_genre, selected_lang, selected_count_g, data))
