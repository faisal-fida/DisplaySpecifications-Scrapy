# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.utils.project import get_project_settings


class DisplayspecificationsPipeline:

    def __init__(self):

        self.conn = pymongo.MongoClient(
            get_project_settings().get('MONGODB_SERVER'),
            get_project_settings().get('MONGODB_SERVER_PORT')
        )
        db = self.conn[get_project_settings().get('MONGODB_DATABASE')]
        self.collection = db[get_project_settings().get('MONGODB_COLLECTION')]

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
