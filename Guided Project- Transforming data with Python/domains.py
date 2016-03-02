import read
from collections import Counter
#from urlparse import urlparse
#import tldextract

df = read.load_data()
urls = df.url

urls_domain = []

"""
for x in urls:
    url = urlparse.urlparse(address)
    length = len(url.hostname.split('.'))
    domain = url.hostname.split('.')[(length-2):]
    urls_domain.append(domain)

print(urls_domain)
"""



"""
for x in urls:
    extracted = tldextract.extract(str(x))
    urls_domain.append("{}.{}".format(extracted.domain, extracted.suffix))
    
print(urls_domain)
"""




urls_counts = urls.value_counts()
first100 = urls_counts[:10]
for name, row in first100.items():
    print("{0}: {1}".format(name, row))
    