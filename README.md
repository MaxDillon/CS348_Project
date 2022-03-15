# CS348_Project


### How To Test

- Open the Project Directory: `cd CS348_Project`
- run command: `docker compose up`
- Access the website through `localhost:3000`
- Make API Queries to Server through `localhost:80` or `localhost`
  - Run arbitrary SQL Code: `localhost/testQuery/[SQL Query]`
    - Example: `localhost/testQuery/SELECT * FROM Customer`
  - Run ORM example for getting Customers `localhost/printCustomers`
- When finished testing `Ctrl-C` to exit server
- If needed, run `docker image prune` and `docker container prune`
  - These commands will remove cached files and make starting the server slower
  - For the most part, there shouldn't be any reason to run these 
