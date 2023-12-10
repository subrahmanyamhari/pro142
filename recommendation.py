from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import csv

df1=pd.read_csv('articles.csv')
df2=pd.read_csv('users_interactions.csv')

count = CountVectorizer(stop_words="english")
data = count.fit_transform(df1["title"])

similarity = cosine_similarity(data,data)

df1 = df1.reset_index()

indexing = pd.Series(df1.index,index=df1["contentId"])

def recommended(similarity,contentId):
#   count1 = CountVectorizer(stop_words="english")
#   count1.fit_transform(contentId)
  id = indexing[contentId]
  print(id)
  similarity_percentage = list(enumerate(similarity[id]))
  sorted_similarity = sorted(similarity_percentage, key=lambda x:x[1] , reverse = True)
  sorted_similarity = sorted_similarity[1:5]
  print(sorted_similarity)
  articles = [i[0] for i in sorted_similarity]
  return  df1[['title','url','text','lang','total_events','contentId']].iloc[articles]

v = recommended(similarity,-4029704725707465084)
print(v)

df1.to_csv("article.csv")