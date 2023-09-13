Content Based Recommender System recommends movies similar to the movie user likes and analyses the sentiments on the reviews given by the user for that movie.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API.

Source Code: https://github.com/qodire/DyQoRec-Movie_Recommender

## How to get the API key?
Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved.

## How to run the project?
1. Clone or download this repository to your local machine.
2. Open the artificats.txt file, then download the file contained in the link. Create a new folder named artificats, then put the downloaded file into the artificats folder.
3. Install all the libraries mentioned in the [requirements.txt](https://github.com/qodire/DyQoRec-Movie_Recommender/blob/main/requirements.txt) file with the command `pip install -r requirements.txt`
4. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
5. Open your terminal/command prompt from your project directory and run the file `app.py` by executing the command `streamlit run app.py`.
6. Go to your browser and type `http://127.0.0.1:5000/` in the address bar.
7. Well, that's it. Please Enjoy!

## Similarity Score : 
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
   
## How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)

More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

### Sources of the datasets 
1. [TMDB 5000 Movie Dataset] (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)