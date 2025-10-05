# Python SDK Update - October 5, 2025

## Response Format Fixes

### Issue 1: Send Message Response
The SDK was expecting `userMessage` and `assistantMessage` in the response, but the actual API returns only the assistant's message in a `message` field.

### Issue 2: Streaming Response Format
The SDK was expecting OpenAI-style streaming format with `choices` and `delta`, but the actual API uses a simpler format with `type` and `content` fields.

### Changes Made

#### 1. Updated Send Message Response Type

**File**: `chatroutes/types/conversation.py`

**Before**:
```python
class SendMessageResponse(TypedDict):
    userMessage: Message
    assistantMessage: Message
```

**After**:
```python
class SendMessageResponse(TypedDict):
    message: Message  # AI response only
    usage: dict       # Token usage statistics
    model: str        # Model used
```

#### 2. Updated Streaming Response Type

**File**: `chatroutes/types/conversation.py`

**Before**:
```python
class StreamChunk(TypedDict):
    id: str
    model: str
    choices: List[StreamChunkChoice]
```

**After**:
```python
class StreamChunk(TypedDict, total=False):
    type: str              # 'content' or 'complete'
    content: Optional[str] # Content chunk
    model: Optional[str]   # Model name
    message: Optional[dict] # Complete message (when type='complete')
```

#### 3. Updated HTTP Client Streaming

**File**: `chatroutes/http_client.py`

Now properly handles the ChatRoutes streaming format and returns the complete message when streaming finishes.

#### 4. Updated Examples

**Files Updated**:
- `examples/basic_usage.py`
- `examples/streaming_example.py`
- `README.md`
- `QUICKSTART.md`

**Send Message - Before**:
```python
print(response['assistantMessage']['content'])
```

**Send Message - After**:
```python
print(response['message']['content'])
print(f"Tokens used: {response['usage']['totalTokens']}")
```

**Streaming - Before**:
```python
def on_chunk(chunk):
    if chunk['choices'][0]['delta'].get('content'):
        print(chunk['choices'][0]['delta']['content'], end='')
```

**Streaming - After**:
```python
def on_chunk(chunk):
    if chunk.get('type') == 'content' and chunk.get('content'):
        print(chunk['content'], end='', flush=True)
```

#### 3. Updated Supported Models

Added all supported models and clarified that exact names must be used:

- `gpt-5` (default)
- `claude-opus-4-1`
- `claude-opus-4`
- `claude-sonnet-4`

**Important**: Using other model names like `gpt-4o` or `gpt-4o-mini` will result in errors.

## Correct Usage

### 1. Send Message (Non-Streaming)

```python
from chatroutes import ChatRoutes

client = ChatRoutes(api_key="your-api-key")

conversation = client.conversations.create({
    'title': 'My Chat',
    'model': 'gpt-5'
})

response = client.messages.send(conversation['id'], {
    'content': 'Hello!',
    'role': 'user'
})

# Access the response
print(response['message']['content'])  # AI response text
print(response['message']['role'])     # 'assistant'
print(response['usage']['totalTokens']) # Token count
print(response['model'])                # 'gpt-5-2025-08-07'
```

### 2. Streaming Messages

```python
def on_chunk(chunk):
    # Handle content chunks
    if chunk.get('type') == 'content':
        print(chunk.get('content', ''), end='', flush=True)

    # Handle completion
    elif chunk.get('type') == 'complete':
        print(f"\n\nMessage saved with ID: {chunk['message']['id']}")

def on_complete(message):
    # Called when streaming finishes
    print(f"Total tokens: {message.get('tokenCount', 'N/A')}")

client.messages.stream(
    conversation['id'],
    {
        'content': 'Tell me a joke',
        'model': 'gpt-5'
    },
    on_chunk=on_chunk,
    on_complete=on_complete
)
```

### 3. Response Structures

**Non-Streaming Response**:
```python
{
    'message': {
        'id': 'msg_...',
        'role': 'assistant',
        'content': 'AI response text here',
        'tokens': 18,
        'createdAt': '2025-10-05T03:01:09.598Z',
        'metadata': {
            'model': 'gpt-5-2025-08-07',
            'temperature': 0.7,
            'maxTokens': 2048,
            'responseTime': 1542,
            'finishReason': 'stop',
            'cost': 0
        }
    },
    'usage': {
        'promptTokens': 8,
        'completionTokens': 18,
        'totalTokens': 26
    },
    'model': 'gpt-5-2025-08-07'
}
```

**Streaming Chunks**:
```python
# Content chunk
{
    'type': 'content',
    'content': 'Hello',
    'model': 'gpt-5-2025-08-07'
}

# Completion chunk
{
    'type': 'complete',
    'message': {
        'id': 'msg_...',
        'role': 'assistant',
        'content': 'Full response here',
        'tokenCount': 42,
        'createdAt': '2025-10-05T...'
    },
    'usage': {
        'promptTokens': 10,
        'completionTokens': 42,
        'totalTokens': 52
    },
    'model': 'gpt-5-2025-08-07'
}
```

## Migration Guide

If you're using an older version of the SDK:

### Change 1: Update non-streaming response access

```python
# OLD (will cause KeyError)
user_msg = response['userMessage']['content']
ai_msg = response['assistantMessage']['content']

# NEW
ai_msg = response['message']['content']
tokens = response['usage']['totalTokens']
```

### Change 2: Update streaming callback

```python
# OLD (will cause KeyError)
def on_chunk(chunk):
    if chunk['choices'][0]['delta'].get('content'):
        print(chunk['choices'][0]['delta']['content'], end='')

# NEW
def on_chunk(chunk):
    if chunk.get('type') == 'content' and chunk.get('content'):
        print(chunk['content'], end='', flush=True)
```

### Change 3: Update model names

```python
# OLD (will cause "Unsupported model" error)
conversation = client.conversations.create({
    'title': 'Chat',
    'model': 'gpt-4o'  # Not supported
})

# NEW
conversation = client.conversations.create({
    'title': 'Chat',
    'model': 'gpt-5'  # Correct
})
```

## Files Changed

- `chatroutes/types/conversation.py` - Updated SendMessageResponse and StreamChunk types
- `chatroutes/http_client.py` - Fixed streaming to handle ChatRoutes format
- `chatroutes/resources/messages.py` - Simplified stream() method
- `examples/basic_usage.py` - Updated response access
- `examples/streaming_example.py` - Updated streaming callbacks
- `README.md` - Updated all examples
- `QUICKSTART.md` - Updated all examples
- `SDK_UPDATE_2025-10-05.md` (this file)

## Version

This update will be included in version `0.1.1` (or next release).

Current version: `0.1.0`

---

**Date**: October 5, 2025
**Status**: ✅ Complete
