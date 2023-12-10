from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import csv

articles = pd.read_csv("C:/Users/subra/PycharmProjects/pythonProject/app/project141/articles.csv")
articles_details = articles[['title','url','text','lang','total_events']]
popular_articles = articles_details.sort_values(["total_events"], ascending = False)
popular_articles = articles_details.head(20)

