import os
from chatroutes import ChatRoutes

api_key = os.environ.get('CHATROUTES_API_KEY', 'your-api-key-here')

client = ChatRoutes(api_key=api_key)

conversation = client.conversations.create({
    'title': 'Branching Example',
    'model': 'gpt-4'
})

print(f"Created conversation: {conversation['id']}\n")

response1 = client.messages.send(
    conversation['id'],
    {
        'content': 'What are the benefits of Python?',
        'model': 'gpt-4'
    }
)

print(f"Main branch response: {response1['assistantMessage']['content'][:100]}...\n")

branch = client.branches.fork(
    conversation['id'],
    {
        'forkPointMessageId': response1['userMessage']['id'],
        'title': 'Alternative Perspective',
        'contextMode': 'FULL'
    }
)

print(f"Created fork at message: {response1['userMessage']['id']}")
print(f"New branch ID: {branch['id']}\n")

response2 = client.messages.send(
    conversation['id'],
    {
        'content': 'What are the challenges of Python?',
        'model': 'gpt-4',
        'branchId': branch['id']
    }
)

print(f"Branch response: {response2['assistantMessage']['content'][:100]}...\n")

branches = client.branches.list(conversation['id'])
print(f"Total branches in conversation: {len(branches)}")
for b in branches:
    print(f"  - {b['title']} (ID: {b['id']}, Main: {b['isMain']})")

tree = client.conversations.get_tree(conversation['id'])
print(f"\nConversation tree:")
print(f"  Total nodes: {tree['metadata']['totalNodes']}")
print(f"  Total branches: {tree['metadata']['totalBranches']}")
print(f"  Max depth: {tree['metadata']['maxDepth']}")
