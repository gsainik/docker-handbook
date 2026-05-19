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

<details>
<summary>
<h1>Steps to Create Containers and Run the Application</h1>
</summary>
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
</details>


<details>
<summary>
<h1>Docker Multi-Stage Builds and Distroless Images
</h1>
</summary>

This document explains:
- Docker Multi-Stage Builds
- Distroless Images
- Why modern production containers use them
- Security and optimization benefits
- Real-world usage patterns

---

## Why Optimization Is Needed?

Traditional Docker images often contain:
- Build tools
- Compilers
- Package managers
- Cache files
- Debugging tools
- Shell utilities

This causes:
- Large image sizes
- Slow deployments
- Increased security risks
- Unnecessary runtime dependencies

---

# Docker Multi-Stage Builds

## What is Multi-Stage Build?

Multi-stage build allows:
- multiple build stages
- multiple FROM statements
- separating build environment from runtime environment

Purpose:
- keep final image lightweight
- remove unnecessary build dependencies

---

## Traditional Docker Build

### Single Stage Example

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

---

### Problem with Single Stage

Final image contains:
- pip cache
- build dependencies
- temporary files
- unnecessary runtime tools

Result:
- larger image
- slower deployment

---

## Multi-Stage Build Flow

```text
Stage 1 - Build Stage
────────────────────────────

Install dependencies
Compile/build application
Run package installation

        ↓ Copy required files only

Stage 2 - Runtime Stage
────────────────────────────

Minimal runtime environment
Only application files
Only runtime dependencies
```

---

## Multi-Stage Dockerfile Example

```dockerfile
# Stage 1 - Builder
FROM python:3.11 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY . .

# Stage 2 - Runtime
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

CMD ["python", "app.py"]
```

---

## Important Understanding

### Stage 1

Purpose:
- install dependencies
- build application

Contains:
- temporary build environment

---

### Stage 2

Purpose:
- run application

Contains:
- only required runtime files

---

### COPY --from

```dockerfile
COPY --from=builder /app /app
```

Copies files:
- from previous stage
- into final runtime image

---

## Multi-Stage Build Diagram

```text
┌─────────────────────────┐
│ Stage 1 - Builder       │
│─────────────────────────│
│ Python                  │
│ Build tools             │
│ pip install             │
│ Dependencies            │
│ Source Code             │
└────────────┬────────────┘
             │
             │ COPY required files
             ▼
┌─────────────────────────┐
│ Stage 2 - Runtime       │
│─────────────────────────│
│ Minimal Python Runtime  │
│ Application Files       │
│ Runtime Dependencies    │
└─────────────────────────┘
```

---

## Advantages of Multi-Stage Builds

| Benefit | Description |
|---|---|
| Smaller image | Faster pull/push |
| Better security | Less unnecessary software |
| Faster deployment | Lightweight containers |
| Cleaner runtime | Production optimized |
| Reduced attack surface | Fewer tools installed |

---

### Real-World Usage

Commonly used in:
- Django
- FastAPI
- React
- Node.js
- Go applications
- Java microservices

---

# Distroless Images

## What is Distroless?

Distroless images contain:
- only application runtime
- no shell
- no package manager
- no Linux utilities

Purpose:
- ultra-minimal production containers

Introduced by:
- Google

---

## Traditional Image

```text
Linux OS
 + bash
 + apt
 + curl
 + package manager
 + runtime
 + application
```

---

## Distroless Image

```text
Runtime
 + application only
```

---

## Distroless Dockerfile Example

```dockerfile
FROM gcr.io/distroless/python3

WORKDIR /app

COPY . .

CMD ["app.py"]
```

---

## Distroless Image Diagram

```text
Traditional Image
────────────────────────────

┌──────────────────────┐
│ Linux OS             │
│ bash                 │
│ apt                  │
│ shell tools          │
│ Python Runtime       │
│ Application          │
└──────────────────────┘


Distroless Image
────────────────────────────

┌──────────────────────┐
│ Python Runtime       │
│ Application          │
└──────────────────────┘
```

---

## Advantages of Distroless Images

| Benefit | Description |
|---|---|
| Smaller image size | Faster deployments |
| Better security | Fewer attack vectors |
| Minimal runtime | Cleaner production |
| Reduced vulnerabilities | No unnecessary packages |
| Faster startup | Lightweight runtime |

---

## Important Limitation

Distroless images do NOT contain:
- bash
- sh
- apt
- curl
- package managers

So commands like:

```bash
docker exec -it <container> bash
```

will fail.

---

## Important Understanding

Distroless images are:
- production focused
- not debugging focused

---

# Multi-Stage + Distroless Combined

Modern production containers often use:
- Multi-stage builds
- Distroless runtime images

---

# Real Production Workflow

```text
Builder Stage
────────────────────
Install dependencies
Build application

        ↓

Distroless Runtime
────────────────────
Run only application
```

---

# Modern Production Dockerfile Example

```dockerfile
# Builder Stage
FROM python:3.11 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY . .

# Distroless Runtime Stage
FROM gcr.io/distroless/python3

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

CMD ["app.py"]
```

---

# Real Industry Usage

Widely used in:
- Kubernetes
- Microservices
- Cloud-native applications
- Production APIs
- Financial systems
- Security-sensitive systems

---

# Multi-Stage vs Distroless

| Multi-Stage Build | Distroless Image |
|---|---|
| Build optimization technique | Minimal runtime image |
| Multiple build stages | Minimal OS/runtime |
| Removes build junk | Removes Linux utilities |
| Smaller final image | Ultra-secure runtime |
| Flexible build workflow | Production-focused runtime |

---
</details>


<details>
<summary>
<h1>Docker Single Stage vs Multi-Stage vs Distroless Using Same Django Application
</h1>
</summary>


This document explains the difference between:
- Single Stage Docker Build
- Multi-Stage Docker Build
- Multi-Stage + Distroless Runtime

using the SAME Django application.

The goal is to clearly understand:
- Build Environment
- Runtime Environment
- Why Multi-Stage exists
- Why Distroless images are used in production

---

## Same Django Application

Assume the same Django project is used in all examples.

Project contains:

```text
manage.py
requirements.txt
templates/
views.py
models.py
```

---

## 1. Single Stage Dockerfile

### Dockerfile

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

### What Happens Here?

Everything happens inside ONE image:
- Build application
- Install dependencies
- Run application

Same image used for:
- building
- runtime

---

### Visual Mapping

```text
BUILDING
    +
RUNNING
    =
ONE BIG IMAGE
```

---

### Final Image Contents

```text
┌────────────────────────────┐
│ Linux OS                   │
│ Python                     │
│ pip                        │
│ shell/bash                 │
│ apt tools                  │
│ build cache                │
│ installed dependencies     │
│ Django app                 │
└────────────────────────────┘
```

---

### Problem with Single Stage

Final image still contains:
- pip
- shell
- Linux tools
- build dependencies
- unnecessary files

Result:
- larger image
- slower deployments
- less secure runtime

---

### Single Stage Diagram

```text
┌────────────────────────────┐
│ Build + Runtime Together   │
│────────────────────────────│
│ Python                     │
│ pip                        │
│ shell                      │
│ build tools                │
│ app                        │
└────────────────────────────┘
```

---

## 2. Multi-Stage Dockerfile

### Dockerfile

```dockerfile
# Stage 1 - Builder
FROM python:3.11 AS builder

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Stage 2 - Runtime
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

### What Changed?

Now:
- Build environment separated
- Runtime environment separated

---

### Stage 1 - Build Environment

```dockerfile
FROM python:3.11 AS builder
```

Temporary builder image created.

Contains:

```text
┌────────────────────────────┐
│ Linux OS                   │
│ Python                     │
│ pip                        │
│ shell/bash                 │
│ build tools                │
│ installed dependencies     │
│ Django app                 │
└────────────────────────────┘
```

Used ONLY for:
- installing dependencies
- preparing application

---

### Stage 2 - Runtime Environment

```dockerfile
FROM python:3.11-slim
```

A completely NEW image starts.

Initially contains:

```text
┌────────────────────────────┐
│ Slim Linux                 │
│ Python Runtime             │
└────────────────────────────┘
```

---

### COPY --from=builder

```dockerfile
COPY --from=builder /app /app
```

Copies ONLY:
- Django application

from Stage 1.

---

### Final Runtime Image

```text
┌────────────────────────────┐
│ Slim Linux                 │
│ Python Runtime             │
│ Django App                 │
└────────────────────────────┘
```

---

### What Improved?

Removed:
- heavy build tools
- unnecessary packages
- larger OS components

Still contains:
- shell
- Linux utilities

---

### Multi-Stage Diagram

```text
STAGE 1 - BUILDER
────────────────────────────

┌────────────────────────────┐
│ Python                     │
│ pip                        │
│ build tools                │
│ shell                      │
│ Django app                 │
└────────────┬───────────────┘
             │ COPY APP
             ▼

STAGE 2 - RUNTIME
────────────────────────────

┌────────────────────────────┐
│ Slim Linux                 │
│ Python Runtime             │
│ Django app                 │
└────────────────────────────┘
```

---

## 3. Multi-Stage + Distroless

### Dockerfile

```dockerfile
# Stage 1 - Builder
FROM python:3.11 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY . .

# Stage 2 - Distroless Runtime
FROM gcr.io/distroless/python3

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

CMD ["manage.py", "runserver", "0.0.0.0:8000"]
```

---

### Stage 1 - Builder

Same builder image:

```text
┌────────────────────────────┐
│ Linux                      │
│ Python                     │
│ pip                        │
│ shell                      │
│ build tools                │
│ dependencies               │
│ Django app                 │
└────────────────────────────┘
```

Used ONLY for:
- building
- dependency installation

---

### Stage 2 - Distroless Runtime

```dockerfile
FROM gcr.io/distroless/python3
```

Completely NEW minimal runtime image.

Initially contains ONLY:

```text
┌────────────────────────────┐
│ Python Runtime             │
└────────────────────────────┘
```

---

### COPY --from=builder

```dockerfile
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app
```

Copies ONLY:
- installed Python packages
- Django app

Does NOT copy:
- shell
- apt
- pip
- gcc
- build tools

---

### Final Distroless Runtime Image

```text
┌────────────────────────────┐
│ Python Runtime             │
│ Dependencies               │
│ Django App                 │
└────────────────────────────┘
```

---

### Distroless Runtime Diagram

```text
STAGE 1 - BUILDER
────────────────────────────

┌────────────────────────────┐
│ Linux                      │
│ Python                     │
│ pip                        │
│ shell                      │
│ build tools                │
│ app                        │
└────────────┬───────────────┘
             │ COPY ONLY REQUIRED FILES
             ▼

DISTROLESS RUNTIME
────────────────────────────

┌────────────────────────────┐
│ Python Runtime             │
│ Django App                 │
└────────────────────────────┘
```

---

## Key Difference Comparison

| Type | Final Image Contains |
|---|---|
| Single Stage | Everything |
| Multi-Stage | Smaller runtime + app |
| Distroless | Runtime + app only |

---

## Final Image Comparison

```text
SINGLE STAGE
────────────────────────────
Linux
Python
pip
shell
gcc
build tools
app


MULTI-STAGE
────────────────────────────
Slim Linux
Python
shell
app


MULTI-STAGE + DISTROLESS
────────────────────────────
Python Runtime
app only
```

---

# Most Important Understanding

Every:

```dockerfile
FROM
```

starts:
- completely NEW image stage

Only files explicitly copied using:

```dockerfile
COPY --from=builder
```

move from one stage to another.

---

# Final Learning Outcome

Successfully understood:
- Single-stage Docker builds
- Multi-stage Docker builds
- Build environment vs runtime environment
- Distroless runtime images
- Runtime image optimization
- Secure minimal production containers
- How COPY --from works in multi-stage builds

# Best Practices

## Use Multi-Stage Builds

For:
- production Docker images
- optimized deployments
- clean runtime containers

---

## Use Distroless Images

For:
- production workloads
- Kubernetes deployments
- secure applications

---

# Final Learning Outcome

Successfully understood:
- Multi-stage Docker builds
- Distroless image concepts
- Production container optimization
- Security-focused containerization
- Runtime image minimization
- Modern cloud-native container patterns

</details>


<details>
<summary>
<h1>Docker Volumes and Bind Mounts|Persistent Storage for Docker|</h1>
</summary>

This document explains:
- Docker Bind Mounts
- Docker Volumes
- Persistent Storage in Docker
- Differences between Volumes and Bind Mounts
- Real-world Docker storage concepts

---

## Why Storage Is Important in Docker?

Docker containers are:
- temporary
- isolated
- ephemeral

When container is deleted:
- application data is lost
- database data is lost
- uploaded files are lost

---

## Problem Without Persistent Storage

### Example

Suppose inside container:
- SQLite database created
- employee records inserted
- uploaded files stored

Then container deleted:

```text
docker rm <container>
```

Result:

```text
❌ All data lost
```

Because container filesystem is temporary.

---

## Solution

Docker provides:
- Bind Mounts
- Volumes

to persist data outside container lifecycle.

---

## Docker Storage Overview

```text
LOCAL MACHINE / DOCKER STORAGE
            │
            ▼
      Docker Container
```

Storage is connected between:
- host machine
- Docker container

---

# 1. Bind Mounts

## What is Bind Mount?

Bind mount directly maps:
- local folder
- into container folder

---

## Bind Mount Diagram

```text
LOCAL MACHINE
────────────────────────────

D:\django-project
│
├── views.py
├── models.py
├── templates/
└── db.sqlite3

        │
        │ Bind Mount
        ▼

DOCKER CONTAINER
────────────────────────────

/app
│
├── views.py
├── models.py
├── templates/
└── db.sqlite3
```

---

## Bind Mount Command

Using ```-v```
```bash
docker run -v ${PWD}:/app django-app
```
Using ```--mount```
```bash
docker run --mount type=bind,source=${PWD},target=/app django-app
```
---

## Command Understanding

| Part | Meaning |
|---|---|
| `${PWD}` | Current local directory |
| `/app` | Container directory |

---

## Important Bind Mount Behavior

Changes in local folder:
- instantly visible inside container

Example:
- edit views.py locally
- container immediately sees changes

---

## Bind Mount Workflow

```text
Edit Local File
        ↓
Container Automatically Sees Changes
        ↓
Django Auto Reloads
```

---

## Best Use Cases for Bind Mounts

- Development environments
- Live code editing
- Local debugging
- Django/FastAPI development
- Frontend hot reload

---

## Real Django Example

```bash
docker run -p 8000:8000 -v ${PWD}:/app django-app
```

Now:
- local project synced with container
- rebuild not needed for every code change

---

## Advantages of Bind Mounts

| Benefit | Description |
|---|---|
| Live code sync | No rebuild required |
| Easy debugging | Edit locally |
| Faster development | Instant updates |
| Simple workflow | Local IDE support |

---

## Limitations of Bind Mounts

| Limitation | Description |
|---|---|
| Host dependent | Depends on local filesystem |
| Less portable | Different host paths |
| Not ideal for production | Development-focused |

---

# 2. Docker Volumes

## What is Docker Volume?

Docker volume is:
- Docker-managed persistent storage

Docker itself stores and manages data.

---

## Docker Volume Diagram

```text
DOCKER MANAGED STORAGE
────────────────────────────

Volume: myvolume
│
├── database files
├── uploads
└── logs

        │
        │ Mounted Into
        ▼

DOCKER CONTAINER
────────────────────────────

/app/data
```

---

## Create Docker Volume

```bash
docker volume create myvolume
```

---

## Use Volume in Container

using ```-v```
```bash
docker run -v myvolume:/app/data django-app
```
using ```mount```
```bash
docker run \
--mount type=volume,source=myvolume,target=/app/data \
django-app
```

---

## Command Understanding

| Part | Meaning |
|---|---|
| `myvolume` | Docker-managed volume |
| `/app/data` | Container directory |

---

## Important Volume Behavior

Container deleted:

```bash
docker rm <container>
```

Volume still exists.

Data preserved.

---

## Volume Persistence Flow

```text
Container Deleted
        ↓
Volume Still Exists
        ↓
Data Preserved
```

---

## Best Use Cases for Volumes

- Databases
- PostgreSQL
- MySQL
- Redis persistence
- Production storage
- Uploaded files
- Logs

---

## Real PostgreSQL Example

```bash
docker run -v postgres-data:/var/lib/postgresql/data postgres
```

Now:
- DB survives container restart
- DB survives container deletion

---

## Advantages of Volumes

| Benefit | Description |
|---|---|
| Persistent storage | Data survives containers |
| Docker-managed | Easier production usage |
| Portable | Better portability |
| Production-ready | Common production practice |

---

## Volume Commands

### List Volumes

```bash
docker volume ls
```

---

### Inspect Volume

```bash
docker volume inspect myvolume
```

---

### Remove Volume

```bash
docker volume rm myvolume
```

---

## Full Comparison Diagram

```text
BIND MOUNT
────────────────────────────

Local Folder
      │
      ▼
Docker Container

Used For:
- development
- live code sync



DOCKER VOLUME
────────────────────────────

Docker Managed Storage
      │
      ▼
Docker Container

Used For:
- databases
- persistent production data
```

---

## Syntax Comparision

| `-v` Syntax | `--mount` Syntax |
----------------------------------------------- |
| `-v source:target` | `--mount type=TYPE,source=SOURCE,target=TARGET` |


## Key Difference Between Bind Mount and Volume

| Feature | Bind Mount | Volume |
|---|---|---|
| Storage Managed By | Host machine | Docker |
| Best For | Development | Production |
| Live code sync | Yes | No |
| Portability | Lower | Higher |
| Host path dependency | Yes | No |
| Persistent storage | Yes | Yes |

---

# Real Development Workflow

## Without Bind Mount

```text
Edit Code
    ↓
docker build
    ↓
docker run
```

Slow workflow.

---

## With Bind Mount

```text
Edit Code
    ↓
Container instantly sees changes
```

Fast development workflow.

---

## Real Production Workflow

Usually:
- Bind mounts for development
- Volumes for databases and persistence

---

## Secure Production Architecture

```text
Browser
    │
    ▼
Django Container
    │
    ▼
Docker Volume
(PostgreSQL Data)
```

---

# Important Docker Concepts Learned

Successfully understood:
- Docker persistent storage
- Bind mounts
- Docker volumes
- Live code synchronization
- Container data persistence
- Production storage concepts
- Development vs production storage workflows

</details>