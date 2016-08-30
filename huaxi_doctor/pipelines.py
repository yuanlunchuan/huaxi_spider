from .items import HuaxiDoctorItem
from scrapy.conf import settings
import pymongo

class HuaxiDoctorPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.post = tdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        doctorInfo = dict(item)
        self.post.insert(doctorInfo)
        return item
