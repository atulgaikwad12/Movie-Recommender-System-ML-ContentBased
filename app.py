'''
Author  : Atul Gaikwad
Purpose : To build streamlit web app
Date    : 2022-April-02
'''
import pickle
import streamlit as st
import requests
import os 
import math
import logging
from dotenv import load_dotenv
from src.utils.common import read_yaml,create_directories,get_unique_log_path

# Config parameters
config_path = "configs/config.yaml"
config = read_yaml(config_path)
LOG_DIR = config["LOG_DIR"]

# Env variables 
load_dotenv()
api_key = os.getenv("tmdb_key")

#Logger configuration 
create_directories([LOG_DIR])
LOG_FILENAME = get_unique_log_path(LOG_DIR)
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s] : %(message)s",
    filemode="a"
)


#Streamlit configuration & other config details mentioned in .streamlit/config.toml file 
st.set_page_config(
   page_title="Movie Recommender App",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

def fetch_poster(movie_id):
    '''
    Author          : atul.gaikwad
    Input  parma    : movie id 
    Description     : Returns movie poster image path from TheMovieDB API   
    '''

    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id,api_key)
        data = requests.get(url)

        full_path = config["webpage"]["default_img_path"] # defualt poster image  

        if(data is not None):
            data = data.json()
            poster_path = data['poster_path']
            
            if(poster_path is not None):
                full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            else: 
                 logging.info(f"for {movie_id} poster image path not found ")
            
            logging.info(f"for {movie_id} poster image path is {full_path}")
        else:
            logging.info(f"Did not received Data for {movie_id} ")
        
        return full_path

    except Exception as e:
        logging.warning(f"Failed to fetch poster image for movie id {movie_id}")
        logging.error(e)
        raise e


def recommend(movie):
    '''
    Author          : atul.gaikwad
    Input  parma    : movie dataframe 
    Description     : Returns tuple of 2 lists (movie name list, movie poster image path)  
    '''
    try:
        similarity = pickle.load(open('artifacts/similarity.pkl','rb'))

        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []

        display_recommendations = config["webpage"]["display_recomendation"]

        if(display_recommendations is None or display_recommendations > 20 ):
            logging.warning("Using default recommendation counts which is 5")
            display_recommendations = 5 # default 

        for i in distances[1:display_recommendations+1]:
            # fetch the movie poster img path
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        
        logging.info(f"Got {display_recommendations} recommendations for movie {movie_id}")
        return recommended_movie_names,recommended_movie_posters

    except Exception as e:
        logging.warning(f"Failed to return recommendations for movie id {movie_id}")
        logging.error(e)
        raise e

try:
    logging.info(f"Starting application...")

    #st.title('Movie Recommender')
    st.header('Content Based Movie Recommendation System')
    movies = pickle.load(open('artifacts/movie_list.pkl','rb'))

    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Start Typing... To choose you favorite Movie ",
        movie_list
    )

    if st.button('Show Recommendation'):
        
        logging.info(f"Finding recommendations for {selected_movie}...")
        recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
       
        # col1, col2, col3, col4, col5 = st.columns(5)
        # with col1:
        #     st.text(recommended_movie_names[0])
        #     st.image(recommended_movie_posters[0])
        # with col2:
        #     st.text(recommended_movie_names[1])
        #     st.image(recommended_movie_posters[1])

        # with col3:
        #     st.text(recommended_movie_names[2])
        #     st.image(recommended_movie_posters[2])
        # with col4:
        #     st.text(recommended_movie_names[3])
        #     st.image(recommended_movie_posters[3])
        # with col5:
        #     st.text(recommended_movie_names[4])
        #     st.image(recommended_movie_posters[4])
        
        movie_per_row = 4 # default

        if(config["webpage"]["movie_per_row"] is not None):
            logging.info(f"showing movie per row row : {movie_per_row}")
            movie_per_row = config["webpage"]["movie_per_row"]

        count = len(recommended_movie_names)
        
        rows = int(math.ceil(count / movie_per_row))
        index = 0
        for r in range(rows):

            if(count < movie_per_row):
                col_count = count
            else:
                col_count = movie_per_row
                count = count - movie_per_row

            cols = st.columns(col_count)

            logging.info(f"diaplaying row : {r+1}")

            for i,col in enumerate(cols):
                col.text(recommended_movie_names[index])
                col.image(recommended_movie_posters[index])
                index += 1

except Exception as e:
    logging.warning(f"Failed to display recommendations !!")
    logging.error(e)

