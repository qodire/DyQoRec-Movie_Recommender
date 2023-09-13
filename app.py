from ctypes import alignment
import pickle
from tkinter import CENTER
from tkinter.ttk import Style
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="DyQoRec - Movie Recommendation", page_icon='img/logo.png', layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=9552e6b985181892f42f52899be8156c&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path

    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:7]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster

st.image("img/merk.png", width=300)
# st.title(":black[DyQoRec]")
st.markdown("<h2 style='text-align: center; color:  #293a46;'>Type or Select A Movie</h2>", unsafe_allow_html=True)

movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))
lottie_gif = load_lottieurl('https://lottie.host/131cbd19-d532-4afd-a887-9fe9c45aa884/BwBgs2v7y0.json')
movie_list = movies['title'].values
leftCol, rightCol = st.columns(2)
with leftCol:
    selected_movie = st.selectbox(
        'Type or Select A Movie to Get Recommendation',
        movie_list
    )
    show_bttn = st.button('Show Recommendation')
with rightCol:
    st_lottie(lottie_gif, height=300)



if show_bttn:
    st.subheader("Recommended Movies Based On " + selected_movie)
    st.write("")
    recommended_movies_name, recommended_movies_poster = recommend(
        selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5, gap='large')
    with col1:
        st.image(recommended_movies_poster[0])
        st.write(recommended_movies_name[0])

    with col2:
        st.image(recommended_movies_poster[1])
        st.write(recommended_movies_name[1])

    with col3:
        st.image(recommended_movies_poster[2])
        st.write(recommended_movies_name[2])

    with col4:
        st.image(recommended_movies_poster[3])
        st.write(recommended_movies_name[3])

    with col5:
        st.image(recommended_movies_poster[4])
        st.write(recommended_movies_name[4])

st.write("##")

st.markdown("***")
st.markdown("<h2 style='text-align: center; color: #293a46;'>Movie Recommendation System</h2>", unsafe_allow_html=True)
st.write("##")
st.write("**The Smart Way To Pick A Movie.**")
st.write("Watching movies is fun, but figuring out what movie to watch next is a nerve-racking experience. Endlessly scrolling through Netflix, watching trailers on YouTube, looking up IMDb ratings, wasting half an hour and still cannot decide what to watch – does this seem familiar to you?")
st.write("Then you have landed on the right page! DyQoRec movie recommendation system is the answer to the question “What movie should I watch?”! Your film choices are about to be simplified greatly.")
st.write("##")

st.write("**What Makes This Movie Recommendation Engine Unique?**")

benefir_list = ["All listed movies are hand-picked and manually tagged by film connoisseurs ensuring high quality recommendations.",
                "You can get more than one recommendations at a time, so there will be many movies you can choose.",
                "New movies are added consistently.",
                "Special recommendations for movie dates: these movies are perfect for dates & will help you to make a good impression on your crush."]
for i in benefir_list:
    st.markdown("◉ " + i)

hide_streamlit_style = """
            <style>
            header{
                margin: 0;
            }
            .css-z5fcl4{
                padding-top: 8vh;
            }
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:before{
                visibility: visible;
                content:'© Copyright 2023 - DyQoRec';
                display:block;
                padding-top: 0px;
            }
            .css-164nlkn{
                width: auto;
                font-size: 16px;
            }
            button[title="View fullscreen"]{visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)