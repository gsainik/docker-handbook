
# Steps to Create Containers and Run the Application


## Step 1 - Open Existing Django Project

Local project folder or Clone the Github repo to Any local Path

```bash
cd <project-folder>
```
or

```bash
git clone <github-repo>
```

## Step 2 - Build Docker Image

- pwd should be the path where ```Dockerfile``` is present inside project folder.
```bash
./<project-folder>
```

Built Docker image:
```bash
docker build -t django-app .
```

### Important Understanding

### docker build:

Creates:
- Docker image

The dot (`.`) means:
- Current folder
- Build context

Docker reads:
- Dockerfile
- requirements.txt
- project source code

from current directory.

---
List Images
```bash
docker images
```

## Step 3 - Run Docker Container

Started Django container:

```bash
docker run -p 8000:8000 django-app
docker run -p 8000:8000 -it <imageid>
```

---

### Port Mapping Understanding

Post Mapping Syntax:
```bash
docker run -p HOST_PORT:CONTAINER_PORT image-name
```

```bash
-p 8000:8000
```

Means:

```text
Laptop Port 8000 or <ec2-public-ip>
        ↓
Container Port 8000
```

Application accessible at:

```text
http://localhost:8000  or 

http://<ec2-public-ip>:8000
```

## Step 4  - Verify Running Container

View running containers:

```bash
docker ps
```

View all containers:

```bash
docker ps -a
```


## Step 5 - Access Application

Open browser:

```text
http://localhost:8000/employees/
```

---




## Final Learning Outcome

Successfully learned:
- Docker Desktop installation
- Docker image creation
- Docker container lifecycle
- Django containerization
- Port mapping
- docker exec usage
- Container persistence behavior
- Running Django inside Docker container

---

