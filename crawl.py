# -*- coding: utf-8 -*-

#查找最多人评价的洗衣机
#http://list.jd.com/737-794-880-0-0-0-0-0-0-0-1-1-1-19-1607-33.html
#http://list.jd.com/737-794-880-0-0-0-0-0-0-0-1-1-2-19-1607-33.html
#http://list.jd.com/737-794-880-0-0-0-0-0-0-0-1-1-%d-19-1607-33.html

import time
import urllib2
import re
import sys

START_PAGE = 1
MAX_PAGE = 6
URL_FORMAT = 'http://list.jd.com/737-794-880-0-0-0-0-0-0-0-1-1-%d-19-1607-33.html'
RE_FORMAT = re.compile('<span class=\'evaluate\'><a.*?href=\'(.*?)\'>已有(\d+?)人评价</a></span>')

def read_input():
    usage_str = 'Usage: python %s <list_url_format> <list_max_page>'
    usage_str = usage_str % sys.argv[0]
    if len(sys.argv) != 3:
        print '!!!command error!!!'
        print usage_str
        sys.exit(-1)
    else:
        global URL_FORMAT,MAX_PAGE
        URL_FORMAT = sys.argv[1]
        MAX_PAGE = int(sys.argv[2])

def main():
    read_input()
    result = []
    for i in range(START_PAGE,MAX_PAGE+1):
        url = URL_FORMAT % i
        try:
            request = urllib2.Request(url)
            opener = urllib2.build_opener()
            request.add_header('User-Agent','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31')
            response = opener.open(request)
        except Exception,e:
            print 'download error: '+str(e)
        response = response.read()
        response = unicode(response,'gbk').encode('utf-8')
        result += RE_FORMAT.findall(response,re.S)
        time.sleep(1)
    sorted_result = sorted(result,key=lambda x:int(x[1]),reverse=True) 
    print sorted_result[:10]
        
if __name__ == '__main__':
    main()
