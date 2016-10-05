# py3
import requests
from lxml import etree


class Pic(object):
    def __init__(self, picid, tags, smurl):
        self.picid = picid
        self.tags = tags
        self.smurl = smurl

    def __str__(self):
        return 'picid:' + str(self.picid)


class YPic(Pic):
    main_prefix = 'https://yande.re'
    pic_prefix = 'https://yande.re/post/show/'

    def __init__(self, picid, tags, smurl):
        super(YPic, self).__init__(picid, tags, smurl)


class UrlPar(object):
    def __init__(self, url):
        self.pics = self.pics_par(self.html_par(self.get_html(url)))

    def __str__(self):
        '''
        if self.pics:
            return 'empty'
        '''
        str_ = ''
        for pic in self.pics:
            str_ += str(pic) + '\n'
        return str_

    def get_html(self, url):
        req = requests.get(url)
        return req.text

    def html_par(self, html):
        return etree.HTML(html)

    def pics_par(self, parsered):
        pics = []
        a_eles = parsered.xpath('//a[@class="thumb"]')
        for a_ele in a_eles:
            matched = a_ele.xpath('@href| img/@src| img/@title')
            matched[0] = matched[0].split('/')[3]
            tags = []
            for x in matched[2].split(' '):
                if x in ('Rating:', 'Score:', 'Tags:'):
                    continue
                if x == 'User:':
                    break
                tags.append(x)
            pics.append(YPic(matched[0], tags, matched[1]))
        return pics


url = UrlPar('https://yande.re/post?tags=rating%3Asafe')
print (url)
