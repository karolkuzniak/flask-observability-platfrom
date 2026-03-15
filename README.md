# Flask Observability Platform

A DevOps-style observability platform demonstrating monitoring, logging, load testing and CI/CD for a Python Flask application.

The project integrates **Prometheus, Grafana, Loki and Promtail** to create a full monitoring stack.

---

# Architecture

Flask application exposes metrics and logs which are collected and visualized using an observability stack.

Flow:

Flask Application  
→ Prometheus → Grafana (metrics)  

Flask Logs  
→ Promtail → Loki → Grafana (logs)  

Load testing  
→ Locust  

---

# Stack

Technologies used:

- Python
- Flask
- Docker
- Docker Compose
- Prometheus
- Grafana
- Loki
- Promtail
- Locust (load testing)
- GitHub Actions (CI/CD)

---

# Project Structure

flask-observability-platform

app  
- app.py  
- requirements.txt  

docker  
- Dockerfile  

monitoring  
- prometheus.yml  
- loki.yml  
- promtail.yml  

grafana  
- dashboards  
  - flask-dashboard.json  
- provisioning  

loadtest  
- locustfile.py  

docker-compose.yml  
README.md  

---

# Running the Platform

Start the full observability stack:

```
docker compose up --build
```

Services available:

Flask API  
http://localhost:5000  

Prometheus  
http://localhost:9090  

Grafana  
http://localhost:3000  

Locust (load testing)  
http://localhost:8089  

---

# Metrics

The Flask application exposes Prometheus metrics at:

```
http://localhost:5000/metrics
```

Example metrics:

- flask_requests_total
- flask_errors_total

These metrics are collected by Prometheus and visualized in Grafana dashboards.

---

# Dashboard

📸 **SCREENSHOT HERE**

Add screenshot here showing Grafana dashboard with request and error metrics.

Example file location:

docs/grafana-dashboard.png

Usage in README:

```
![Grafana Dashboard](docs/grafana-dashboard.png)
```

---

# Prometheus

Prometheus scrapes metrics from the Flask application and stores time-series data.

📸 **SCREENSHOT HERE**

Add screenshot showing Prometheus targets page.

Example:

docs/prometheus-targets.png

---

# Logging

Application logs are collected using:

Promtail → Loki → Grafana

This enables centralized log storage and log querying directly in Grafana.

📸 **SCREENSHOT HERE**

Add screenshot showing logs in Grafana (Loki datasource).

Example:

docs/grafana-logs.png

---

# Load Testing

Traffic simulation is implemented using Locust.

Run the load test:

```
locust -f loadtest/locustfile.py
```

Open the Locust UI:

```
http://localhost:8089
```

Example test scenario:

- requests to `/`
- simulated errors using `/error`

This generates metrics visible in Grafana dashboards.

📸 **SCREENSHOT HERE**

Add screenshot showing Locust load test UI.

Example:

docs/locust-test.png

---

# CI/CD

The repository includes a GitHub Actions pipeline.

Pipeline steps:

1. Checkout repository
2. Install Python dependencies
3. Run lint checks
4. Build Docker image
5. Validate docker-compose configuration

The pipeline runs automatically on every push to the repository.

📸 **SCREENSHOT HERE**

Add screenshot showing GitHub Actions pipeline passing.

Example:

docs/github-actions.png

---

# Purpose

This project demonstrates a complete observability workflow including:

- application metrics
- centralized logging
- dashboards
- load testing
- CI/CD automation

The goal is to simulate a production-style monitoring setup for microservices.

---

# Author

@karolkuzniak