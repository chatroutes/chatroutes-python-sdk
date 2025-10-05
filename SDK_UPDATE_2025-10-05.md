# Python SDK Update - October 5, 2025

## Response Format Fix

### Issue
The SDK was expecting `userMessage` and `assistantMessage` in the response, but the actual API returns only the assistant's message in a `message` field.

### Changes Made

#### 1. Updated Type Definition

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

#### 2. Updated Examples

**Files Updated**:
- `examples/basic_usage.py`
- `examples/streaming_example.py`
- `README.md`
- `QUICKSTART.md`

**Before**:
```python
print(response['assistantMessage']['content'])
```

**After**:
```python
print(response['message']['content'])
print(f"Tokens used: {response['usage']['totalTokens']}")
```

#### 3. Updated Supported Models

Added all supported models and clarified that exact names must be used:

- `gpt-5` (default)
- `claude-opus-4-1`
- `claude-opus-4`
- `claude-sonnet-4`

**Important**: Using other model names like `gpt-4o` or `gpt-4o-mini` will result in errors.

## Correct Usage

### Send Message

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

### Response Structure

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

## Migration Guide

If you're using an older version of the SDK:

### Change 1: Update response access

```python
# OLD (will cause KeyError)
user_msg = response['userMessage']['content']
ai_msg = response['assistantMessage']['content']

# NEW
ai_msg = response['message']['content']
tokens = response['usage']['totalTokens']
```

### Change 2: Update model names

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

- `chatroutes/types/conversation.py`
- `examples/basic_usage.py`
- `examples/streaming_example.py`
- `README.md`
- `QUICKSTART.md`
- `SDK_UPDATE_2025-10-05.md` (this file)

## Version

This update will be included in version `0.1.1` (or next release).

Current version: `0.1.0`

---

**Date**: October 5, 2025
**Status**: ✅ Complete
