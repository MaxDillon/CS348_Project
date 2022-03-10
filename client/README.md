# How To Use Docker

- Make Sure to [install docker desktop](https://docs.docker.com/get-docker/)
	- Run `docker -v` to verify it is properly installed
- cd into this directory
- run `docker build -t reactapp .`
- run `docker run -p 3000:3000 -v --rm pythonapp`
	- I will modify dockerfile and shell scripts to make this easier later
	- React App should now be running. Go to localhost:3000
- Close server with `Ctrl-C`
