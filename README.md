# SecureMe Mini — AWS ECS Flask Application

## 📌 Overview

**SecureMe Mini** is a lightweight web application designed to demonstrate the creation and deployment of a cloud-based, containerized application using Amazon Web Services.
The application presents simple cybersecurity tips and a checklist through a clean web interface.

This project focuses on **cloud architecture, containerization, and deployment**, rather than complex application logic.

---

## 🎯 Purpose of the Project

The goal of this project was to:

* Build a simple Flask web application
* Containerize it using Docker
* Store the container image in Amazon Elastic Container Registry (ECR)
* Deploy and run the application using Amazon Elastic Container Service (ECS)
* Expose the application through an Application Load Balancer (ALB)
* Serve static assets (banner image) from Amazon S3 using environment variables

---

## 🛠️ Technologies Used

* **Python (Flask)** — Web application framework
* **Docker** — Containerization
* **Amazon ECR** — Container image registry
* **Amazon ECS (Fargate)** — Container orchestration
* **Application Load Balancer (ALB)** — Traffic routing
* **Amazon S3** — Static file storage
* **AWS Cloud9** — Development environment

---

## 🧩 Application Structure

```
.
├── application/
│   ├── app.py
│   ├── templates/
│   └── static/
├── infrastructure/
│   ├── Dockerfile
│   └── deployment scripts
└── README.md
```

* **application/** — Flask application source code
* **infrastructure/** — Dockerfile and deployment-related files
* **README.md** — Project documentation

---

## 🚀 Deployment Architecture

1. The Flask application is containerized using Docker.
2. The Docker image is pushed to **Amazon ECR**.
3. An **ECS service** runs the container using Fargate.
4. An **Application Load Balancer** routes HTTP traffic to the running task.
5. A banner image is stored in **Amazon S3** and loaded dynamically using environment variables.

---

## ⚙️ Configuration

The application uses environment variables for configuration:

* `S3_BUCKET` — Name of the S3 bucket
* `S3_BANNER_KEY` — Banner image filename
* `AWS_REGION` — AWS region

This approach avoids hardcoding values and supports flexible deployments.

---

## 🌐 Accessing the Application

The application is accessible via the **Application Load Balancer DNS URL**, which routes requests to the running ECS task.

---

## 📚 Learning Outcomes

This project demonstrates:

* Container-based application design
* AWS service integration (ECR, ECS, ALB, S3)
* Environment-based configuration
* Real-world cloud deployment workflow

---

## 👤 Author

**Fred Junior NTWALI**
Course: *Creation and Administration of Cloud Based Application, 2025*

<img width="975" height="482" alt="ac563b37-f627-4d41-8bf2-322527b296bd" src="https://github.com/user-attachments/assets/953a480e-c9d0-4d6c-9832-1583d2dbdb75" />
<img width="975" height="546" alt="a86ff024-afb0-47b3-b874-7b5a260fb4fd" src="https://github.com/user-attachments/assets/23de0800-b304-445e-b2ec-3828a6872a02" />
<img width="975" height="550" alt="338625d5-c253-4d4c-81eb-d9a05ac55ea9" src="https://github.com/user-attachments/assets/74925ed9-5df7-4f95-a392-a296aacac416" />
<img width="975" height="545" alt="aa8e5db8-4ed1-4a70-95e1-b2ce743de97a" src="https://github.com/user-attachments/assets/65ebb16c-56db-4bcd-813c-da0e40c2af6e" />
