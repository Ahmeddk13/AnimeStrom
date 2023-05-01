from flask import Flask , request
from WAnime import *
app = Flask(__name__)

Domain ="https://witanime.com/anime-type/"
Classer = "anime-list-content"

#Home list page 

@app.route('/list')
def Home():
    posi_list = request.args.get('list')
    return GetList_Anime(posi_list=posi_list)

#MOVIES LIST PAGE

@app.route('/Movie/')
def Movie():
    return GetList_Anime(Domain+'movie/',Classer)

#ANIME LIST PAGE

@app.route('/Anime/')
def Anime():
    return GetList_Anime(Domain+'anime/',Classer)

app.run(host='0.0.0.0', port=81)
