import os
from chatroutes import ChatRoutes

api_key = os.environ.get('CHATROUTES_API_KEY', 'your-api-key-here')

client = ChatRoutes(api_key=api_key)

conversation = client.conversations.create({
    'title': 'Checkpoint Example',
    'model': 'gpt-5'
})

print(f"Created conversation: {conversation['id']}\n")

response1 = client.messages.send(
    conversation['id'],
    {
        'content': 'Explain quantum computing in simple terms.',
        'model': 'gpt-5'
    }
)

print(f"Response 1: {response1['assistantMessage']['content'][:100]}...\n")

response2 = client.messages.send(
    conversation['id'],
    {
        'content': 'What are some practical applications?',
        'model': 'gpt-5'
    }
)

print(f"Response 2: {response2['assistantMessage']['content'][:100]}...\n")

main_branch_id = conversation.get('branches', [{}])[0].get('id')
if not main_branch_id:
    branches = client.branches.list(conversation['id'])
    main_branch = next((b for b in branches if b['isMain']), None)
    if main_branch:
        main_branch_id = main_branch['id']

if main_branch_id:
    checkpoint = client.checkpoints.create(
        conversation['id'],
        branch_id=main_branch_id,
        anchor_message_id=response2['assistantMessage']['id']
    )

    print(f"Created checkpoint: {checkpoint['id']}")
    print(f"  Summary: {checkpoint['summary']}")
    print(f"  Token count: {checkpoint['token_count']}\n")

    checkpoints = client.checkpoints.list(conversation['id'])
    print(f"Total checkpoints: {len(checkpoints)}")
    for cp in checkpoints:
        print(f"  - {cp['id']}: {cp['summary'][:50]}... ({cp['token_count']} tokens)")

    response3 = client.messages.send(
        conversation['id'],
        {
            'content': 'Can you elaborate on quantum entanglement?',
            'model': 'gpt-5'
        }
    )

    print(f"\nResponse 3 (after checkpoint): {response3['assistantMessage']['content'][:100]}...")

    metadata = response3['assistantMessage'].get('metadata', {})
    if metadata:
        print(f"\nMessage metadata:")
        if 'checkpoint_used' in metadata:
            print(f"  Checkpoint used: {metadata['checkpoint_used']}")
        if 'context_truncated' in metadata:
            print(f"  Context truncated: {metadata['context_truncated']}")
        if 'context_message_count' in metadata:
            print(f"  Context message count: {metadata['context_message_count']}")
        if 'prompt_tokens' in metadata:
            print(f"  Prompt tokens: {metadata['prompt_tokens']}")

    print(f"\nDeleting checkpoint: {checkpoint['id']}")
    client.checkpoints.delete(checkpoint['id'])
    print("Checkpoint deleted successfully!")
else:
    print("Could not find main branch ID to create checkpoint")
