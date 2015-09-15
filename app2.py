import sys
sys.path.append('lib2')
from bing2 import Bing

appID = 'Hko5cXg5U8h/WIE46pYQjmo/MLXNNkXYr+VXx/a66Ig' #get your own AppId from Azure Microsoft Bing

bing = Bing(appID, 'mootools')

print bing.search()

