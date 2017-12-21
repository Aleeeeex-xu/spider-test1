
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
reload(sys)
page = 1
url = 'http://www.qiushibaike.com/text/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    f = open(r'f:/result.txt','w')

    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<div class="stats".*?i class="number">(.*?)</i>(.*?)</span>.*?<span class="dash".*?i class="number">(.*?)</i>(.*?)</a>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[4]
            f.write(item[0].encode('utf-8'))
            f.write(item[1].encode('utf-8'))
            f.write(item[4].encode('utf-8'))
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason