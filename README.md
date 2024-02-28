## How to run the containerized version manually:
- Pull postgresql image from docker hub registry (we used postgres:16-alpine version): ```docker pull postgres:16-alpine```
- Create fastapi app image: ```docker build -t <image-name>:<tag> .```
- Create a custom network for the containers to communicate (With docker compose, that's done automatically): ```docker network create <network-name>```
- Create both containers (fastapi app, postgres)
    - Fastapi app: ```docker create -p8000:8000 --name <name> --network <network-name> --env-file .env <image-name>:<tag>```
    - Postgres: ```docker create -p5432:5432 --name database --network <network-name> --env-file .env postgres:16-alpine```
        - Database container name needs to be database, otherwise one should change the database url under app/database.py.
- Start both containers:
    - ```docker start database```
    - ```docker start <fastapi-container-name>```
- Access ```localhost:8000/docs``` .
- If everything worked fine, you should see the auto generated docs for the API where you could try the creation and retrieval of users and items.

## How to run everything with docker compose
- Run ```docker compose up``` to execute.
- Run ```docker compose down``` ro remove.
