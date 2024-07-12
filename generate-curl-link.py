import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key and endpoint from environment variables
api_key = os.getenv('APPSYNC_API_KEY')
graphql_endpoint = os.getenv('APPSYNC_ENDPOINT')

# Ensure that the environment variables are set
if not api_key or not graphql_endpoint:
    raise EnvironmentError("APPSYNC_API_KEY and APPSYNC_ENDPOINT must be set as environment variables.")

# Define the GraphQL query
graphql_query = """
query MyQuery {
  getTodo(id: "f9cbdfc3-b8f1-4ee6-b82c-1b5e66f62bac") {
    description
    id
    name
    when
    where
  }
}
"""


escaped_query = graphql_query.replace('\n', '').replace('"', '\\"')

# Construct the curl command string
curl_cmd = (
    f"curl -i -H 'Content-Type: application/json' "
    f"-H 'x-api-key:{api_key}' "
    f"-X POST -d '{{\"query\": \"{escaped_query}\"}}' "
    f"{graphql_endpoint}"
)

def generateCurlLink():
    print(curl_cmd)

print("Generating curl link to AppSync endpoint")
generateCurlLink()
print("Finished generating curl link to AppSync endpoint")
