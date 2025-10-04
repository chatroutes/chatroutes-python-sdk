import os
from chatroutes import ChatRoutes

api_key = os.environ.get('CHATROUTES_API_KEY', 'your-api-key-here')

client = ChatRoutes(api_key=api_key)

conversation = client.conversations.create({
    'title': 'Python SDK Example',
    'model': 'gpt-4'
})

print(f"Created conversation: {conversation['id']}")

response = client.messages.send(
    conversation['id'],
    {
        'content': 'Hello! Can you explain what ChatRoutes is?',
        'model': 'gpt-4'
    }
)

print(f"\nUser: {response['userMessage']['content']}")
print(f"Assistant: {response['assistantMessage']['content']}")

conversations = client.conversations.list({'limit': 5})
print(f"\nTotal conversations: {conversations['total']}")

branch = client.branches.create(
    conversation['id'],
    {
        'title': 'Alternative Discussion',
        'contextMode': 'FULL'
    }
)

print(f"\nCreated branch: {branch['id']}")
