### source: https://kafka.apache.org/quickstart

```bash
# Start Zookeper Server
bin/zookeeper-server-start.sh config/zookeeper.properties

# In another process start a Kafka Server
bin/kafka-server-start.sh config/server.properties

# Create a Topic
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

# List Topics
bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# Send some messages
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test
> This is a message

# Start a consumer
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

# To check which pid is running on port {PORT}
lsof -i tcp:{PORT}

# Kill PID
kill -9 {PID}
```

### Hello world in Kafka: https://timber.io/blog/hello-world-in-kafka-using-python/
1. Kafka is run as a cluster on one or more servers
2. Kafka stores a stream of records in categories called topics. Each record consists of a key, value and a timestamp
3. Kafka works on the publish-subscribe pattern. It allows some of the applications to act as producers and publish the records to Kafka topics. Similarly, it allows some of the applications to act as consumers and subscribe to Kafka topics and process the records produced by it
4. Alongside, Producer API and Consumer API, Kafka also offers Streams API for an application to work as a stream processor and Connector API through which we can connect Kafka to other existing applications and data systems

### How to launch a complete example
```bash
# Start Zookeper Server
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka Server
bin/kafka-server-start.sh config/server.properties

# Create a `sample` Topic
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sample

# Set up a consumer flusher
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sample --from-beginning # or python kafka/consumer.py

# Open up an interactive producer
python kafka/producer.py
```