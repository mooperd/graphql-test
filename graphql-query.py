from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import pprint

header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJPbmVHcmFwaCIsImF1ZCI6Imh0dHBzOi8vc2VydmUub25lZ3JhcGguY29tL2Rhc2hib2FyZC9hcHAvMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwiaWF0IjoxNjE2OTExNDI2LCJleHAiOjE2MTY5OTc4MjZ9.mZkofuj42PbD1-rk9TRszIGNlVivLrAOJTSZj3hwz_c"}

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(headers=header, url="http://localhost:8080/v1/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
query = gql(
    """query MyQuery{
            town {
                name
                county {
                    id
                    name
                    country {
                        id
                        name
                    }
                }
            }
        }"""
)

# Execute the query on the transport
result = client.execute(query)
pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(result)


