# MOVIE-RECOMMENDER-SYSTEM
A movie recommender system is used to recommend movies to users based on various factors. There are primarily two types of recommender systems, content based systems and collaborative systems. 
* Collaborative filters : This type of filter is based on users’ rates, and it will recommend us movies that we haven’t watched yet, but users similar to us have, and like. To determine whether two users are similar or not, this filter considers the movies both of them watched and how they rated them. By looking at the items in common, this type of algorithm will basically predict the rate of a movie for a user who hasn’t watched it yet, based on the similar users’ rates.

* Content-based filters : This type of filter does not involve other users if not ourselves. Based on what we like, the algorithm will simply pick items with similar content to recommend us.
## Dataset
These files contain metadata for all 45,000 movies listed in the Full MovieLens Dataset.Data points include cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote counts and vote averages and ratings.

**movies_metadata.csv**: Features include title, posters, backdrops, budget, revenue, release dates, languages, production countries and companies.

**keywords.csv**: Contains the movie plot keywords for our MovieLens movies. Available in the form of a stringified JSON Object.

**credits.csv**: Consists of Cast and Crew Information for all our movies. Available in the form of a stringified JSON Object.

The goal for this NLP project was to divide the content based recommendations of a movie into separate clusters(using Kmeans clustering) and then use text analysis to determine various attributes of movies each cluster recommends. The recommender system takes movie title as an input and returns three different bags of movies. Initial sorting and subsequent clustering is done based on similarity scores (genre, cast, overview, keywords, director) and ratings of the movies. Visualization was done using wordclouds and plotly charts. Following are the recommendations for "The Chronicles of Narnia: Prince Caspian".
## Approach
A general approach towards a content basd sytem is that it computes similarity between movies based on certain metrics and suggests movies that are most similar to a particular movie that a user liked. On the other hand collaborative methods for recommender systems are methods that are based solely on the past interactions recorded between users and items in order to produce new recommendations. We wanted to do something different and apply a machine learning approach to the system and so we decided to use clustering. he goal for this NLP project was to divide the content based recommendations of a movie into separate clusters(using Kmeans clustering) and then use text analysis to determine various attributes of movies each cluster recommends. The recommender system takes movie title as an input and returns three different bags of movies. So the process like any other ML project involved three steps :
1. Data Cleaning : The very first task was to clean the data so that it would make sense. This included managing null values, dealing with stringified JSON object data, sorting data jumbled across various columns, converting data types of columns for appropriate use.
1. Data Preprocessing : In order to perform further operations on our text, we need to transform our documents into vector representations such that we can apply numeric machine learning. For vectorization of text corpuses (or columns) "CountVectorizer" and "Tfidfvectorizer"have been used. The vectorized matrix was further used as an input for calculating similarity score between movies. The output for the same was in the form of matrix. 
1. Modelling : The matrix had movies for it's rows as well as columns, each cell representing a similarity score between the movies that belonged to the respective row and column.The similariy scores were calculated for:
The above mentioned matrix was used a an input for the clustering algorithm which divided the movies into three clusters. 

![](PLOTS/WC1.png) <br /><br /><br />
![](PLOTS/TABLE1.png)<br /><br /><br />
![](PLOTS/CLUSTER1.png)<br /><br /><br /><br />
![](PLOTS/WC2.png)<br /><br /><br />
![](PLOTS/TABLE2.png)<br /><br /><br />
![](PLOTS/CLUSTER2.png)<br /><br /><br /><br />
![](PLOTS/WC3.png)<br /><br /><br />
![](PLOTS/TABLE3.png)<br /><br /><br />
![](PLOTS/CLUSTER3.png)

