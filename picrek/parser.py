from lxml import etree
from pic import *
import log

logger = log.get_logger('parser')

xmldoc = '<?xml version="1.0" encoding="UTF-8"?>'


def gel(xml):
    try:
        xml = xml.replace(xmldoc, '')
        par = etree.XML(xml)
        posts = par.xpath('//post')
        pics = []
        for post in posts:
            info                      = {}
            file                      = {}
            sample                    = {}
            preview                   = {}
            info['pid']               = post.xpath('@id')[0]
            info['rating']            = post.xpath('@rating')[0]
            info['tags']              = post.xpath('@tags')[0]
            info['score']             = post.xpath('@score')[0]
            file['file_url']          = post.xpath('@file_url')[0]
            file['file_height']       = post.xpath('@height')[0]
            file['file_width']        = post.xpath('@width')[0]
            sample['sample_url']      = post.xpath('@sample_url')[0]
            sample['sample_height']   = post.xpath('@sample_height')[0]
            sample['sample_width']    = post.xpath('@sample_width')[0]
            preview['preview_url']    = post.xpath('@preview_url')[0]
            preview['preview_height'] = post.xpath('@preview_height')[0]
            preview['preview_width']  = post.xpath('@preview_width')[0]
            info['file']              = file
            info['sample']            = sample
            info['preview']           = preview
            pics.append(GPic(**info))
    except Exception as e:
        logger.error(str(e))
    return pics


def yan(xml):
    try:
        xml = xml.replace(xmldoc, '')
        par = etree.XML(xml)
        posts = par.xpath('//post')
        pics = []
        for post in posts:
            info                      = {}
            file                      = {}
            sample                    = {}
            preview                   = {}
            jpeg                      = {}
            info['pid']               = post.xpath('@id')[0]
            info['rating']            = post.xpath('@rating')[0]
            info['tags']              = post.xpath('@tags')[0]
            info['score']             = post.xpath('@score')[0]
            file['file_url']          = post.xpath('@file_url')[0]
            file['file_height']       = post.xpath('@height')[0]
            file['file_width']        = post.xpath('@width')[0]
            jpeg['jpeg_url']          = post.xpath('@jpeg_url')[0]
            jpeg['jpeg_height']       = post.xpath('@jpeg_height')[0]
            jpeg['jpeg_width']        = post.xpath('@jpeg_width')[0]
            sample['sample_url']      = post.xpath('@sample_url')[0]
            sample['sample_height']   = post.xpath('@sample_height')[0]
            sample['sample_width']    = post.xpath('@sample_width')[0]
            preview['preview_url']    = post.xpath('@preview_url')[0]
            preview['preview_height'] = post.xpath('@preview_height')[0]
            preview['preview_width']  = post.xpath('@preview_width')[0]
            info['jpeg']              = jpeg
            info['file']              = file
            info['sample']            = sample
            info['preview']           = preview
            pics.append(YPic(**info))
    except Exception as e:
        logger.error(str(e))
    return pics


