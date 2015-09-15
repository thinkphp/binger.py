import sys
sys.path.append('lib')
from bing import Bing

appID = 'Hko5cXg5U8h/WIE46pYQjmo/MLXNNkXYr+VXx/a66Ig'

bing = Bing(appID)

print bing.search(query='mootools',sources='web')

