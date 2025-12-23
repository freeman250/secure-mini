# SecureMe Mini

**Simple Cybersecurity Habits Web Application**

## 📌 Project Overview

SecureMe Mini is a lightweight web application designed to promote basic cybersecurity best practices.
The application presents users with short security tips and a checklist, helping them build safer online habits in a simple and accessible way.

The project demonstrates how a containerized Flask application can be built, stored, and deployed using core Amazon Web Services.

---

## 🧩 Application Features

* Three pages: **Home**, **Security Tips**, and **Checklist**
* Banner image loaded dynamically from **Amazon S3**
* Environment-based configuration (no hardcoded cloud resources)
* Containerized using **Docker**
* Deployed on **Amazon ECS** with **Application Load Balancer**
* Publicly accessible through a single ALB DNS URL

---

## 🏗️ Architecture Overview

The application uses the following AWS services:

* **Docker** – Packages the Flask application into a container image
* **Amazon ECR (Elastic Container Registry)** – Stores the Docker image
* **Amazon ECS (Elastic Container Service)** – Runs the container as a managed service
* **Application Load Balancer (ALB)** – Routes HTTP traffic to the running container
* **Amazon S3** – Hosts the static banner image used by the application

All services work together to deliver a scalable and reliable cloud-based deployment.

---

## 📁 Project Structure

```text
.
├── application/
│   ├── app.py
│   ├── templates/
│   └── static/
├── infrastructure/
│   ├── Dockerfile
│   └── build.sh
├── README.md
```

* `application/` – Flask application source code
* `infrastructure/` – Docker and deployment-related files
* `README.md` – Project documentation

---

## 🐳 Docker Build & Push (Example)

```bash
docker build -t secureme-mini -f infrastructure/Dockerfile .
docker tag secureme-mini:latest 541373007083.dkr.ecr.us-east-1.amazonaws.com/secureme-mini:latest
docker push 541373007083.dkr.ecr.us-east-1.amazonaws.com/secureme-mini:latest
```

---

## 🚀 Deployment

* The Docker image is deployed to **Amazon ECS** as a service
* The service runs one task behind an **Application Load Balancer**
* The application is accessed using the **ALB DNS URL**
* Static banner image is fetched from **Amazon S3** using environment variables

---

## 🌐 Live Application

The application is accessible through the Application Load Balancer DNS URL provided by AWS after deployment.

---

## 🎓 Course Context

This project was developed as part of the course:

**Creation and Administration of Cloud Based Application, 2025**

It demonstrates practical usage of containerization and cloud deployment concepts covered during the course.

---
class 2025

Fred Junior NTWALI

<img width="975" height="482" alt="ac563b37-f627-4d41-8bf2-322527b296bd" src="https://github.com/user-attachments/assets/28eba687-78d6-4ab8-8465-f4d8f94dabaa" />
<img width="975" height="546" alt="a86ff024-afb0-47b3-b874-7b5a260fb4fd" src="https://github.com/user-attachments/assets/04f7f92c-368b-4423-8fdd-4c72b395f9d2" />
<img width="975" height="550" alt="338625d5-c253-4d4c-81eb-d9a05ac55ea9" src="https://github.com/user-attachments/assets/6dca1de5-63c2-4188-bcbb-27d43868faa8" />
<img width="975" height="545" alt="aa8e5db8-4ed1-4a70-95e1-b2ce743de97a" src="https://github.com/user-attachments/assets/a2b97a6c-e251-426a-a279-5b2ca6d25b5f" />



📘 Project Disclaimer

This project was created as part of a university course assignment (“Creation and Administration of Cloud Based Application, 2025”). It was initially based on a course-provided starter template (private classroom repository). I extended it by improving the UI, containerizing the Flask app with Docker, deploying it to Amazon ECS behind an Application Load Balancer, and loading static assets from Amazon S3 via environment variables.
