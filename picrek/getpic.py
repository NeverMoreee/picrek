import requests

# test
yapi = 'https://yande.re/post.xml'
gapi = 'http://gelbooru.com/index.php?page=dapi&s=post&q=index&limit=100&pid=1'
proxy = {
    'http': '47.89.53.92:3128',
}
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
}
# end


def get_ypic(url, limit=100, page=1, tags=None, proxy=None):
    req = requests.get(url, proxies=proxy
                       params=dict([('limit', limit), ('page', page), ('tags': tags)]))
    return req.text


def get_gpic(url, limit=100, pid=1, tags=None, proxy=None):
    # pid = pageid
    req = requests.get(url, proxies=proxy,
                       params=dict([('limit', limit), ('pid', pid), ('tags', tags)]))
    return req.text

