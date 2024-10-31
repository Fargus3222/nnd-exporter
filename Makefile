docker_build:
		docker build . -t fargus3222/nnd-exporter:latest

docker_push:
	docker tag fargus3222/nnd-exporter:latest fargus3222/nnd-exporter:$(shell git log -1 --format=%s)
	docker push fargus3222/nnd-exporter:$(shell git log -1 --format=%s)
	docker push fargus3222/nnd-exporter:latest
		

init:
		docker compose up -d --build

down:
		docker compose down


cleanup:
		docker system prune -a -f