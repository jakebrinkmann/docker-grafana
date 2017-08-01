.PHONY: vertest docker-deps-up docker-deps-up-nodaemon docker-deps-down clean

# pull the tag from version.py
TAG=0.0.1
WORKERIMAGE=chameleon-admin-console:$(TAG)

DCD:=docker-compose -f docker-compose.yml

vertest:
	echo $(TAG)
	echo $(WORKERIMAGE)

docker-deps-up:
	$(DCD) up -d

docker-deps-up-nodaemon:
	$(DCD) up --build

docker-deps-down:
	$(DCD) down

clean:
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -delete


