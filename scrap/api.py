import requests
import time
from .log import get_logger
from .err import ConnectException
from .constant import const

logger = get_logger('api')


def yandere(url=const.API_YANDERE,
            limit=const.DEF_LIMIT, page=const.DEF_PAGE,
            proxy=const.DEF_PROXY, atm_time=1):
    logger.info(const.GET_INFO.format(website='yandere',
                page=page, limit=limit, proxy=proxy))
    param = {'page': page, 'limit': limit}
    beftime = time.time()
    try:
        req = requests.get(url, proxies=proxy, params=param)
    except Exception as e:
        logger.error(str(e))
        if atm_time <= const.ATM_TIME:
            yandere(page=page, limit=limit, atm_time=atm_time + 1)
        else:
            raise ConnectException(const.GOT_ERR)
    else:
        afttime = time.time()
        costime = afttime - beftime
        logger.info(const.GOT_INFO.format(time=costime, code=req.status_code))
        return req.text


def gelbooru(url=const.API_GELBOORU,
             limit=const.DEF_LIMIT, page=const.DEF_PAGE,
             proxy=const.DEF_PROXY, atm_time=1):
    logger.info(const.GET_INFO.format(website='gelbooru',
                page=page, limit=limit, proxy=proxy))
    # pid = pageid
    param = {'pid': page, 'limit': limit}
    beftime = time.time()
    try:
        req = requests.get(url, proxies=proxy, params=param)
    except Exception as e:
        logger.error(str(e))
        if atm_time <= const.ATM_TIME:
            yandere(page=page, limit=limit, atm_time=atm_time + 1)
        else:
            raise ConnectException(const.GOT_ERR)
    else:
        afttime = time.time()
        costime = afttime - beftime
        logger.info(const.GOT_INFO.format(time=costime, code=req.status_code))
        return req.text
