import requests_1

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests_1.get("http://www.pythonhow.com", headers = headers)
# print (r)
# print(r.text[:100])
print (__name__)
print (r["text"][:100])
# import pprint
#
# content= dict(text="""<!DOCTYPE html>
# <!--[if IE 7]>
# <html class="ie ie7" lang="en-US" prefix="og: http://ogp.me/ns#">""")
#
# print (content)