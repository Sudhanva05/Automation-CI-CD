 # 🚀 Automated CI/CD Pipeline with Docker, GitHub Actions, and Watchtower

## 📌 Project Overview

This project demonstrates a **fully automated CI/CD pipeline** for a containerized FastAPI application.

Whenever code is pushed to GitHub:

1. GitHub Actions automatically **builds a Docker image**
2. The image is **pushed to DockerHub**
3. Watchtower detects the new image
4. The running container is **automatically updated**

This creates a **true Continuous Integration and Continuous Deployment (CI/CD) system**.

---

# 🏗 Architecture

Developer
↓
GitHub Repository
↓
GitHub Actions (CI)
↓
Docker Image Build
↓
Push to DockerHub
↓
Watchtower monitors DockerHub
↓
Automatic container update (CD)

---

# ⚙ Technologies Used

* **Python**
* **FastAPI**
* **Uvicorn**
* **Docker**
* **DockerHub**
* **GitHub Actions**
* **Watchtower**
* **CI/CD Automation**

---

# 📂 Project Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

# 🚀 How the CI/CD Pipeline Works

### Step 1 — Developer pushes code

```
git push origin main
```

---

### Step 2 — GitHub Actions runs

GitHub Actions will:

* Install dependencies
* Build Docker image
* Push image to DockerHub

---

### Step 3 — Watchtower detects new image

Watchtower periodically checks DockerHub for updated images.

When a new image is detected:

* The container is stopped
* The latest image is pulled
* The container restarts automatically

---

# 🐳 Running the Application

### Pull the Docker image

```
docker pull sudhanva591/automation-ci-cd
```

### Run the container

```
docker run -d -p 8000:8000 --name cicd-app sudhanva591/automation-ci-cd
```

---

# 🔄 Enable Automatic Deployment (Watchtower)

```
docker run -d \
--name watchtower \
-e DOCKER_API_VERSION=1.44 \
-v /var/run/docker.sock:/var/run/docker.sock \
containrrr/watchtower \
--interval 30
```

This will automatically update containers when new images are pushed.

---

# 🌐 Access the Application

```
http://localhost:8000
```

Example response:

```
{"message": "Hello All CI/CD is working"}
```

---

# 📈 Key Features

✔ Automated Docker image builds
✔ Continuous Integration using GitHub Actions
✔ Automatic deployments with Watchtower
✔ Containerized FastAPI application
✔ Zero manual deployment steps

---

# 🎯 Learning Outcomes

Through this project I learned:

* Docker containerization
* CI/CD pipeline automation
* GitHub Actions workflow automation
* Container monitoring with Watchtower
* Real-world DevOps deployment practices

---

# 👨‍💻 Author

**Sudhanva J Rao**

Final Year Engineering Student
DevOps & AI Enthusiast

---

