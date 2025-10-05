import os
from chatroutes import ChatRoutes

api_key = os.environ.get('CHATROUTES_API_KEY', 'your-api-key-here')

client = ChatRoutes(api_key=api_key)

conversation = client.conversations.create({
    'title': 'Streaming Example',
    'model': 'gpt-5'
})

print(f"Created conversation: {conversation['id']}\n")

def on_chunk(chunk):
    if chunk.get('type') == 'content' and chunk.get('content'):
        print(chunk['content'], end='', flush=True)

def on_complete(response):
    print("\n\nStreaming complete!")
    print(f"Full response saved")

print("Assistant: ", end='', flush=True)

client.messages.stream(
    conversation['id'],
    {
        'content': 'Write a short poem about programming in Python',
        'model': 'gpt-5',
        'temperature': 0.8
    },
    on_chunk=on_chunk,
    on_complete=on_complete
)
