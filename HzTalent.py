# -*- encoding: utf-8 -*-
'''
@File    :   HzTalent.py    
@Contact :   shentuhaisan@gmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/12/28 下午6:11   shentu      1.0         None
'''
import codecs
import json
import re
import requests


def fetch(url):
    try:
        params = {}
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Cookie': 'hzrc_online_session=WDAY%2F9S94eeszgzgEvP8kAndQ3J%2BGljT7c4ThFcsB2cMjcaqyROjAf7pS07nIw%2F%2F6uuFxAkNo30eH%2BFXrW%2BPVLDbsbUKbqQtLvYxdUur0h4iXVp6OV64VpChyA6pKYE12T52m8sVtY7btiGNCCUMf15H1vHOxGc7Ku9nrA6eS8mopOTflAU6Pn4CxLB%2BSgASv7JwVxZ5bCHvF0LrS8DdUlH7b2S1e8q4kYQ6i8hF6AG9DOCKDgjJx26A0T7m5qP6BeUfIfae3VKOebSwrWQHtSYX9xkMaw0RCM5w7guXH24BfwEYrIcQllcHxIpVPDw8J6TF3Fpjg2LG2Rdtt29w2z30%2FuLLGqCSJIYUFKmI2vQlhzr8DahmpgG3PP3Gejiu%2FrcOxyoz73TIQD4s5ifsnmVCLb0LLv1pkW4pOc%2BDDqQQQkGyOh8AGr3bMAlZUoTXBq1NkXRFe7siVtGROhyy9A%3D%3Debe8e02c9b24504e7d7b662a1a9d8b32672350c6; BIGipServerrc_10.10.20.47=789842442.20480.0000',
            'Host': 'rc.zjhz.hrss.gov.cn',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://rc.zjhz.hrss.gov.cn/articles/2/page/1.html',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            }
        response = requests.get(url, params=None, headers=headers)
        if response.status_code in [200, 201]:
            return response.text
        return None
    except Exception as e:
        print("fetch url:{},error:{}", url, e)
        # raise e
        return None


def parse(html):
    pattern = re.compile('<li>.*?href="(.*?)".*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        #print('解析后内容：{}'.format(item))
        detail = fetch(item)
        detailPattern = re.compile('<div class="articles-detail-box gray-box">.*?<h3>(.*?)</h3>.*?</div>', re.S)
        detailItems = re.findall(detailPattern, detail)
        for dd in detailItems:
            # print(dd)
            # title = str(dd).index('高层次人才的公示')
            if dd.find('高层次人才的公示') > -1:
                rcPattern = re.compile(
                    '<p class="MsoNormal".*?<span>(.*?)</span>(.*?)<span>(.*?)</span>(.*?)<span>(.*?)</span>.*?<span>(.*?)</span>.*?.*?</p>',
                    re.S)
                rcInfo = re.findall(rcPattern, detail)
                if len(rcInfo) > 0:
                    print(rcInfo)
                    for rc in rcInfo:
                        info = {
                            'name(姓名)': rc[0],
                            'workUnit(单位)': rc[1],
                            'company(公司)': rc[2],
                            'birthday(年月日)': rc[3],
                            'level(级别)': rc[4],
                            'other(其他)': rc[5]
                        }
                        write_to_file(info)


def write_to_file(content):
    with open('HzTalent.txt', 'a', encoding='utf-8') as f:
        data = json.dumps(content, ensure_ascii=False)
        f.write(data + '\n')
    f.close()


if __name__ == '__main__':
    # 默认25一页
    for i in range(1,100):
        url = 'http://rc.zjhz.hrss.gov.cn/articles/2/page/' + str(i) + '.html'
        html = fetch(url)
        parse(html)
    #write_to_file(rcList)
    # movies = parse(html)
    # for item in movies:
    #     print(item)
    #     # insert_to_mysql(item)
    #     write_to_file(item)
