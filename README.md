# sheepfish-vpn-service
SheepFish VPN Service

## Run project:
1) Setup variable's values in the `.env.sample` file.
2) Execute `docker-compose build` command in Terminal to build project image.
3) Execute `docker-compose up` to up a project container.
4) Browse `127.0.0.1:8000` or `localhost:8000` url.

## About project
This project requires login and has simple interface to add proxy for sites.
Routing through proxy sites takes place through regular expressions.
Because the task said only to replace saved links, all links were not replaced with proxy links.
Only created links in the database.
Commits are not divided into stages of development in order to complete the task as quickly as possible.