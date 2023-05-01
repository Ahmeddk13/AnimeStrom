import requests as rq
from bs4 import BeautifulSoup as sp

# get the html of home page
def GetList_Anime(url="https://witanime.com/",classer="content page-content-container",posi_list=0): 
    page = rq.get(url)
    the_last_js_data = []
    soup = sp(page.text, 'html.parser')
    data = soup.find_all("div", classer)
    
    info_sp = sp(str(data[posi_list]),'html.parser')
    info = info_sp.find_all('img',{'class':'img-responsive'})
    statu = info_sp.find_all('div','anime-card-status')
    type = info_sp.find_all('div','anime-card-type')
    overlay_url = info_sp.find_all('a','overlay')
    
    # sync data to json
    for i in range(len(info)):
        the_last_js_data.append({
        'title':info[i]['alt'],
        'img':info[i]['src'],
        'statu':statu[i].text,
        'type':type[i].text,
        'overlay_url':overlay_url[i]['href']
        })
    #finsh program  and will all data saved
    return the_last_js_data