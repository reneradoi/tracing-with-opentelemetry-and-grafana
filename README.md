# Tracing with OpenTelemetry and Grafana

## Build and run application
`docker build -t world-countries:1.0 .`

`docker run -d -p 80:80 world-countries:1.0` or `docker-compose up -d`

## Grafana Explore
`sensible-browser http://localhost:3000`

-> TraceQL Query: `{.http.status_code = 404}`