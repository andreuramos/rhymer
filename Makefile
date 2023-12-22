up:
	docker-compose up -d

down:
	docker-compose down

rhyme:
	docker-compose exec python python app.py $(word 2, $(MAKECMDGOALS))

%:
	@: