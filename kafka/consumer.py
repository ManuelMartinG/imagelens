from kafka import KafkaConsumer


if __name__ == "__main__":
    consumer = KafkaConsumer("sample")
    for message in consumer:
        print(f"\nMessage: {message}")
