This document provides instructions to connect a pgadmin docker container with a postgresql server running in another docker container.

It's useful for the following:
- Don't need to install pgadmin locally.
- Easy access/inspection to docker database

2 different approaches are available:
- Manually run every needed container
- Run it with docker compose file

## Manually run every needed container

These are the steps to follow:
1. Create a network to have enable communication between containers: ```docker network create <network-name>```
2. Create the postgresql container: ```docker create --name <postgresql-cont-name> -p5432:5432 -e POSTGRES_USER=<user-name> -e POSTGRES_PASSWORD=<password> -e POSTGRES_DB=<db-name> --network <network-name> postgres:<tag>```
3. Create the pgadmin container: ```docker create --name <pgadmin-cont-name> -p80:80 -e "PG_ADMIN_DEFAULT_EMAIL=<default-email>" -e "PGADMIN_DEFAULT_PASSWORD=<default-password>" --network <network-name> dpage/pgadmin4```
4. Start the postgres container: ```docker start <postgresql-cont-name>```
5. Start the pgadmin container: ```docker start <pgadmin-cont-name>```

If everything worked fine, you should be able to access ```http://localhost:80``` and pgadmin login page should appear (if not, wait a few seconds, pgadmin initialization usually takes some seconds). Once you reached the login page, follow these steps:
1. Enter with the credentials you specified when creating the pgadmin container
![pgAdmin Login](/public/pgadmin-login.PNG)
2. Register a new server: Servers > Register > Server
![pgAdmin Server creation](/public/pgadmin-server-creation.PNG)
3. In General tab, specify a name (doesn't really matter which name)
![pgAdmin Server name](/public/pgadmin-servername.PNG)
4. Go to Connection tab. 
5. Fill the missing fields:
    - Host name/address: Write the name of the postgresql container ```<postgresql-cont-name>```
    - Leave port a 5432
    - Modify Username with the username you set to the postgresql container ```<user-name>```
    - Modify Password with the password you set to the postgresql container ```<password>```
    
    ![pgAdmin Connection details](/public/pgadmin-connection-details.PNG)

6. Click Save. Now the server should load correctly and you should be able to see your default database ```<db-name>```. In this example case, this name is root2.
![pgAdmin final load](/public/pgadmin-end.PNG)

## Run it with docker compose file
First, inspect the docker-compose.pgadmin.yml file.
1. Run the containers: ```docker compose --file docker-compose.pgadmin.yml up```
2. Follow the same steps as in steps from the manual option but using the credentials/data specified in the docker compose file we used to run it.
3. To end the execution: ```docker composer --file docker-compose.pgadmin.yml down```