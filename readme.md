# GraphQL sample

Developed on OSX with Docker Desktop

Start hasura and psql:
`docker-compose up`

Inject data from uk-towns-sample.csv into psql database:
`python3 import.py`

Access the Hasura interface from http://localhost:8080. In the 'data' tab ->
"Untracked tables or views" -> click "Track All". Then 
"Untracked foreign-key relationships" -> "Track All"

You can then run:
`python3 graphql-query.py` to run a basic graphQL query against Hasura.


