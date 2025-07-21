from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry.protobuf import ProtobufSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from proto.event_pb2 import Event
import random
import time

schema_registry_conf = {'url': 'http://localhost:8081'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

protobuf_serializer = ProtobufSerializer(
    Event,
    schema_registry_client
)

producer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'key.serializer': str.encode,
    'value.serializer': protobuf_serializer
}

producer = SerializingProducer(producer_conf)

while True:
    event = Event(id=random.randint(1, 100), value=random.uniform(10.0, 100.0))
    producer.produce(topic='event-protobuf', key=str(event.id), value=event)
    print(f"Produced: {event}")
    time.sleep(5)
