import asyncio

from graphqlclient import GraphQLClient

gc = GraphQLClient("ws://domain:<port>/graphql")
query = """
{
  students{
    id
    name
    age

  }
}
"""
# resp = gc.execute(query)
# print(resp)

sub = """
subscription {
  teacher{
    mutation
    updatedFields
    node{
      id
      name
      age
    }
  }
}
"""


async def main():
    s = gc.subscription(sub)
    await s.start()
    async for i in s.listen():
        print(i)


asyncio.get_event_loop().run_until_complete(main())
