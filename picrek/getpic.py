import requests
import log

logger = log.get_logger('getpic')

proxy = {
    'http': '47.89.53.92:3128',
}
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
}


def yan(url='https://yande.re/post.xml',
        limit =100, page=1 , tags=None, proxy=None):
    try:
        param = {'page': page, 'limit': limit, 'tags': tags}
        req = requests.get(url, proxies=proxy, params=param)
        logger.info('yandere:status_code:%d, page:%d, limit:%d' %
                    (req.status_code, page, limit))
    except Exception as e:
        logger.error(str(e))
    return req.text


def gel(url='http://gelbooru.com/index.php?page=dapi&s=post&q=index',
        limit=100, pid=1, tags=None, proxy=None):
    try:
        param = {'pid': pid, 'limit': limit, 'tags': tags}
        req = requests.get(url, proxies=proxy, params=param)
        logger.info('gelbooru:status_code:%d, pid:%d, limit:%d' %
                    (req.status_code, pid, limit))
    except Exception as e:
        logger.error(str(e))
    return req.text
