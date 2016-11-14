import peewee as pw

db = pw.MySQLDatabase('picrek', user='root', passwd='yi')


class Pic(pw.Model):
    pid = pw.IntegerField()
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


class Mysqldb(object):
    def __init__(self):
        db.connect()

    @staticmethod
    def insert_yan(pics):
        for p in pics:
            pic = Pic(pid=int(p.pid),
                      rating=p.rating,
                      score=int(p.score),
                      tags=p.tags,
                      file_url=p.file_url,
                      file_height=int(p.file_height),
                      file_width=int(p.file_width),
                      sample_url=p.sample_url,
                      sample_height=int(p.sample_height),
                      sample_width=int(p.sample_width),
                      preview_url=p.preview_url,
                      preview_height=int(p.preview_height),
                      preview_width=int(p.preview_width),
                      jpeg_url=p.jpeg_url,
                      jpeg_height=int(p.jpeg_height),
                      jpeg_width=int(p.jpeg_width)
                      )
            pic.save()
