from filter import *
import matplotlib.pyplot as plt


def Pie(x, y):
    plt.pie(y, labels=x, radius=10)
    return plt


def lgenre_unique(data):
    data["new_genre"] = data["genre"].str.replace("\xa0", "")
    genlist = []
    for item in data["new_genre"]:
        genres_list = item.split(",")
        for gen in genres_list:
            genlist.append(gen.strip())

    return genlist


def vgenlang(data, language):
    if language:
        x = data[data["orig_lang"] == language]
        y = lgenre_unique(x)
        # y = x["genre"]  # Assuming "genre" is a column in your dataset
        # z = pd.Series(y).value_counts().head(count)
        return y
    else:
        x = x = data[data["orig_lang"] != language]
        y = lgenre_unique(x)
        return y


# def vlanguage():
