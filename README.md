docker compose up --build

docker compose down


# Kafka

```
/opt/bitnami/kafka/bin/kafka-topics.sh \
  --bootstrap-server kafka:9092 \
  --create --topic test-kafka --partitions 2 --replication-factor 1
```