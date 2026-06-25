import streamlit as st
import pandas as pd

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

# ---------------- BACKGROUND STYLE ----------------
st.markdown("""
<style>

.stApp {
    background-image: url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.main-box {
    background: rgba(0,0,0,0.75);
    padding: 30px;
    border-radius: 20px;
}

h1,h2,h3,h4,p,label {
    color: white !important;
}

.stButton button {
    background-color: #ff4b5c;
    color: white;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- MOVIE DATA ----------------
movies = pd.DataFrame({

    "title": [

        "Avatar",
        "Titanic",
        "Avengers: Endgame",
        "The Dark Knight",
        "Interstellar",
        "Inception",
        "Joker",
        "Frozen",
        "The Lion King",
        "Spider-Man: No Way Home",
        "Doctor Strange",
        "Iron Man",
        "Black Panther",
        "The Matrix",
        "Jurassic World",

        "3 Idiots",
        "Dangal",
        "Pathaan",
        "Jawan",
        "PK",
        "War",
        "Kabir Singh",
        "Drishyam",
        "Raazi",
        "Krrish",

        "Kantara",
        "KGF Chapter 1",
        "KGF Chapter 2",
        "777 Charlie",
        "Yuvarathnaa",
        "Roberrt",
        "James",
        "Vikrant Rona",
        "Ugramm",
        "Mungaru Male"

    ],

    "genre": [

        "Sci-Fi",
        "Romance",
        "Action",
        "Action",
        "Sci-Fi",
        "Sci-Fi",
        "Thriller",
        "Animation",
        "Animation",
        "Action",
        "Fantasy",
        "Action",
        "Action",
        "Sci-Fi",
        "Adventure",

        "Comedy",
        "Sports",
        "Action",
        "Action",
        "Comedy",
        "Action",
        "Romance",
        "Thriller",
        "Thriller",
        "Sci-Fi",

        "Action",
        "Action",
        "Action",
        "Drama",
        "Drama",
        "Action",
        "Action",
        "Fantasy",
        "Action",
        "Romance"
    ],

    "year": [

        2009,
        1997,
        2019,
        2008,
        2014,
        2010,
        2019,
        2013,
        1994,
        2021,
        2016,
        2008,
        2018,
        1999,
        2015,

        2009,
        2016,
        2023,
        2023,
        2014,
        2019,
        2019,
        2015,
        2018,
        2006,

        2022,
        2018,
        2022,
        2022,
        2021,
        2021,
        2022,
        2022,
        2014,
        2006
    ],

    "rating": [

        7.8,
        7.9,
        8.4,
        9.0,
        8.6,
        8.8,
        8.4,
        7.4,
        8.5,
        8.2,
        7.5,
        7.9,
        7.3,
        8.7,
        6.9,

        8.4,
        8.3,
        7.0,
        7.1,
        8.1,
        6.8,
        7.0,
        8.2,
        7.8,
        6.4,

        8.3,
        8.2,
        8.4,
        8.8,
        6.2,
        6.8,
        7.5,
        7.1,
        8.0,
        7.6
    ],

    "info": [

        "A marine explores the alien world Pandora.",
        "A romantic story on the Titanic ship.",
        "The Avengers fight to save the universe.",
        "Batman faces Joker in Gotham city.",
        "A journey through space and time.",
        "A thief enters dreams to steal secrets.",
        "A failed comedian becomes Joker.",
        "Two sisters discover magical powers.",
        "A lion prince returns to his kingdom.",
        "Spider-Man faces multiverse villains.",
        "A doctor learns magical powers.",
        "A billionaire becomes Iron Man.",
        "The king protects Wakanda.",
        "A hacker discovers hidden reality.",
        "Dinosaurs return in a theme park.",

        "Three students discover true success.",
        "A wrestler trains his daughters.",
        "A spy fights dangerous enemies.",
        "A man fights for justice.",
        "An alien questions human beliefs.",
        "Two agents battle terrorism.",
        "A doctor falls in love deeply.",
        "A man protects his family from police.",
        "A spy works secretly for India.",
        "A superhero gains special powers.",

        "A man protects forest traditions.",
        "Rocky rises in Kolar Gold Fields.",
        "Rocky fights powerful enemies.",
        "A man and dog share friendship.",
        "A student becomes a leader.",
        "A gangster fights evil forces.",
        "A soldier fights criminals.",
        "A hero protects magical secrets.",
        "A gangster rises to power.",
        "A romantic story during rainy season."
    ],

    "poster": [

        "https://image.tmdb.org/t/p/w500/kyeqWdyUXW608qlYkRqosgbbJyK.jpg",
        "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg",
        "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
        "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
        "https://image.tmdb.org/t/p/w500/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg",
        "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
        "https://image.tmdb.org/t/p/w500/kgwjIb2JDHRhNk13lmSxiClFjVk.jpg",
        "https://image.tmdb.org/t/p/w500/dzBtMocZuJbjLOXvrl4zGYigDzh.jpg",
        "https://image.tmdb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg",
        "https://image.tmdb.org/t/p/w500/uGBVj3bEbCoZbDjjl9wTxcygko1.jpg",
        "https://image.tmdb.org/t/p/w500/78lPtwv72eTNqFW9COBYI0dWDJa.jpg",
        "https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg",
        "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
        "https://image.tmdb.org/t/p/w500/jjBgi2r5cRt36xF6iNUEhzscEcb.jpg",

        "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
        "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
        "https://upload.wikimedia.org/wikipedia/en/c/c3/Pathaan_film_poster.jpg",
        "https://upload.wikimedia.org/wikipedia/en/3/39/Jawan_film_poster.jpg",
        "https://upload.wikimedia.org/wikipedia/en/c/c3/PK_poster.jpg",
        "https://upload.wikimedia.org/wikipedia/en/6/6c/War_official_poster.jpg",
        "https://upload.wikimedia.org/wikipedia/en/d/dc/Kabir_Singh.jpg",
        "https://upload.wikimedia.org/wikipedia/en/8/8a/Drishyam_2015_film.jpg",
        "https://upload.wikimedia.org/wikipedia/en/2/2f/Raazi_-_Poster.jpg",
        "https://upload.wikimedia.org/wikipedia/en/5/50/Krrish_Poster.jpg",

        "https://upload.wikimedia.org/wikipedia/en/8/84/Kantara_poster.jpeg",
        "https://upload.wikimedia.org/wikipedia/en/6/62/K.G.F_Chapter_1_poster.jpg",
        "https://upload.wikimedia.org/wikipedia/en/d/d7/K.G.F_Chapter_2.jpg",
        "https://upload.wikimedia.org/wikipedia/en/5/57/777_Charlie.jpg",
        "https://upload.wikimedia.org/wikipedia/en/4/4b/Yuvarathnaa.jpg",
        "https://upload.wikimedia.org/wikipedia/en/5/5d/Roberrt.jpg",
        "https://upload.wikimedia.org/wikipedia/en/3/31/James_2022_film.jpg",
        "https://upload.wikimedia.org/wikipedia/en/f/f5/Vikrant_Rona.jpg",
        "https://upload.wikimedia.org/wikipedia/en/8/85/Ugramm_poster.jpg",
        "https://upload.wikimedia.org/wikipedia/en/2/2d/MungaruMale.jpg"
    ]
})

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio("Menu", ["app", "about"])

selected_genre = st.sidebar.selectbox(
    "🎭 Select Genre",
    sorted(movies["genre"].unique())
)

# ---------------- APP ----------------
if menu == "app":

    st.markdown('<div class="main-box">', unsafe_allow_html=True)

    st.title("🎬 Movie Recommendation System")

    search_movie = st.text_input("🔍 Search Movie")

    movie_list = movies["title"].tolist()

    if search_movie:
        filtered_movies = [
            movie for movie in movie_list
            if search_movie.lower() in movie.lower()
        ]
    else:
        filtered_movies = movie_list

    selected_movie = st.selectbox(
        "🎥 Choose Movie",
        filtered_movies
    )

    num = st.slider(
        "⭐ Number of Recommendations",
        1, 3, 5
    )

    # ---------------- SELECTED MOVIE DETAILS ----------------

selected_data = movies[movies["title"] == selected_movie].iloc[0]

st.subheader("🎬 Selected Movie")

col1, col2 = st.columns([1, 3])

with col1:
    st.image(selected_data["poster"], width=220)

with col2:
    st.markdown(f"## {selected_data['title']}")
    st.write(f"📅 Year: {selected_data['year']}")
    st.write(f"🎭 Genre: {selected_data['genre']}")
    st.write(f"⭐ Rating: {selected_data['rating']}")
    st.write(f"📝 {selected_data['info']}")

# ---------------- RECOMMENDATION ----------------

if st.button("Get Recommendations"):

    movie_genre = selected_data["genre"]

    same_genre = movies[
        (movies["genre"] == movie_genre) &
        (movies["title"] != selected_movie)
    ]

    other_movies = movies[
        (movies["genre"] != movie_genre) &
        (movies["title"] != selected_movie)
    ]

    result = pd.concat([same_genre, other_movies])

    result = result.sort_values(
        by="rating",
        ascending=False
    ).head(num)

    st.subheader("🎯 Recommended Movies")

    cols = st.columns(5)

    for i, (_, row) in enumerate(result.iterrows()):

        with cols[i % 5]:
            st.image(row["poster"], width=160)
            st.markdown(f"### {row['title']}")
            st.write(f"📅 {row['year']}")
            st.write(f"🎭 {row['genre']}")
            st.write(f"⭐ {row['rating']}")
            st.write(f"📝 {row['info']}")
st.subheader("🏆 Top Rated Movies")

top_movies = movies.sort_values(
    by="rating",
    ascending=False
).head(5)

cols = st.columns(5)

for i, (_, row) in enumerate(top_movies.iterrows()):

    with cols[i % 5]:

        st.image(row["poster"], width=160)

        st.markdown(f"### {row['title']}")

        st.write(f"📅 {row['year']}")

        st.write(f"🎭 {row['genre']}")

        st.write(f"⭐ {row['rating']}")

        st.write(f"📝 {row['info']}")
# ---------------- ABOUT ----------------
else:

    st.markdown('<div class="main-box">', unsafe_allow_html=True)

    st.title("About Project")

    st.write("""
    This Movie Recommendation System recommends
    Hollywood, Bollywood, and Kannada movies
    based on movie genre and ratings.

    Features:
    ✔ Search Movie  
    ✔ Genre Filter  
    ✔ Movie Posters  
    ✔ Top Rated Movies  
    ✔ 35+ Movies Included  
    ✔ Kannada + Hindi + English Movies  
    """)

    st.markdown("</div>", unsafe_allow_html=True)