import requests
from bs4 import BeautifulSoup
import json

url = "https://www.rottentomatoes.com/m/the_super_mario_bros_movie"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

# Movie title
title = soup.title.text.strip()

# Scores
score_data = {
    "Tomatometer": None,
    "Audience Score": None,
    "Critics Avg": None,
    "Audience Avg": None
}

json_tag = soup.find("script", {"id": "media-scorecard-json"})

if json_tag:
    data = json.loads(json_tag.string)

    score_data["Tomatometer"] = data.get("criticsScore", {}).get("score")
    score_data["Audience Score"] = data.get("audienceScore", {}).get("score")
    score_data["Critics Avg"] = data.get("criticsScore", {}).get("averageRating")
    score_data["Audience Avg"] = data.get("audienceScore", {}).get("averageRating")

# Movie info
info = {}

items = soup.find_all("div", {"data-qa": "item"})

for item in items:
    label = item.find("rt-text", {"data-qa": "item-label"})
    values = item.select('[data-qa="item-value"]')  # handles rt-text + rt-link
    
    if label and values:
        key = label.text.strip()
        val = ", ".join([v.text.strip() for v in values])
        info[key] = val

rating = info.get("Rating")
genre = info.get("Genre")
box_office = info.get("Box Office (Gross USA)")

# Output
print("\n--- Movie Data ---\n")

print(f"{'Title:':25} {title}")
print(f"{'Tomatometer:':25} {score_data['Tomatometer']}")
print(f"{'Audience Score:':25} {score_data['Audience Score']}")
print(f"{'Critics Avg:':25} {score_data['Critics Avg']}")
print(f"{'Audience Avg:':25} {score_data['Audience Avg']}")
print(f"{'Rating:':25} {rating}")
print(f"{'Genre:':25} {genre}")
print(f"{'Box Office (USA):':25} {box_office}")

import requests
from bs4 import BeautifulSoup
import json
import time
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0"}

GUIDE_URL = "https://editorial.rottentomatoes.com/guide/oscars-best-and-worst-best-pictures/"


# Movie links
def get_movie_links_from_guide():
    res = requests.get(GUIDE_URL, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    movie_urls = set()

    # All Rotten Tomatoes movie pages are /m/...
    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "/m/" in href and "rottentomatoes.com" in href:
            movie_urls.add(href.split("?")[0])

        elif href.startswith("/m/"):
            movie_urls.add("https://www.rottentomatoes.com" + href.split("?")[0])

    return list(movie_urls)


# Scrape 1 movie
def scrape_movie(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.title.text.strip() if soup.title else None

    score_data = {
        "Tomatometer": None,
        "Audience Score": None,
        "Critics Avg": None,
        "Audience Avg": None
    }

    json_tag = soup.find("script", {"id": "media-scorecard-json"})
    if json_tag:
        data = json.loads(json_tag.string)
        score_data["Tomatometer"] = data.get("criticsScore", {}).get("score")
        score_data["Audience Score"] = data.get("audienceScore", {}).get("score")
        score_data["Critics Avg"] = data.get("criticsScore", {}).get("averageRating")
        score_data["Audience Avg"] = data.get("audienceScore", {}).get("averageRating")

    info = {}
    for item in soup.find_all("div", {"data-qa": "item"}):
        label = item.find("rt-text", {"data-qa": "item-label"})
        values = item.select('[data-qa="item-value"]')

        if label and values:
            key = label.text.strip()
            val = ", ".join(v.text.strip() for v in values)
            info[key] = val

    return {
        "Title": title,
        "URL": url,
        **score_data,
        "Rating": info.get("Rating"),
        "Genre": info.get("Genre"),
        "Box Office (USA)": info.get("Box Office (Gross USA)")
    }


# Run on list
movie_urls = get_movie_links_from_guide()

print(f"Found {len(movie_urls)} movie links")

results = []

for i, url in enumerate(movie_urls):
    try:
        print(f"[{i+1}/{len(movie_urls)}] Scraping {url}")
        results.append(scrape_movie(url))
        time.sleep(1)  # be polite
    except Exception as e:
        print(f"Failed {url}: {e}")


# Output
df = pd.DataFrame(results)
print(df)

df.to_csv("oscars_best_worst_movies.csv", index=False)

import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("oscars_best_worst_movies.csv")

# Clean data
df["Tomatometer"] = pd.to_numeric(df["Tomatometer"], errors="coerce")
df["Audience Score"] = pd.to_numeric(df["Audience Score"], errors="coerce")
df["Critics Avg"] = pd.to_numeric(df["Critics Avg"], errors="coerce")
df["Audience Avg"] = pd.to_numeric(df["Audience Avg"], errors="coerce")

def parse_box_office(x):
    if pd.isna(x):
        return None
    x = str(x).replace("$", "").replace("M", "")
    try:
        return float(x)
    except:
        return None

df["Box Office (USA)"] = df["Box Office (USA)"].apply(parse_box_office)

df_clean = df.dropna(subset=["Tomatometer", "Audience Score"])

# Fill missing box office
df_clean["Box Office (USA)"] = df_clean["Box Office (USA)"].fillna(0)

# scale for bubble size
df_clean["Box Office Size"] = df_clean["Box Office (USA)"] / 10


# Scatterplot
fig1 = px.scatter(
    df_clean,
    x="Tomatometer",
    y="Audience Score",
    color="Box Office (USA)",
    size="Box Office Size",
    hover_name="Title",
    hover_data=["Critics Avg", "Audience Avg", "Rating", "Genre"],
    title="Critics vs Audience Scores (Bubble = Box Office)"
)
fig1.show()


# Genre Analysis
df_genre = df_clean.assign(Genre=df_clean["Genre"].str.split(", ")).explode("Genre")

fig2 = px.box(
    df_genre,
    x="Genre",
    y="Tomatometer",
    color="Genre",
    title="Critics Scores by Genre"
)
fig2.update_layout(xaxis_tickangle=-45)
fig2.show()


# Rating Analysis
df_clean["Rating Clean"] = df_clean["Rating"].astype(str).str.split(" ").str[0]

fig3 = px.box(
    df_clean,
    x="Rating Clean",
    y="Audience Score",
    color="Rating Clean",
    title="Audience Scores by MPAA Rating (Cleaned)"
)

fig3.show()


# Critics vs audience
fig4 = px.scatter(
    df_clean,
    x="Critics Avg",
    y="Audience Avg",
    hover_name="Title",
    color="Box Office (USA)",
    size="Box Office Size",
    title="Critics Avg vs Audience Avg Ratings"
)
fig4.show()


# Box Office
fig5 = px.histogram(
    df_clean,
    x="Box Office (USA)",
    nbins=20,
    title="Box Office Distribution (USA)"
)
fig5.show()
