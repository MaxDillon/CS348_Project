# How To Use Docker

- Make Sure to [install docker desktop](https://docs.docker.com/get-docker/)
	- Run `docker -v` to verify it is properly installed
- cd into client/react-app `cd react-app`
- run `docker build -t reactapp .`
- run `docker run -p 3000:3000 reactapp`
	- I will modify dockerfile and shell scripts to make this easier later
	- React App should now be running. Go to localhost:3000
- Close server with `Ctrl-C`
- When you are finished with rinning and debugging, run `docker container prune`
