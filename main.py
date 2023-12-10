from flask import Flask, render_template, jsonify,request
import pandas as pd
from content import popular_articles
from recommendation import recommended, similarity
app = Flask(__name__)

liked = []
unliked = []
popular = []
recommendations = []

articles = pd.read_csv("C:/Users/subra/PycharmProjects/pythonProject/app/project141/articles.csv")
articles_details = articles[['title','url','text','lang','total_events','contentId']]
# popular_articles = articles_details.sort_values(["total_events"], ascending = False)
# popular_articles = popular_articles.head(20)
# print(popular_articles)
# # @app.route("/")

def default():
    global articles_details
    data = {"title":articles_details.iloc[0,0],"url":articles_details.iloc[0,1],"text":articles_details.iloc[0,2],"lang":articles_details.iloc[0,3],"total_events":str(articles_details.iloc[0,4]),"contentId":str(articles_details.iloc[0,5])}
    return data
def pops():
    global popular_articles

#     return data

@app.route("/get-article")
def get_articles():
    global articles, articles_details
    dt = default()
    print(dt)
    return jsonify({"article":dt,"success":"success"})

@app.route("/liked-article")
def liked_articles():
    global articles_details
    dtl = default()
    liked.append(dtl)
    articles_details.drop([0],inplace=True)
    articles_details = articles_details.reset_index(drop = True)
    return jsonify({"success":"success"})

@app.route("/unliked-article")
def unliked_articles():
    global articles_details
    dtul = default()
    unliked.append(dtul)
    articles_details.drop([0],inplace=True)
    articles_details = articles_details.reset_index(drop = True)
    return jsonify({"success":"success"})

@app.route("/liked")
def diplay_like():
    global liked
    return jsonify({"data":liked})

@app.route("/unliked")
def diplay_unlike():
    global unliked
    return jsonify({"data":unliked})

@app.route("/popular-articles")
def popular_ars():
    global articles, articles_details,popular_articles
    p_article = []
    for i,value in popular_articles.iterrows():
#         print(i,value)
        data = {"title":value["title"],"url":value["url"],"text":value["text"],"lang":value["lang"],"total_events":str(value["total_events"])}
        p_article.append(data)
    print(p_article)
    return jsonify({"article":p_article,"success":"success"})

@app.route("/recommended-articles")
def recommend():
    global liked
    r_article = []
    for i in liked:
        data = recommended(similarity,int(i["contentId"]))
        recommendations.append(data)
    print(recommendations)
    for i,value in recommendations.iterrows():
#         print(i,value)
        data = {"title":value["title"],"url":value["url"],"text":value["text"],"lang":value["lang"],"total_events":str(value["total_events"])}
        r_article.append(data)
    return jsonify({"article":r_article,"success":"success"})
app.run()