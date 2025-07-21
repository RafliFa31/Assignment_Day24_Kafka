# Assignment_Day24_Kafka
This project demonstrates a simple real-time ETL pipeline using Apache Kafka and PySpark Streaming.

Requirements
1.Docker & Docker Compose
2. Python around 3.8+
3. PySpark
4. kafka-python

langkah menjalankan
1. Jalankan Kafka Cluster menggunakan : docker-compose up -d
2. Install protobuf compiler: pip install protobuf
3. Lalu compile: protoc --python_out= event.proto     
4. Jalankan Producer cd producer , python producer.py
5. Jalankan Consumer : cd consumer, python consumer.py
6. Akses UI Kafka
   Kafka UI: http://localhost:8080
   Schema Registry: http://localhost:8081
   KsqlDB Server: http://localhost:808
