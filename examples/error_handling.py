import os
from chatroutes import (
    ChatRoutes,
    ChatRoutesError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ServerError
)

api_key = os.environ.get('CHATROUTES_API_KEY', 'your-api-key-here')

client = ChatRoutes(api_key=api_key)

try:
    conversation = client.conversations.create({
        'title': 'Error Handling Example',
        'model': 'gpt-5'
    })

    print(f"Created conversation: {conversation['id']}")

except AuthenticationError as e:
    print(f"Authentication failed: {e.message}")
    print("Please check your API key")

except ValidationError as e:
    print(f"Validation error: {e.message}")
    if e.details:
        print(f"Details: {e.details}")

except RateLimitError as e:
    print(f"Rate limit exceeded: {e.message}")
    if e.retry_after:
        print(f"Retry after {e.retry_after} seconds")

except NotFoundError as e:
    print(f"Resource not found: {e.message}")

except ServerError as e:
    print(f"Server error: {e.message}")
    print("Please try again later")

except ChatRoutesError as e:
    print(f"ChatRoutes error: {e.message}")
    print(f"Status code: {e.status_code}")
    if e.code:
        print(f"Error code: {e.code}")

try:
    non_existent = client.conversations.get('invalid-id')

except NotFoundError:
    print("\nCaught NotFoundError for invalid conversation ID")

print("\nError handling complete!")
