# Local Datacenter Lab

## Overview

This lab simulates a private datacenter using Docker containers on Docker Desktop and WSL2.

## Architecture

- Docker network: `datacenter-net`
- Network subnet: `10.30.1.0/24`
- Application container: `app-server` (`10.30.1.10`)
- Database container: `db-server` (`10.30.1.20`)
- Database: PostgreSQL
- Database name: `app_db`
- Application database role: `app_user`
- PostgreSQL port: `5432`

## Application

The Python application in `src/datacenter_app.py` connects to PostgreSQL, queries the `lab_check` table, and displays the stored records.

The application image is built using `src/Dockerfile` and `src/requirements.txt`.

## Build and Run

Build the image from the repository root:

```bash
docker build -t datacenter-app:1.0 ./src
```

Run it on the private network:

```bash
docker run --rm \
  --network datacenter-net \
  -e DB_HOST=10.30.1.20 \
  -e DB_PORT=5432 \
  -e DB_NAME=app_db \
  -e DB_USER=app_user \
  -e DB_PASSWORD='<lab-password>' \
  datacenter-app:1.0
```

Replace `<lab-password>` with the database user's lab password. Do not commit real credentials to Git.

## Validation

The application has successfully connected to PostgreSQL over the Docker network and retrieved a stored record.

## Limitations and Next Steps

This is a local simulation, not a deployed production datacenter. Next steps include improving secrets management, restricting database access, making service startup reproducible, and building the AWS environment with Terraform.
