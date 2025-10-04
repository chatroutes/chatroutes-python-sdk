# ChatRoutes Python SDK - Quick Start Guide

## Installation

### From PyPI (when published)

```bash
pip install chatroutes
```

### From Source

```bash
git clone https://github.com/chatroutes/chatroutes-python-sdk.git
cd chatroutes-python-sdk
pip install -e .
```

## Basic Usage

### 1. Initialize the Client

```python
from chatroutes import ChatRoutes

client = ChatRoutes(api_key="your-api-key")
```

### 2. Create a Conversation

```python
conversation = client.conversations.create({
    'title': 'My First Chat',
    'model': 'gpt-4'
})

print(f"Conversation ID: {conversation['id']}")
```

### 3. Send a Message

```python
response = client.messages.send(
    conversation['id'],
    {
        'content': 'Hello, how can I use ChatRoutes?',
        'model': 'gpt-4'
    }
)

print(response['assistantMessage']['content'])
```

### 4. Stream Responses

```python
def on_chunk(chunk):
    if chunk['choices'][0]['delta'].get('content'):
        print(chunk['choices'][0]['delta']['content'], end='', flush=True)

client.messages.stream(
    conversation['id'],
    {'content': 'Tell me about AI'},
    on_chunk=on_chunk
)
```

### 5. Create Branches

```python
branch = client.branches.create(
    conversation['id'],
    {
        'title': 'Alternative Discussion',
        'contextMode': 'FULL'
    }
)

client.messages.send(
    conversation['id'],
    {
        'content': 'Let\'s explore this differently',
        'branchId': branch['id']
    }
)
```

## Environment Setup

Create a `.env` file:

```bash
CHATROUTES_API_KEY=your-api-key-here
```

Then in your code:

```python
import os
from chatroutes import ChatRoutes

api_key = os.environ.get('CHATROUTES_API_KEY')
client = ChatRoutes(api_key=api_key)
```

## Common Patterns

### Error Handling

```python
from chatroutes import NotFoundError, RateLimitError

try:
    conv = client.conversations.get('conv_123')
except NotFoundError:
    print("Conversation not found")
except RateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after}s")
```

### List with Pagination

```python
page = 1
while True:
    result = client.conversations.list({
        'page': page,
        'limit': 10
    })

    for conv in result['data']:
        print(conv['title'])

    if not result.get('hasNext'):
        break

    page += 1
```

### Working with Branches

```python
branches = client.branches.list(conversation['id'])

for branch in branches:
    messages = client.branches.get_messages(
        conversation['id'],
        branch['id']
    )
    print(f"{branch['title']}: {len(messages)} messages")
```

## Next Steps

- Check out the [examples](examples/) directory for more detailed usage
- Read the [full documentation](https://docs.chatroutes.com)
- Explore the [API reference](https://api.chatroutes.com/docs)

## Support

- GitHub Issues: https://github.com/chatroutes/chatroutes-python-sdk/issues
- Email: support@chatroutes.com
- Documentation: https://docs.chatroutes.com
