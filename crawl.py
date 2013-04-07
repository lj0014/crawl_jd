# -*- coding: utf-8 -*-

#查找最多人评价的洗衣机
#http://list.jd.com/737-794-880-0-0-0-0-0-0-0-1-1-1-19-1607-33.html
#http://list.jd.com/737-794-880-0-0-0-0-0-0-0-1-1-2-19-1607-33.html
#http://list.jd.com/737-794-880-0-0-0-0-0-0-0-1-1-%d-19-1607-33.html


import urllib2
import re

START_PAGE = 1
MAX_PAGE = 6
URL_FORMAT = 'http://list.jd.com/737-794-880-0-0-0-0-0-0-0-1-1-%d-19-1607-33.html'
RE_FORMAT = re.compile(r'<a.*?href="(.*?)">已有(\d+?)人评价</a>')

def main():
    result = []
    for i in range(START_PAGE,MAX_PAGE+1):
        url = URL_FORMAT % i
        try:
            response = urllib2.urlopen(url,timeout=10)
        except Exception,e:
            print 'download error: '+str(e)
        response = response.read()
        result += RE_FORMAT.findall(response)
    sorted_result = sorted(result,key=lambda x:x[1],reverse=True) 
    print sorted_result[:10]
        
if __name__ == '__main__':
    main()
