import json
import re

import requests
import time
import Movie

"""
请求url
返回内容
"""
def fetch(url):
    try:
        response = requests.get(url)
        if response.status_code in [200,201]:
            return response.text
        return None
    except Exception as e:
        print("fetch url:{},error:{}",url,e)
        #raise e
        return None

def parse(html):
    pattern = re.compile('<li>.*?<em.*?>(\d+)</em>.*?src="(.*?)".*?title">(.*?)</span>.*?v:average">(.*?)</span>.*?inq">(.*?)</span>.*?</li>',re.S)
    items = re.findall(pattern, html)
    print("解析后的内容：{}".format(items))
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title(片名)': item[2],
            'score(评分)': item[3],
            'inq(影评)': item[4]
        }

def write_to_file(content):
    with open('doubanmovie.txt', 'a', encoding='utf-8') as f:
        moviedata = json.dumps(content,ensure_ascii=False)
        f.write(moviedata + '\n')
    f.close()

def insert_to_mysql(dict_item):
    movie = Movie.Movie(json.dumps(dict_item,ensure_ascii=False),"douban", 1, dict_item.get("title(片名)"), 0, dict_item.get("inq(影评)"), dict_item.get("image"), float(dict_item.get("score(评分)")))
    print(movie)
    Movie.add_one_movie(movie)

def insert_to_mysql(dict_items):
    movie_list = []
    for dict_item in dict_items:
        movie = Movie.Movie(json.dumps(dict_item, ensure_ascii=False), "douban", 1, dict_item.get("title(片名)"), 0,
                            dict_item.get("inq(影评)"), dict_item.get("image"), float(dict_item.get("score(评分)")))
        movie_list.append(movie)
    Movie.batch_add_movie(movie_list)

def main(start_num):
    # 默认25一页
    url = 'https://movie.douban.com/top250?start='+str(start_num)+'&filter='
    html = fetch(url)
    movies = parse(html)
    insert_to_mysql(movies)
    for item in movies:
        print(item)
        #insert_to_mysql(item)
        write_to_file(item)

if __name__ == '__main__':
     start_time = time.time()
     for i in range(10):
        main(i*25)
     print("耗时{}".format(time.time()-start_time))