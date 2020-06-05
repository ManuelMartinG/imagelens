from kafka import KafkaConsumer


class ImageProcessorConsumer(KafkaConsumer):
    def __init__(self, topic: str):
        self._consumer = super(ImageProcessorConsumer, self).__init__(topic)

    def get_next_image(self):
        for message in self._consumer:
            print(f"\nMessage: {message}")

