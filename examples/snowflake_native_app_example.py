import snowflake.connector  # type: ignore

from contextual import ContextualAI

SF_BASE_URL = "xxxxx-xxxxx-xxxxx.snowflakecomputing.app"
BASE_URL = f"https://{SF_BASE_URL}/v1"

SAMPLE_MESSAGE = "Can you tell me about XYZ"

ctx = snowflake.connector.connect(  # type: ignore
    user="",  # snowflake account user
    password="",  # snowflake account password
    account="organization-account",  # snowflake organization and account <Organization>-<Account>
    session_parameters={"PYTHON_CONNECTOR_QUERY_RESULT_FORMAT": "json"},
)

# Obtain a session token.
token_data = ctx._rest._token_request("ISSUE")  # type: ignore
token_extract = token_data["data"]["sessionToken"]  # type: ignore

# Create a request to the ingress endpoint with authz.
api_key = f'"{token_extract}"'

client = ContextualAI(api_key=api_key, base_url=BASE_URL)

agents = [a for a in client.agents.list()]

agent = agents[0] if agents else None

if agent is None:
    print("No agents found")
    exit()
print(f"Found agent {agent.name} with id {agent.id}")

messages = [
    {
        "content": SAMPLE_MESSAGE,
        "role": "user",
    }
]

res = client.agents.query.create(agent.id, messages=messages)  # type: ignore

output = res.message.content  # type: ignore

print(output)
