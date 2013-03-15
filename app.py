import sys
sys.path.append('lib')
from bing import Bing

bing = Bing('49EB4B94127F7C7836C96DEB3F2CD8A6D12BDB71')

print bing.search(query='mootools',sources='web')

