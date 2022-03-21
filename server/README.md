# Setup
- Runn app with docker compose
- Run `docker exec cs348_project-server-1 create_schema`
	- This will generate the sqlalchemy code for the database

# How To Use Docker

- Make Sure to [install docker desktop](https://docs.docker.com/get-docker/)
	- Run `docker -v` to verify it is properly installed
- cd into this directory `cd server`
- run `docker build -t pythonapp .`
- run `docker run -p 8080:5000 -v $(pwd):/app pythonapp`
	- I will modify dockerfile and shell scripts to make this easier later
	- Python Server should now be running. Go to localhost:8080
	- Edits to server should automatically update the docker container
		- This is a bit janky and i'll make it better in the future
- Close the server with `Ctrl-C`
- When done with debugging
	- run `docker container prune`
	- run `docker image prune`
