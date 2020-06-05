from common.mongo import MongoClient


class ImageLensManager:

    def __init__(self):
        self.mongoclient = MongoClient()

    def insert_image(self, imageid, imageblob):
        self.mongoclient.insert({
            "imageid": imageid,
            "imageblob": imageblob
        })
