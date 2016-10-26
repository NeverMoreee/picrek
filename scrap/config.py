import json
import os
import log

logger = log.get_logger('config')

cwd = os.getcwd()
conf_path = os.path.join(cwd, 'config.json')

def init():
    try:
        if(not os.path.exists(conf_path)):
            data = {}
            data['gelbooru'] = {}
            data['gelbooru']['cur_id'] = 1
            data['gelbooru']['sum'] = 1
            data['yandere'] = {}
            data['yandere']['cur_id'] = 1
            data['yandere']['sum'] = 1
            with open(conf_path, 'w') as f:
                json.dump(data, f)
        else:
            with open(conf_path, 'r') as f:
                data = json.load(f)
    except Exception as e:
        logger.error(str(e))
        return None
    else:
        logger.info('config init')
        return data
