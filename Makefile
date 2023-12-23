up:
	docker-compose up -d

down:
	docker-compose down

rhyme:
	docker-compose exec python python rhyme.py $(word 2, $(MAKECMDGOALS))

%:
	@: