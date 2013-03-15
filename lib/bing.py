import urllib
import urllib2
import json

class Bing:
      ENDPOINT = 'http://api.bing.net/json.aspx'

      def __init__(self, appid):
          self.appid = appid

      def search(self,**params):
          data = {}
          for k,v in params.items():
              data.update({k.replace('_','.'):v.replace(' ','+')})
          qs = urllib.urlencode(data).replace('%2B','+')
          url = '%s?Appid=%s&%s' % (self.ENDPOINT, self.appid, qs) 
          f = urllib2.urlopen(url)
          return json.loads(f.read())
  