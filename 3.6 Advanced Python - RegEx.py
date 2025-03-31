import re

teks = 'rambut'
x = re.match('^r....t$', teks)
print(x)

tx = "bapak punya 1000 rambut putih"
x = re.split('\s', tx)
print(x)
d = re.sub('\d+', '98kml', tx)
print(d)
c = re.search('^bapak.*putih$', tx)
print(c)

web = 'http://huhuhi.com/ #juaraindo'
x = re.sub('http[s]?\://\S+', '_', web)
print(x)
y = re.findall('#[_]*[a-z]+', web)
print(y)