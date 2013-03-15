# Binger

A simple client for Microsoft's Bing API Search.

# Install

```
$ git clone git://github.com/thinkphp/binger.py.git
$ cd binger.py
$ python app.py
$ => output
```

# Usage

Results as JSON
```
bing = Bing('your-api-key')

print bing.search(query='MooTools',sources='web')
print bing.search(query='jQuery',sources='web image')
print bing.search(query='Dojo',sources='news')

```

Results as XML

```
bing = Bing('your-api-key','xml')

print bing.search(query='mootools',sources='web')
# => xml.dom.minidom.Document instance at 0x00D4F5A8>
```

# License

MIT

