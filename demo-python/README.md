# otel-demo-python

## This file consists of all the commands needed to set up and run this demo using Docker and OpenTelemetry. 🚀

### Installation

# install python dependancies
 pip3 install -r requirements.txt

# install opentelemetry instrumentation dependancies
 opentelemetry-bootstrap -a install

# list all installed python packages
  pip3 list







 Instrumentation on console



### Containerization of flask app

# build the container image for the flask app

 docker build -t flaskapp:v1 .




### Run LGTM Stack + Python flask container

# create a network in docker

docker network create my-net

# run lgtm stack container
 docker run -p 3000:3000 -p 4317:4317 -p 4318:4318  -dit \
--network my-net --name otel-lgtm grafana/otel-lgtm

# run python app & send all telemetry data to grafana via otlp
  docker run -dit -p 3010:3000 --network my-net  \
-e OTEL_TRACES_EXPORTER=otlp \
-e OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://otel-lgtm:4317 \
-e OTEL_METRICS_EXPORTER=otlp \
-e OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://otel-lgtm:4317 \
-e OTEL_LOGS_EXPORTER=otlp \
-e OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://otel-lgtm:4317 \
-e OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true \
-e OTEL_SERVICE_NAME=flask-app \
--name flask  flaskapp:v1


### Grafana URL

http://localhost:3000

Username: admin
Password: admin
