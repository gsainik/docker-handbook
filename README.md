# docker-handbook

A Docker Image is a read-only blueprint that contains the instructions for creating a container, while a Docker Container is a live, running instance of that image

### What is a Container?
- a container is a lightweight, standalone, and executable software package that contains everything needed to run an application: code, runtime, system tools, libraries, and settings

### What is Docker?

- Docker is a containerization platform used to package applications with dependencies

### What is an Image?

- A read-only template used to create containers.
A Docker image is a read-only, lightweight, and standalone executable file that serves as a blueprint for creating Docker containers. It packages together everything needed to run an application—including the code, runtime, system libraries, tools, and settings—ensuring it runs the same way in any environment

### Difference between VM and Docker?

- VM includes full OS; Docker shares host OS kernel and is lightweight.


Docker LifeCycle

There are three important things,

- docker build -> builds docker images from Dockerfile
- docker run -> runs container from docker images
- docker push -> push the container image to public/private regestries to share the docker images.


## Most Important Understanding
Docker Image = Saved packaged application

Docker Container = Running application from image


Dockerfile → Builds → Image
Image → Runs → Container


| Image | Container |
|---|---|
| Blueprint | Running app |
| Static | Dynamic |
| Read-only | Executable |
| Template	| Instance |

---

# Important Docker Concepts Learned

## Docker Image

- Blueprint/template
- Created using docker build

---

## Docker Container

- Running instance of image
- Created using docker run

---

## docker run vs docker start

| Command | Purpose |
|---|---|
| docker run | Creates NEW container |
| docker start | Starts EXISTING container |

---

## docker ps vs docker ps -a

| Command | Purpose |
|---|---|
| docker ps | Running containers |
| docker ps -a | All containers |


---
| Command | Purpose |
|---|---|
| Stop Container | docker stop <container_id> |
| Remove Container | docker rm <container_id> |
| Remove Image | docker rmi myapp |

## Container Persistence Understanding

Learned:
- Running docker run again creates NEW container
- SQLite data not available in new container
- Existing container can be restarted using:

```bash
docker start -a <container_id>
```



## Step 1 - Open Existing Django Project

Moved into local project folder:

```bash
cd <project-folder>
```

## Step 2 - Build Docker Image

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




### Final Learning Outcome

Successfully learned:
- Docker Desktop installation
- Docker image creation
- Docker container lifecycle
- Django containerization
- Port mapping
- docker exec usage
- Container persistence behavior
- Running Django inside Docker container