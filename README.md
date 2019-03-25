# Unreliable server

This is a simple FastAPI server designed to:

1. provide a testing server for Pingdom and other blackbox monitoring tools
2. provide some testing resources to allow people to check that their code is handling errors and timeouts correctly.

It exposes four routes:

- `/` - hello world
- `/items/{item_id}`- echoes item_id
- `/heartbeat` - tells you if the server is up
- `/error` - will return a `404`, `408`, or `500` error randomly
- `/timeout`- will take 40 seconds to respond, more than likely to trigger a timeout in your http code.

It is normally running at:

http://unreliable.labs.crossref.org/

See OpenAPI docs at:

http://unreliable.labs.crossref.org/docs

## To build

`docker build -t unreliable .`

## To run

`docker run --name unreliable-server -p 5066:80 unreliable`

or

`docker-compose up -d`

or

`docker stack deploy -c docker-compose.yml unreliable_server`
