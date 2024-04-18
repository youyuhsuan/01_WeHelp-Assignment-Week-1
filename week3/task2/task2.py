import urllib.request as req
import bs4
import csv

def write_to_csv(articletitle, like, dislike, publishtime):
    file.write("{},{},{},{}\n".format(articletitle, like,dislike, publishtime))


def parse_page(page_url):
    request = req.Request(page_url, headers={
        'cookie':'over18=1',
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(data,"html.parser")
        titles = root.find_all("div",class_="title")
    

    for title in titles:
        if title.a != None:
            articletitle = title.a.string
            # print(title.a.string)
            article_url = "https://www.ptt.cc" + title.a["href"]
            like, dislike, publishtime = parse_article(article_url)
            write_to_csv(articletitle, like, dislike, publishtime)
            
    nextLink = root.find("a",string="‹ 上頁")
    return nextLink["href"]


def parse_article(article_url):
    request = req.Request(article_url, headers={
        'cookie':'over18=1',
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        article_root = bs4.BeautifulSoup(data, "html.parser")
        
        like_tags = article_root.find_all("span", string="推 ")
        like=len(like_tags)
        
        dislike_tag = article_root.find_all("span", string="→ ")
        dislike=len(dislike_tag)
        
        article_meta_value = article_root.find_all("span", class_="article-meta-value")
        
        if article_meta_value:
            article_meta_value = article_meta_value[-1]
            publishtime = article_meta_value.string
            # print(publishtime.string)
        else:
            publishtime = ""
        
    return like, dislike, publishtime
    
page_url = 'https://www.ptt.cc/bbs/Lottery/index.html'
# parse_page(page_url)

with open('week3/task2/article.csv', mode="w",encoding="utf-8") as file:
    for pre_page in range(3):
        page_url = 'https://www.ptt.cc' + parse_page(page_url) 
        
