import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key, endpoint, and token from environment variables
api_key = os.getenv('APPSYNC_API_KEY')
graphql_endpoint = os.getenv('APPSYNC_ENDPOINT')
auth_token = os.getenv('AUTHORIZATION_TOKEN')  # Ensure this token is set in your .env file

# Ensure that the environment variables are set
if not api_key or not graphql_endpoint or not auth_token:
    raise EnvironmentError("APPSYNC_API_KEY, APPSYNC_ENDPOINT, and AUTHORIZATION_TOKEN must be set as environment variables.")

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

# Construct the cURL command string with the authorization token
curl_cmd = (
    f"curl -i -H 'Content-Type: application/json' "
    f"-H 'x-api-key: {api_key}' "
    f"-H 'Authorization: {auth_token}' "
    f"-X POST -d '{{\"query\": \"{escaped_query}\"}}' "
    f"{graphql_endpoint}"
)

def generateCurlLink():
    print(curl_cmd)

print("Generating cURL link to AppSync endpoint")
generateCurlLink()
print("Finished generating cURL link to AppSync endpoint")
