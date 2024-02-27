## How to run the containerized version manually:
- Pull postgresql image from docker hub registry (we used postgres:16-alpine version)
- Create fastapi image: ```docker build -t <image-name>:<tag> .```
- Create both containers (fastapi app, postgres)
    - Fastapi app: ```docker create -p8000:8000 --name <name> --network <mynet> <image-name>:<tag>```
    - Postgres: ```docker create -p5432:5432 --name <name> --network mired -e POSTGRES_USER=common_user -e POSTGRES_PASSWORD=password_default -e POSTGRES_DB=fastapi_docker_db postgres:16-alpine```
        - Note that POSTGRES_USER and POSTGRES_PASSWORD are the same values that we set in the database.py file, Changing it to adapt it to your naming conventions.
- Start both containers:
    - ```docker start <fastapi-container-name>```
    - ```docker start <postgres-container-name>```
- Access ```localhost:8000/docs``` .
- If everything worked fine, you should see the auto generated docs for the API where you could try the creation and retrieval of users and items.

## How to run everything with docker compose
tbd
