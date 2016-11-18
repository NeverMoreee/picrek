from lxml import etree
from collections import namedtuple
from .log import get_logger
from .err import ParserException
from .constant import const

logger = get_logger('parser')


def gelbooru(xml):
    Pic = namedtuple('Pic', ['pid', 'rating', 'score', 'tags',
                             'file_url', 'file_height', 'file_width',
                             'sample_url', 'sample_height', 'sample_width',
                             'preview_url', 'preview_height', 'preview_width'])
    try:
        xml = xml.replace(const.XMLDOC, '')
        par = etree.XML(xml)
    except Exception as e:
        logger.error(str(e))
        raise ParserException
    else:
        posts = par.xpath('//post')
        pics = []
        for post in posts:
            pic = Pic(post.xpath('@id')[0],
                      post.xpath('@rating')[0],
                      post.xpath('@score')[0],
                      post.xpath('@tags')[0],
                      post.xpath('@file_url')[0],
                      post.xpath('@height')[0],
                      post.xpath('@width')[0],
                      post.xpath('@sample_url')[0],
                      post.xpath('@sample_height')[0],
                      post.xpath('@sample_width')[0],
                      post.xpath('@preview_url')[0],
                      post.xpath('@preview_height')[0],
                      post.xpath('@preview_width')[0],
                      )
            pics.append(pic)
        return pics


def yandere(xml):
    Pic = namedtuple('Pic', ['pid', 'rating', 'score', 'tags',
                             'file_url', 'file_height', 'file_width',
                             'sample_url', 'sample_height', 'sample_width',
                             'preview_url', 'preview_height', 'preview_width',
                             'jpeg_url', 'jpeg_height', 'jpeg_width'])
    try:
        xml = xml.replace(const.XMLDOC, '')
        par = etree.XML(xml)
    except Exception as e:
        logger.error(str(e))
        raise ParserException
    else:
        posts = par.xpath('//post')
        pics = []
        for post in posts:
            pic = Pic(post.xpath('@id')[0],
                      post.xpath('@rating')[0],
                      post.xpath('@score')[0],
                      post.xpath('@tags')[0],
                      post.xpath('@file_url')[0],
                      post.xpath('@height')[0],
                      post.xpath('@width')[0],
                      post.xpath('@sample_url')[0],
                      post.xpath('@sample_height')[0],
                      post.xpath('@sample_width')[0],
                      post.xpath('@preview_url')[0],
                      post.xpath('@preview_height')[0],
                      post.xpath('@preview_width')[0],
                      post.xpath('@jpeg_url')[0],
                      post.xpath('@jpeg_height')[0],
                      post.xpath('@jpeg_width')[0]
                      )
            pics.append(pic)
        return pics


def count(xml):
    try:
        xml = xml.replace(const.XMLDOC, '')
        par = etree.XML(xml)
    except Exception as e:
        logger.error(str(e))
        raise ParserException
    else:
        return par.xpath('@count')[0]
