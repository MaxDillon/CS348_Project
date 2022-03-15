# CS348_Project

### Git Rules
- When making new changes, always make a branch (honor system cuz need pro version to inforce)
- When merging changes, create pull request for code review
  - Format pull request title to be clear statement of intent
- Try to keep pull requests kinda short/localized to one feature
  - Helps with debugging
  - If you are working on two things that don't directly rely on eachother, make 2 branches


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
Our Project for CS 348