# Project: Movie Recommender System Using Machine Learning!

<img src="demo/6.jpeg" alt="workflow" width="70%">

Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.

#### Types of Recoomendation system
1. Content based
2. Collabrative Filtering Based
3. Hybrid based

#### Content Based - 
Recommend based on similiarty of content. Example Iron Man and Iron Man 2 are similar.
#### Collabrative Filtering Based - 
lets say customer 1 and customer 2 have similar kind of interest becuase for most of the movies they 
have given simmilar ratings. 
So for any movie/ movie criteria on which customer 1 has given good rating then its high chance that customer 2 also will give good rating for the same movie.
#### Hybrid Based - 
Both content and collabrative filtering used in hybrid based recommendation 
 


# About this project:

This is a web application that recommends similar kinds movies to user based on its search input. It is using streamlit to provide UI and precalculated distnaces between vectors for recommendations. To calculate distance between two vectors we have used cosine similarity.  
Note - Number of similar movies to be displayed is configurable due to parameters of "configs/config.yaml" file.

Also, have a look at deployed project,

* [Click here to run it live on server](https://share.streamlit.io/atulgaikwad12/movie-recommender-system-ml-contentbased/main/app.py)


# Demo:

<img src="demo/1.png" alt="workflow" width="70%">

<img src="demo/2.png" alt="workflow" width="70%">

<img src="demo/3.png" alt="workflow" width="70%">


# Dataset has been used:

* [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)



# How to run?
### STEPS:

#### Clone the repository in local directory

```bash
git clone https://github.com/atulgaikwad12/Movie-Recommender-System-ML-ContentBased.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n envmovie python=3.7.10 -y
```

```bash
conda activate envmovie
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


#### Open jupyter notebook run with current env
```bash
jupyter-notebook
```

#### Can Download data set from below location and unzip in data folder 
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/download

#### Run below jupyter notebook to do data preprocessing, generate artifacts of distances, movies that can be used further to get end result.
Note - Find generated pickel files in artifcats folder    
```bash
Movie Recommender System Data Analysis.ipynb
```

#### To run application use below command
```bash
streamlit run app.py
```

#### Create repository on github and execute below commands to push code 
```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add <origin your_new_github_repo_url>
git push -u origin main
```

#### To push large files use below commands 
##### Download and install the Git lfs command line extension.
```bash
git lfs install
```
##### select the file types you'd like Git LFS to manage
```bash
git lfs track "*.pkl"
git lfs track "*.png"
git lfs track "*.jpeg"
```
##### To make sure .gitattributes is tracked
```bash
git add .gitattributes
```
##### Add large files or simply all in staging area
```bash
git add .
```
##### Finally commit and push (may have to solve some conflict on push) 
```bash
git commit -m "Add design file"
git push origin main  
```
#### To deploy application on streamlit share 
##### 1. Signup in streamlit share using github account OAuth and Create New app
##### 2. Select Github repository and branch
##### 3. Add scerate tmdb_key in TOML format
```bash
tmdb_key = "API_KEY_STRING"
```
##### 4. Deploy app



