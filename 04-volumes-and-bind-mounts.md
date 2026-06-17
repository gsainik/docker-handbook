
# Docker Volumes and Bind Mounts|Persistent Storage for Docker

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
|---|---|
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

---