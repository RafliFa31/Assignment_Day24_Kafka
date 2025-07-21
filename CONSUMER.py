from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry.protobuf import ProtobufDeserializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from proto.event_pb2 import Event

schema_registry_conf = {'url': 'http://localhost:8081'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

protobuf_deserializer = ProtobufDeserializer(Event, schema_registry_client)

consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'key.deserializer': str,
    'value.deserializer': protobuf_deserializer,
    'group.id': 'protobuf-group',
    'auto.offset.reset': 'earliest'
}

consumer = DeserializingConsumer(consumer_conf)
consumer.subscribe(['event-protobuf'])

total = 0
count = 0

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue

    event = msg.value()
    print(f"Consumed: {event}")
    total += event.value
    count += 1
    print(f"Running Average: {total / count:.2f}")
