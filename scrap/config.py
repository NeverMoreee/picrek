import json
import os
import log

logger = log.get_logger('config')


class Config(object):
    def __init__(self):
        self.cwd = os.getcwd()
        self.conf_path = os.path.join(self.cwd, 'config.json')

        try:
            if(not os.path.exists(self.conf_path)):
                self.data = {}
                self.data['gelbooru'] = {}
                self.data['gelbooru']['cur_pid'] = 1
                self.data['gelbooru']['count'] = 1
                self.data['yandere'] = {}
                self.data['yandere']['cur_pid'] = 1
                self.data['yandere']['count'] = 1
                with open(self.conf_path, 'w') as f:
                    json.dump(self.data, f)
            else:
                with open(self.conf_path, 'r') as f:
                    self.data = json.load(f)
        except Exception as e:
            logger.error(str(e))
        else:
            logger.info('config init')

    def save(self):
        with open(self.conf_path, 'w') as f:
            json.dump(self.data, f)
