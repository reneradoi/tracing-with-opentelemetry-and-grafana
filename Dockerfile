FROM python:3.9-slim-bullseye

WORKDIR /src

COPY requirements /src/requirements

RUN pip install --no-cache-dir --upgrade -r /src/requirements \
    && chmod 777 /src \
    && opentelemetry-bootstrap -a install \
    && useradd -g operator -u 1000 -m operator

COPY world_countries.py /src/world_countries.py

USER operator

CMD ["opentelemetry-instrument", "--traces_exporter", "otlp", "--metrics_exporter", "none", "--service_name", "world-countries", "--exporter_otlp_endpoint", "http://tempo:4317", "uvicorn", "world_countries:app", "--host", "0.0.0.0", "--port", "80"]
