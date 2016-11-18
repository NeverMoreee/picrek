class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError('Cant change const %s.' % name)
        if not name.isupper():
            raise self.ConstCaseError(
                'const name %s is not all uppercase' % name)
        self.__dict__[name] = value


const = _const()
const.API_YANDERE = 'https://yande.re/post.xml'
const.API_GELBOORU = 'http://www.gelbooru.com/index.php?page=dapi&s=post&q=index'

const.DEF_LIMIT = 100
const.DEF_PAGE = 1
const.DEF_PROXY = None
const.ATM_TIME = 3

const.GET_INFO = 'getting:{website}, page: {page}, limit: {limit}, proxy；{proxy}'
const.GOT_INFO = 'time: {time}s, code:{code}'
const.GOT_ERR = 'timeout'

const.XMLDOC = '<?xml version="1.0" encoding="UTF-8"?>'

