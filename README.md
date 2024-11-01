# Nexus node docker exporter

This exporter for nnd.

- Work with prometheus - approve 

## Metrics
### nnd_log_line 
- Last log line in docker container

## Needs
* docker
* docker compose
* make

## .env

### CONTAINER_ID
- id or name of taget container

## docker-compose.yml
``` yml
version: "3.5"
services:
    nnd-exporter:
        image: fargus3222/nnd-exporter
        restart: unless-stopped
        ports:
          - "8082:8080"
        volumes:
            - /var/run/docker.sock:/var/run/docker.sock
        environment:
          - CONTAINER_ID=${CONTAINER_ID}
```
## Deploy

``` bash
$ make init
```

