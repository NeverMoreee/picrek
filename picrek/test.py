# py3
import requests
from lxml import etree

# Using for test
url = 'https://yande.re/post?tags=rating%3Asafe'
path = '/home/nemos/misc/pic/'
# end


class Pic(object):
    def __init__(self, picid, tags, smurl):
        self.picid = picid
        self.tags = tags
        self.smurl = smurl

    def __str__(self):
        return 'picid:' + str(self.picid)


class YPic(Pic):
    '''YPic for yande.re'''
    main_prefix = 'https://yande.re'
    pic_prefix = 'https://yande.re/post/show/'

    def __init__(self, picid, tags, smurl):
        super(YPic, self).__init__(picid, tags, smurl)

    def get_smurl(self):
        return self.smurl


class UrlPar(object):
    def __init__(self, url):
        self.pics = self.pics_par(self.html_par(self.get_html(url)))

    def __str__(self):
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
            # matched sample
            # @href: /post/show/370935
            # img/@src: https://assets.yande.re/data/preview/b4/86/b48679aebc400976e0d7c56903c19bab.jpg
            # img/@title: Rating: Safe Score: 12 Tags: animal_ears falkyrie_no_monshou heels kagetomo_midori maid nekomimi symmetrical_docking tail thighhighs User: Mr_GT'
            matched[0] = matched[0].split('/')[3]
            tags = []
            # index0: rating
            # index1: score
            # index2..: tags
            for x in matched[2].split(' '):
                if x in ('Rating:', 'Score:', 'Tags:'):
                    continue
                if x == 'User:':
                    break
                tags.append(x)
            pics.append(YPic(matched[0], tags, matched[1]))
        return pics


def downloader(pic):
    req = requests.get(pic.get_smurl())
    with open(path + pic.picid + '.jpg', 'wb') as f:
        f.write(req.content)
        print('downloading:' + pic.picid)


'''
urlpar = UrlPar(url)
for pic in urlpar.pics:
    downloader(pic)
'''
