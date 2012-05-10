import ConfigParser
import os
import urllib, urllib2
import time
from cookielib import CookieJar

def main():
    BANKIT_DIR = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(BANKIT_DIR, os.pardir, 'conf', 'bankit.ini')
    #print(config_file)
    config = ConfigParser.SafeConfigParser()
    config.read(config_file)
    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    url = config.get('global','url')
    # form field that gives offset to GMT in minutes
    localtime = time.localtime()
    hdTimeZoneOffset = (time.gmtime().tm_hour - localtime.tm_hour) * 60
    hdDateTime = '%s/%s/%s %s:%s:%s' % (localtime.tm_mon, localtime.tm_mday,
                                        localtime.tm_year, localtime.tm_hour,
                                        localtime.tm_min, localtime.tm_sec)

    data = {'ctlUserName':config.get('global','user'),
                  'txtPassword':config.get('global','pwd'),
                  'hdTimeZoneOffset':hdTimeZoneOffset, 'hdDateTime':hdDateTime}
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
     'Accept-Encoding':'gzip,deflate,sdch',
     'Accept-Language':'en-US,en;q=0.8',
     'Cache-Control':'max-age=0',
     'Connection':'keep-alive',
     'Content-Type':'application/x-www-form-urlencoded',
     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11'}
    request = urllib2.Request(url, data=urllib.urlencode(data), headers=headers)
    #print 'Request method before data:', request.get_method()
    #print 'Request method after data:', request.get_method()

    #print 'Outgoing request:'
    #print request.get_full_url()
    try:
        #response1 = opener.open('https://www.ufcu.org')
        #print response1.read()
        #import pdb; pdb.set_trace()

        f = opener.open(request)
	response = f.read()
    except Exception as e:
        print 'exception', e.args
    response2 = urllib2.Request("https://ondemand.ufcu.org/HBNET/accountinfo/AccountHistory.aspx", data=urllib.urlencode(data), headers=headers)
    f = opener.open(request)
    response = f.read()
    print response
    
if __name__ == '__main__':
    #print ("Running from command line")
    main()
