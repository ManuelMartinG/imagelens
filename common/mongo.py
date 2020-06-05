import pymongo


class MongoClient:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["imagelens"]

        self.images_collection_name = "images"
        self.images = None

    def _dumb_init(self):
        entries = [{"imageid": "test.jpg", "imageblob": "AAA"}]
        _ids = self.images.insert_many(entries)
        print(_ids.inserted_ids)

    def start_up_database(self):
        self.db.create_collection(self.images_collection_name)
        self.images = self.db[self.images_collection_name]

    def get_images_collection(self):
        return self.db[self.images_collection_name]
