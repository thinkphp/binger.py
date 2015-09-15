import urllib2
import json

class Bing:

      def __init__( self, keyBing, searchString):

          self.credentialBing = 'Basic ' + (':%s' % keyBing).encode('base64')[:-1] 

          searchString = '%27'+searchString+'%27'

          top = 20

          offset = 0

          q = 'Query=%s&$top=%d&$skip=%d&$format=json' % (searchString, top, offset)

          self.url = 'https://api.datamarket.azure.com/Bing/Search/Web?'+ q

      def search( self ):

          request = urllib2.Request( self.url )

          request.add_header('Authorization', self.credentialBing )

          requestOpener = urllib2.build_opener()

          response = requestOpener.open( request ) 

          results = json.load(response)

          return results;


  