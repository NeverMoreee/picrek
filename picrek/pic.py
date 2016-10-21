class Pic(object):
    def __init__(self, **kwarg):
        self.pid = kwarg['pid']
        self.rating = kwarg['rating']
        self.score = kwarg['score']
        self.tags = kwarg['tags']
        self.file = kwarg['file']
        self.sample = kwarg['sample']
        self.preview = kwarg['preview']

    def __str__(self):
        return 'pid:' + str(self.pid)


class GPic(Pic):
    """GPic for gelbooru"""
    main_url = 'https://gelbooru.com/'
    belong = 'gelbooru'

    def __init__(self, **kwarg):
        super(GPic, self).__init__(**kwarg)


class YPic(Pic):
    '''YPic for yande.re'''
    main_url = 'https://yande.re'
    belong = 'yandere'

    def __init__(self, **kwarg):
        super(YPic, self).__init__(**kwarg)
        self.jpeg = kwarg['jpeg']
