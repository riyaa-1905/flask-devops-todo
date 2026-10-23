# Flask DevOps To-Do Application

## Project Overview

This project implements an end-to-end DevOps pipeline for a Flask-based To-Do web application. It demonstrates how an application can be developed, tested, containerized, and monitored using DevOps tools.

## Objectives

- Develop a working web application using Flask.
- Manage source code using Git and GitHub.
- Automate testing and Docker image builds using GitHub Actions.
- Containerize the application using Docker.
- Run the application and monitoring tools using Docker Compose.
- Monitor application metrics using Prometheus and Grafana.

## Technologies Used

- **Python and Flask** — Web application development
- **Git and GitHub** — Version control and source code hosting
- **GitHub Actions** — Continuous Integration (CI)
- **pytest** — Automated testing
- **Docker** — Application containerization
- **Docker Compose** — Running the application and monitoring services
- **Prometheus** — Metrics collection
- **Grafana** — Monitoring dashboards

## Application Features

- Add and manage To-Do tasks.
- Delete tasks.
- Mark tasks as completed.
- Filter tasks by status and priority.
- Expose application metrics for monitoring.

## DevOps Pipeline

The project demonstrates the following workflow:

1. Write and update application code.
2. Push code to GitHub.
3. Trigger the GitHub Actions CI workflow.
4. Install dependencies and run automated tests.
5. Build the Docker image.
6. Run the application and monitoring services using Docker Compose.
7. Collect application metrics with Prometheus.
8. Visualize monitoring metrics in Grafana.

## Project Structure

```text
flask-devops-todo/
├── .github/
│   └── workflows/
│       └── ci.yml
├── monitoring/
│   ├── prometheus.yml
│   └── grafana-dashboard.json
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Running the Project

### Prerequisites

- Python
- Docker
- Docker Compose
- Git

### Run with Docker Compose

From the project root directory, run:

```bash
docker compose up -d --build
```

Access the services at:

- **To-Do application:** http://localhost:5000
- **Prometheus:** http://localhost:9090
- **Grafana:** http://localhost:3000

To check the running containers:

```bash
docker compose ps
```

To stop the services:

```bash
docker compose down
```

Do not use `docker compose down -v` if you want to preserve the named Grafana data volume.

## Testing and Continuous Integration

Automated tests are written using pytest. The GitHub Actions workflow runs the tests and builds the Docker image when code is pushed or a pull request is opened against the `main` branch.

Run tests locally with:

```bash
pytest -v
```

## Monitoring

Prometheus collects application metrics from the Flask application's `/metrics` endpoint.

Grafana connects to Prometheus and displays monitoring information through the **Flask DevOps Monitoring** dashboard, including application status, request rate, and average response time.

## Conclusion

This project demonstrates practical use of source control, automated testing, continuous integration, containerization, and application monitoring in an end-to-end DevOps workflow.
