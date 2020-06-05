from kafka import KafkaProducer

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    while True:
        value = input("Send a message to a Kafka consumer: ")
        bytes_value = str.encode(value)
        producer.send("sample", bytes_value)

