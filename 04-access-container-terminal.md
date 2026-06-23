# Accessing a Running Container Terminal Using docker exec

The `docker exec` command allows us to open a terminal session inside an already running container.

---

## Syntax

```bash
docker exec -it <container-name-or-id> <shell>
```

Where:

- `exec` → Execute a command inside a running container.
- `-i` → Interactive mode (keep STDIN open).
- `-t` → Allocate a terminal (TTY).
- `<shell>` → Shell to open (`bash` or `sh`).

---

## Using Bash Shell

```bash
docker exec -it mypython /bin/bash
```

or

```bash
docker exec -it mypython bash
```

### Purpose

Opens an interactive Bash terminal inside the container.

### Requirement

The container image must have Bash installed.

Common examples:

- Ubuntu
- Debian
- Jenkins

---

## Using SH Shell

```bash
docker exec -it mypython sh
```

or

```bash
docker exec -it mypython /bin/sh
```

### Purpose

Opens a lightweight shell inside the container.

### Common Images

- Alpine Linux
- Python Alpine
- Redis Alpine
- BusyBox

---

## Example: Python Alpine Container

Image:

```text
python:alpine3.23
```

Open terminal:

```bash
docker exec -it mypython2 sh
```

Expected output:

```text
/app #
```

or

```text
/ #
```

---

## Why Bash May Fail

If Bash is not installed:

```bash
docker exec -it mypython2 bash
```

Error:

```text
exec: "bash": executable file not found in $PATH
```

In this case, use:

```bash
docker exec -it mypython2 sh
```

---

## Checking Available Shells

Inside the container:

```bash
which sh
which bash
```

Example:

```text
/usr/bin/sh
```

No output for Bash means Bash is not installed.

---

## Difference Between bash and sh

| Feature | bash | sh |
|----------|------|-----|
| Full-featured shell | ✅ | ❌ |
| Lightweight | ❌ | ✅ |
| Available in Alpine | ❌ Usually No | ✅ Yes |
| Available in Ubuntu | ✅ Yes | ✅ Yes |
| Commonly used for debugging | ✅ | ✅ |

---

## Difference Between docker run -it and docker exec -it

### Create New Container

```bash
docker run -it python:alpine3.23 sh
```

Creates a brand-new container and opens a terminal.

---

### Open Existing Container

```bash
docker exec -it mypython2 sh
```

Opens a terminal in an already running container.

---

## Visual Representation

```text
Docker Image
      │
      ▼
docker run
      │
      ▼
Running Container
      │
      ├── docker exec -it sh
      ├── docker exec -it sh
      └── docker exec -it sh
```

Multiple terminal sessions can be opened into the same running container.

---

## Important Note

`docker exec` works only for running containers.

Check running containers:

```bash
docker ps
```

If the container is stopped:

```bash
docker start <container-name>
```

Then access it:

```bash
docker exec -it <container-name> sh
```

---

## Key Learning

- `docker run -it` → Creates a new container and opens a terminal.
- `docker exec -it` → Opens a terminal in an existing running container.
- Use `bash` if available.
- Use `sh` for Alpine-based containers.
- Container must be running before using `docker exec`.