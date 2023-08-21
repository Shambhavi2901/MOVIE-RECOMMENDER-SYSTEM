#!/usr/bin/env python
# coding: utf-8

# ![](http://data:image/jpeg;base64,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)

# # **INTRODUCTION**
# 
# Recommender Systems are used to generate recommendations. The two main types of recommender systems are either collaborative or content-based filters.
# 
# * Collaborative filters : This type of filter is based on users’ rates, and it will recommend us movies that we haven’t watched yet, but users similar to us have, and like. To determine whether two users are similar or not, this filter considers the movies both of them watched and how they rated them. By looking at the items in common, this type of algorithm will basically predict the rate of a movie for a user who hasn’t watched it yet, based on the similar users’ rates.
# 
# * Content-based filters : This type of filter does not involve other users if not ourselves. Based on what we like, the algorithm will simply pick items with similar content to recommend us.
# 
# * Hybrid Engine : Ideas brought together from content and collaborative filtering to build an engine that gave movie suggestions to a particular user based on the estimated ratings that it had internally calculated for that user.

# # DATASET
# 
# ### Context
# 
# These files contain metadata for all 45,000 movies listed in the Full MovieLens Dataset. The dataset consists of movies released on or before July 2017. Data points include cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote counts and vote averages.
# 
# This dataset also has files containing 26 million ratings from 270,000 users for all 45,000 movies. Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.

# # IMPORT LIBRARIES

# In[1]:


import re
import nltk
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
from ast import literal_eval
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.font_manager import FontProperties
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import plotly
import plotly.io as pio
from os import path
from PIL import Image
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

get_ipython().run_line_magic('matplotlib', 'inline')
warnings.simplefilter('ignore')
pd.set_option('display.max_columns', 50)


# # IMPORT DATASET
# 
# We're going to use only three files from the database, namely
# 
# * movies_metadata,
# * credits,
# * keywords.

# In[2]:


#Loading the datasets
#metadata of the movies
md = pd.read_csv('/kaggle/input/the-movies-dataset/movies_metadata.csv')
#movie credits
credits = pd.read_csv('/kaggle/input/the-movies-dataset/credits.csv') 
#movie keywords
keywords = pd.read_csv('/kaggle/input/the-movies-dataset/keywords.csv') 


# # DATA PREPARATION

# ### credits.csv

# In[3]:


credits.head()


# ***credits*** contains the cast, crew and id corresponding to various movies. As we can see, the cast and crew columns contains a list of dictionaries but it is in the form of strings somewhat resembling a JSON format. Hence we'll use literal_eval to convert in from string to list of dictionaries and then extract the Cast and Director from the Crew columns.

# In[4]:


#Converting the string into list of dictionaries
credits.cast = credits.cast.apply(literal_eval)
credits.crew = credits.crew.apply(literal_eval)


# In[5]:


# Extracting the Casts into a list from Dictionaries
credits['cast'] = credits['cast'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])


# In[6]:


# Extracting the Director from the Crew
def extract_director(x):
    for crew_mem in x:
        if crew_mem['job'] == 'Director':
            return crew_mem['name']
        else:
            return np.nan

credits['director'] = credits['crew'].apply(extract_director)
credits['director'].fillna('',inplace = True)


# In[7]:


credits.drop(['crew'],axis = 1,inplace = True)
credits.head()


# ### keywords.csv

# In[8]:


keywords.head()


# ***keywords*** contains the keywords and id corresponding to various movies. As we can see, the keywords columns contains a list of dictionaries but it is in the form of strings,similar to ***credits***. We'll handle it in a similar way.

# In[9]:


#Converting the string into list of dictionaries
keywords.keywords = keywords.keywords.apply(literal_eval)


# In[10]:


# Extracting the Keywords into a list from Dictionaries
keywords['keywords'] = keywords['keywords'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])


# In[11]:


keywords.head()


# ## movies_metadata.csv

# In[12]:


md.head()


# In[13]:


md.describe(include = 'all')


# In[14]:


md[(md.adult != "True") & (md.adult != "False")]


# The "adult" column has 5 values instead of 2 (True and False). So first let's handle this column itself.
# 
# For these three movies, the data seems to be all jumbled up amongst various columns. For example, adult column contains the overview and overview column contains the status etc. But actually the data is divided across two indices. So we combine the data into single index and drop the later index.

# In[15]:


idx = [19729,29502,35586]
lst_1 = ['popularity', 'poster_path', 'production_companies','production_countries', 'release_date', 'revenue',
         'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count']
lst_2 = ['belongs_to_collection', 'budget', 'genres', 'homepage', 'id', 'imdb_id', 'original_language', 'original_title', 
         'overview','popularity', 'poster_path', 'production_companies','production_countries', 'release_date']
for i in idx:
    for col_seq in range(len(lst_1)):
            md[lst_1[col_seq]][i] = md[lst_2[col_seq]][i+1]


# In[16]:


idx = [x+1 for x in idx]
md.drop(index = idx,inplace = True)


# In[17]:


md.adult = md.adult.apply(lambda x : True if (x == 'True') else False)


# genres are also in JSON format, so we'll handle it in the similar way we have handled it so far.

# In[18]:


# Extracting the Genres into a list from Dictionaris
md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])


# In[19]:


# Dropping Duplicates 
credits.drop_duplicates('id',inplace = True)
keywords.drop_duplicates('id',inplace = True)
md.drop_duplicates('id',inplace = True)


# In[20]:


#Converting IDs into same data type
md.id = md.id.astype(int)


# In[21]:


#Merging DataFrames into one
md = md.merge(credits, on = 'id', how = 'left')
md = md.merge(keywords, on = 'id', how = 'left')
md.head()


# # SELECTING REQUIRED DATA

# In[22]:


# Selecting required columns from the master dataframe
movies = md[['id','original_title','title','cast', 'director', 'keywords', 'genres', 'release_date', 'overview', 
             'original_language', 'adult', 'runtime', 'tagline', 'vote_average', 'vote_count','popularity']]
movies.head(30)


# In[23]:


# Missing Value
movies.isna().sum()


# ### SUBSTITUTING NULL VALUES  

# In[24]:


movies.original_language.fillna('',inplace = True)
# Fill NA of Tagline with empty strings
movies.tagline.fillna('',inplace = True)
# Fill NA of overview with empty strings
movies.overview.fillna('',inplace = True)
movies.loc[movies.overview == 'No overview found.','overview'] = ''
# Fill NA of runtime with 0
movies.runtime.fillna(0,inplace = True)

movies.cast = movies.cast.apply(lambda x: x if isinstance(x, list) else [])
movies.director.fillna('',inplace = True)
movies.keywords = movies.keywords.apply(lambda x: x if isinstance(x, list) else [])

# If the release_Date is missing, as of now we're putting the date of 2050-01-01 in order to be able to convert in into datetime object
movies.loc[movies['release_date'].isna(),'release_date'] = '2050-01-01'
movies.release_date = pd.to_datetime(movies.release_date,format = '%Y-%m-%d')


# In[25]:


movies.head(5)


# # DATA PREPROCESSING

# ## !!! Takes a lot of time, so a csv file has been saved, use that !!!

# Due to the limited computing strength available only around 45%(20,000 rows) of the data has been used to work upon.

# In[26]:


movies["popularity"] = pd.to_numeric(movies["popularity"], downcast="float")
movies = movies.sort_values(by='popularity',axis=0, ascending=False)[0:20000].reset_index()
movies=movies.drop(['index'], axis=1)
movies.head(5)


# In[27]:


#combining the overview and taglines
movies['plot_corpus'] = movies['overview'] + movies['tagline']

def listtostr(txt):
    '''
    Returns string by joining the elements of the list
    '''
    
    txt_clean = ' '.join([str(elem) for elem in txt])
    return txt_clean

movies['keywords'] = movies['keywords'].apply(listtostr)
movies['genres'] = movies['genres'].apply(listtostr)

#movies['plot_corpus_1'] = movies['overview'] + movies['tagline'] + movies['keywords']
movies['genre_corpus'] = movies['keywords'] + movies['genres']


# ## Text cleaning
# Before vectorization a certain level of cleaning is required. This includes:
# * Removing punctuations
# * Converting the text documents to lower case
# * Removing the stopwords: Stopwords are the English words which do not add much meaning to a sentence. They can safely be ignored      without sacrificing the meaning of the sentence. For example, the words like the, he, have etc
# * Lemmatization : Lemmatization is the process of converting a word to its base form. 
# 
# **Note** : Another way of reducing words to their root form is stemming. But stemming just removes the last few characters, often leading to incorrect meanings and spelling errors whereas lemmatization considers the context and converts the word to its meaningful base form, we decided to use the latter. 

# In[28]:


def get_wordnet_pos(word):
    '''
    Returns the tag for the word
    '''
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

lemmatizer=WordNetLemmatizer()

def clean_plot(txt):
    '''
    Returns the cleaned plot text 
    '''
    
    regex = re.compile(r"[!@%&;?'',.""-]")
    txt_clean = re.sub(regex,'',txt)
    txt_clean = txt_clean.lower()
    txt_clean = txt_clean.split(' ')
    txt_clean = [word for word in txt_clean if word not in stopwords.words('english')]
    txt_clean = ' '.join(txt_clean)
    word_list = nltk.word_tokenize(txt_clean)
    txt_clean = ' '.join([lemmatizer.lemmatize(w,get_wordnet_pos(w)) for w in word_list])
    return txt_clean

def clean_cast(txt):
    '''
    Returns the cleaned cast string
    '''
    
    for i in range(len(txt)):
        txt[i] = re.sub(r"[.,']","",txt[i])
        txt[i] = re.sub(r"[-]"," ",txt[i])
        txt[i] = re.sub(" ","_",txt[i])
        txt[i] = txt[i].lower()
    return txt

def clean_director(txt):
    '''
    Returns the cleaned director string
    '''
    
    txt_clean = re.sub(r"[.,']","",txt)
    txt_clean = re.sub(r"[-]"," ",txt_clean)
    txt_clean = re.sub(" ","_",txt_clean)
    txt_clean = txt_clean.lower()
    return txt_clean


# In[29]:


movies['plot_corpus'] = movies['plot_corpus'].apply(clean_plot)
movies['genre_corpus'] = movies['genre_corpus'].apply(clean_plot)
movies['genre_pure'] = movies['genres'].apply(clean_plot)


# In[30]:


movies['genre_pure']


# In[31]:


movies['cast'] = movies['cast'].apply(clean_cast)
movies['cast'] = movies['cast'].apply(listtostr)
movies['director'] = movies['director'].apply(clean_director)


# In[32]:


movies['genre_corpus'] = movies['genre_corpus'] + movies['cast']
movies['mixed_corpus'] = movies['genre_corpus'] + movies['plot_corpus']


# ## Vectorization 
# In order to perform further operations on our text, we need to transform our documents into vector representations such that we can apply numeric machine learning. This process is called vectorization.For vectorization of text corpuses (or columns) "CountVectorizer" and "Tfidfvectorizer"have been used.
# 
# "CountVectorizer" counts the word frequencies. With the "TfidfVectorizer" the value increases proportionally to count, but is inversely proportional to frequency of the word in the corpus; that is the inverse document frequency (IDF) part. The IDF feature of the tfidf vectorizer helps in dealing with the redundancy that might be caused by common words in a corpus consisting of sentences such as our overview column."Tfidfvectorizer" has been used to vectorize the 'plot corpus' and countevectorizer to vectorize genre,cast and director columns.

# In[33]:


tf = TfidfVectorizer(analyzer = 'word', ngram_range = (1,2), min_df = 0, stop_words = 'english')
cv = CountVectorizer(analyzer = 'word', ngram_range = (1,2), min_df = 0, stop_words = 'english')

plot_vector = tf.fit_transform(movies['plot_corpus'])
genre_vector = cv.fit_transform(movies['genre_corpus'])
cast_vector = cv.fit_transform(movies['cast'])
director_vector = cv.fit_transform(movies['director'])
genre_only_vector = cv.fit_transform(movies['genre_pure'])


# ## SIMILARITY MEASURES
# There are various metrics to calculate the similarity score of the vectorized documents. Cosine similarity has been used here.
# Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. The smaller the angle, higher the cosine similarity. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. 
# 
# The cosine similarity function returns a returns a pairwise cosine similarity matrix for the vector input. When stored in a dataframe, each row represents the similarity score of a particular movies with respect to all the other movies.

# In[34]:


from sklearn.metrics.pairwise import cosine_similarity

plot_score = cosine_similarity(plot_vector,plot_vector)
genre_score = cosine_similarity(genre_vector,genre_vector)
cast_score = cosine_similarity(cast_vector,cast_vector)
director_score = cosine_similarity(director_vector, director_vector)
genre_only_score = cosine_similarity(genre_only_vector,genre_only_vector)

plot_score = pd.DataFrame(plot_score)
genre_score = pd.DataFrame(genre_score)
cast_score = pd.DataFrame(cast_score)
director_score = pd.DataFrame(director_score)
genre_only_score = pd.DataFrame(genre_only_score)


# Calculating average of the ratings alotted by various users would give biased results because of the discrepancy in the number of ratings each movie received. Instead we use the weighted rating formulae.
# 

# In[35]:


vote_counts = movies[movies['vote_count'].notnull()]['vote_count'].astype('int')
vote_averages = movies[movies['vote_average'].notnull()]['vote_average'].astype('int')
C = vote_averages.mean()
m = vote_counts.quantile(0.95)

print(C,m)

def weighted_rating(x):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)

movies['wr'] = movies.apply(weighted_rating, axis=1)


# There are a total of 151 movies with 0 votes,but no movie has a popularity of 0.
# So we can get a weighted average of votes of similar movies in the same genres and also weigth it on the popularity of the corresponding movie.

# In[36]:


movies['genres'] = movies['genres'].apply(lambda x : x.split())
movies['release_year'] = movies.release_date.apply(lambda x: x.year)


# In[37]:


def score(value,index_list,feature):
    '''
    Returns list of scores for the passed feature
    '''
    if feature == 'genre':
        df_temp = pd.DataFrame(genre_only_score[value])
    if feature == 'plot':
        df_temp = pd.DataFrame(plot_score[value])
    if feature == 'plot_1':
        df_temp = pd.DataFrame(plot_score_1[value])
    if feature == 'cast':
        df_temp = pd.DataFrame(cast_score[value])
    if feature == 'director':
        df_temp = pd.DataFrame(director_score[value])
    df_temp = df_temp.loc[df_temp.index.isin(index_list)]
    my_list = df_temp[value].tolist()
    return my_list

    


# ## MODEL KEY POINTS 
# * Arrange movies in the descending order by their genre similarity score with respect to the target film.
# * Cluster the movies received from the previous step based on their plot scores.
# * Further sort movies(in descending order) within each cluster on the basis of all the similarity scores(previously calculated) and their calculated weighted ratings.
# * Return the top fifty recommendations from each cluster

# In[38]:


def get_feature_set(df1,df2,df3,title):
    
    '''
    idx : index value of the target movie
    top : index value of top 500 movies(sorted(descending) by genre similarity score w.r.t. target movie)
    feature_set : Data frame containing plot score matrix of movies which had their index in "top"
    movie_set : Name of the movies which had their index in "top"
    '''   
    
    idx = movies.index[movies.title == title].values.astype(int)[0]
    top = df1[idx].sort_values(ascending = False)[0:500].index.values.tolist()
    top = df1[idx].sort_values(ascending = False)[0:500].index.values.tolist()
    feature_set = df2[df2.index.isin(top)]
    movies_set = pd.DataFrame(movies.loc[movies.index.isin(top),'title'])
    return feature_set,movies_set

def get_recommendations(title,cluster_num,df1=genre_score,df2=plot_score,df3=cast_score):
    
    '''
    movie_set = dataframe to store the cluster labels(1,2,3) assigned to movies along with their similarity scores and ratings
    df_recommend = dataframe with information about the top 50 movies recommended from each cluster
    '''
    
    feature_set,movies_set = get_feature_set(df1,df2,df3,title)
    cluster_algo = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=42)
    cluster = cluster_algo.fit(feature_set)
    movies_set['cluster'] = cluster.labels_
    index = movies_set.index.values.tolist()
    idx = movies.index[movies.title == title].values.astype(int)[0]
    movies_set.loc[movies_set.index.isin(index),'wr'] = movies.loc[movies.index.isin(index),'wr']
    movies_set.loc[movies_set.index.isin(index),'p_score'] = score(idx,index,'plot')
    movies_set.loc[movies_set.index.isin(index),'g_score'] =score(idx,index,'genre')
    movies_set.loc[movies_set.index.isin(index),'c_score'] = score(idx,index,'cast')
    movies_set.loc[movies_set.index.isin(index),'d_score'] = score(idx,index,'director')
    target_cluster = movies_set.loc[movies_set.title == title, 'cluster'].values[0]
    if(target_cluster!=0):
        movies_set.loc[movies_set.cluster==target_cluster,'cluster'] = 100
        movies_set.loc[movies_set.cluster==0,'cluster'] = target_cluster
        movies_set.loc[movies_set.cluster==100,'cluster'] = 0
    if(cluster_num==1):
        recommend_1 = movies_set[movies_set.cluster == 0] 
        df_recommend = pd.DataFrame(recommend_1.sort_values(['g_score','p_score','c_score','d_score', 'wr'],ascending=[False,False,False,False,False])[1:50].title)
    if(cluster_num==2):
        recommend_1 = movies_set[movies_set.cluster == 1] 
        df_recommend = pd.DataFrame(recommend_1.sort_values(['g_score','p_score','c_score','d_score', 'wr'],ascending=[False,False,False,False,False])[1:50].title)
    if(cluster_num==3):
        recommend_1 = movies_set[movies_set.cluster == 2] 
        df_recommend = pd.DataFrame(recommend_1.sort_values(['g_score','p_score','c_score','d_score', 'wr'],ascending=[False,False,False,False,False])[1:50].title)
    df_recommend.loc[df_recommend.index.isin(index),'genres'] = movies.loc[movies.index.isin(index),'genre_pure']
    df_recommend.loc[df_recommend.index.isin(index),'title'] = movies.loc[movies.index.isin(index),'title']
    df_recommend.loc[df_recommend.index.isin(index),'director'] = movies.loc[movies.index.isin(index),'director']
    df_recommend.loc[df_recommend.index.isin(index),'cast'] = movies.loc[movies.index.isin(index),'cast']
    df_recommend.loc[df_recommend.index.isin(index),'ratings'] = movies.loc[movies.index.isin(index),'wr']
    df_recommend.loc[df_recommend.index.isin(index),'adult'] = movies.loc[movies.index.isin(index),'adult']
    df_recommend['ratings'] = df_recommend['ratings'].round(decimals=2)
    return df_recommend


# ## VISUALIZATION
# After we have the recommendations we need to present it in a way that is easy to comprehend.
# * We are going to print top ten recommendations from each cluster.
# * Wordclouds to represent prominent genres, casts and directors in each cluster.
# > (Word clouds or tag clouds are graphical representations of word frequency that give greater prominence to words that appear more frequently in a source text. The larger the word in the visual the more common the word was in the document(s).We are going to make three wordclouds for each cluster.)
# * Pie chart to represent genre frequency in each cluster
# * A barchart to represent maximum, minimum and average ratings of each cluster
# 
# 

# In[39]:


def cluster_class(title,cl_num):
    '''
    converts each column of the recommendation dataframe into list
    '''
    df = get_recommendations(title,cluster_num=cl_num)
    cast = ' '.join(df.cast.tolist())
    genre = ' '.join(df.genres.tolist())
    director = ' '.join(df.director.tolist())
    ratings = df.ratings.tolist()
    return df,cast,director,genre,ratings,cl_num


# In[40]:


class recommended_cluster:
    '''
    movies   : A dataframe of movies with other information within a cluster
    cast     : A list of cast for the movies within a cluster
    director : A list of directors for the movies within a cluster
    genre    : A list of genres of the movies within a cluster
    ratings  : A list of ratings of the movies within a cluster
    
    '''
   
    def __init__(self,cluster_tuple):
        self.movies = cluster_tuple[0]
        self.cast = cluster_tuple[1]
        self.director = cluster_tuple[2]
        self.genre = cluster_tuple[3]
        self.ratings = cluster_tuple[4]
        self.cl_num = cluster_tuple[5]
        
    def recommended_movie(self):
        '''
        generates a table containing top 10 recommendations from each cluster along with their corresponding ratings
        '''
        df = self.movies[0:10]
        fig = go.Figure(data=[go.Table(header = dict(values = ['Title','Rating'],
                                                     font = dict(size=15),
                                                     align = "center"),
                                       cells = dict(values = [df.title,df.ratings],
                                                    align = "center")
                                      )
                             ]
                       )
        fig.show()    
    
    
    def cast_cloud(self):
        '''
        generates a wordcloud of casts present in a cluster
        '''
        wordcloud = WordCloud(random_state=1,
                              background_color='black', colormap='Blues_r',
                              collocations=False, stopwords = STOPWORDS).generate(self.cast)
        return wordcloud

    def director_cloud(self):
        '''
        generates a wordcloud of directors present in a cluster
        '''
        wordcloud = WordCloud(random_state=1,
                              background_color='black', colormap='Blues_r',
                              collocations=False, stopwords = STOPWORDS).generate(self.director)
        return wordcloud

        
    def genre_cloud(self):
        '''
        generates a wordcloud of genres present in a cluster
        '''
        wordcloud = WordCloud(random_state=1,
                              background_color='black', colormap='Blues_r',
                              collocations=False, stopwords = STOPWORDS).generate(self.genre)
        return wordcloud

    
    def get_wordcloud(self):
        '''
        plots the cast, genre and director wordclouds in the from of subplots 
        '''
        fig = plt.figure(figsize=(30,10))
        ax1 = fig.add_subplot(131)
        ax2 = fig.add_subplot(132)
        ax3 = fig.add_subplot(133)

        font = FontProperties()
        font.set_family('serif')
        font.set_name('Times New Roman')
        font.set_size(40)

        def nulltick(ax):
            '''
            removes the ticks from x and y axis of the wordcloud plots
            '''
            ax.xaxis.set_major_locator(ticker.NullLocator())
            ax.xaxis.set_minor_locator(ticker.NullLocator())
            ax.yaxis.set_major_locator(ticker.NullLocator())
            ax.yaxis.set_minor_locator(ticker.NullLocator())
        
        ax1.imshow(self.genre_cloud(), interpolation='bilinear')
        nulltick(ax1)
        ax1.set_xlabel("GENRE WORDCLOUD",fontproperties = font)
        ax2.imshow(self.cast_cloud(), interpolation='bilinear')
        nulltick(ax2)
        ax2.set_xlabel("CAST WORDCLOUD",fontproperties = font)
        ax3.imshow(self.director_cloud(), interpolation='bilinear')
        nulltick(ax3)
        ax3.set_xlabel("DIRECTOR WORDCLOUD",fontproperties = font)
        
        fig.suptitle('CLUSTER '+str(self.cl_num), fontsize=60)
        fig.tight_layout()
        plt.show()
    
    def pie_data(self):
        '''
        returns a dataframe with frequency of occurence of genres in a cluster
        '''
        wordlist = self.genre.split()
        wordfreq = [wordlist.count(p) for p in wordlist]
        dictionary = dict(list(zip(wordlist,wordfreq)))
        lst = list(dictionary.items())
        df = pd.DataFrame(lst)
        df.columns =['Genre','Frequency']
        return df

    def get_piechart(self):
        '''
        plots the frequency of occurence of genres in a cluster in the form of a piechart
        '''
        df = self.pie_data()
        values = df['Frequency']
        labels = df['Genre']
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.show()
        
        
    def get_ratings(self):
        '''
        calculates the minimum, maximum and average rating of a cluster
        '''
        minima = min(self.ratings)
        maxima = max(self.ratings)
        avg = sum(self.ratings)/len(self.ratings)
        return round(minima,2),round(maxima,2),round(avg,2)
    
    def ratings_chart(self):
        '''
        plots the minimum, maximum and average rating of a cluster in the form of a bar chart 
        '''
        minima,maxima,avg = self.get_ratings()
        fig = go.Figure(data=[
            go.Bar(name='Minimum Rating', x=['CLUSTER '+str(self.cl_num)], y=[minima], text=minima,textposition='outside',width = [0.2,0.2,0.2],marker_color = 'indianred'),
            go.Bar(name='Average Rating', x=['CLUSTER '+str(self.cl_num)], y=[avg],text=avg,textposition='outside', width = [0.2,0.2,0.2],marker_color = 'blue'),
            go.Bar(name='Maximum Rating', x=['CLUSTER '+str(self.cl_num)], y=[maxima],text=maxima,textposition='outside', width = [0.2,0.2,0.2], marker_color = 'green')
        ])
        fig.update_yaxes(range=[1, 10],dtick=1)
        fig.show()
   


# In[41]:


def Dashboard(title):
    for i in [1,2,3]:
        cluster = recommended_cluster(cluster_class(title,i))
        cluster.get_wordcloud()
        cluster.recommended_movie()
        cluster.get_piechart()
        cluster.ratings_chart()


# In[42]:


Dashboard("Spider-Man")


# In[ ]:




