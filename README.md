# CS348_Project

### How To Test
- Install Docker Desktop: https://www.docker.com/products/docker-desktop/
- Start Docker Desktop
- `git clone https://github.com/MaxDillon/CS348_Project.git` 
- `cd CS348_Project`
- `docker compose build`
- `docker compose up`
- For Debugging (Developers Only) 
  - If docker commands aren't working:
    - Make sure you restart Docker Desktop
  - If server error when communicating with Database
    - `docker image prune`
    - `rm -rf postgres/postgres/postgres-data`
    - `docker compose build`
    - `docker compose up`
  - If client is giving "cant find module" errors
    - `docker image prune`
    - `npm i --package-lock-only`
    - `docker compose build`
    - `docker compose up`
