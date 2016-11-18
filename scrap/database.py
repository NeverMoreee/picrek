import peewee as pw
from .log import get_logger

logger = get_logger('database')

db = pw.MySQLDatabase('picrek', user='root', passwd='yi')


class Yandere(pw.Model):
    pid = pw.IntegerField(primary_key=True)
    rating = pw.CharField()
    score = pw.IntegerField()
    tags = pw.CharField()
    file_url = pw.CharField()
    file_height = pw.IntegerField()
    file_width = pw.IntegerField()
    sample_url = pw.CharField()
    sample_height = pw.IntegerField()
    sample_width = pw.IntegerField()
    preview_url = pw.CharField()
    preview_height = pw.IntegerField()
    preview_width = pw.IntegerField()
    jpeg_url = pw.CharField()
    jpeg_height = pw.IntegerField()
    jpeg_width = pw.IntegerField()

    class Meta:
        database = db


def init():
    db.connect()
    # try:
    #     db.create_table(Yandere)
    # except Exception as e:
    #     logger.error(str(e))


def insert_yan(pics):
    for p in pics:
        pic = Yandere(pid=int(p.pid),
                      rating=str(p.rating),
                      score=int(p.score),
                      tags=str(p.tags),
                      file_url=str(p.file_url),
                      file_height=int(p.file_height),
                      file_width=int(p.file_width),
                      sample_url=str(p.sample_url),
                      sample_height=int(p.sample_height),
                      sample_width=int(p.sample_width),
                      preview_url=str(p.preview_url),
                      preview_height=int(p.preview_height),
                      preview_width=int(p.preview_width),
                      jpeg_url=str(p.jpeg_url),
                      jpeg_height=int(p.jpeg_height),
                      jpeg_width=int(p.jpeg_width)
                      )
        pic.save()


