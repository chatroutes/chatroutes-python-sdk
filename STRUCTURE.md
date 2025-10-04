# ChatRoutes Python SDK - Project Structure

```
chatroutes-python-sdk/
│
├── chatroutes/                          # Main package directory
│   ├── __init__.py                     # Package initialization & exports
│   ├── client.py                       # Main ChatRoutes client class
│   ├── exceptions.py                   # Custom exception classes
│   ├── http_client.py                  # HTTP client with retry logic
│   │
│   ├── resources/                      # API resource modules
│   │   ├── __init__.py
│   │   ├── conversations.py            # Conversations resource
│   │   ├── messages.py                 # Messages resource
│   │   └── branches.py                 # Branches resource
│   │
│   └── types/                          # Type definitions
│       ├── __init__.py
│       └── conversation.py             # TypedDict classes
│
├── examples/                            # Usage examples
│   ├── basic_usage.py                  # Basic CRUD operations
│   ├── streaming_example.py            # Streaming responses
│   ├── branching_example.py            # Working with branches
│   └── error_handling.py               # Error handling patterns
│
├── setup.py                            # Package setup configuration
├── pyproject.toml                      # Modern Python packaging config
├── requirements.txt                    # Production dependencies
├── requirements-dev.txt                # Development dependencies
├── README.md                           # Main documentation
├── QUICKSTART.md                       # Quick start guide
├── STRUCTURE.md                        # This file
└── .gitignore                          # Git ignore patterns
```

## Module Overview

### Core Modules

#### `chatroutes/client.py`
- **ChatRoutes**: Main client class
- Constructor accepts: api_key, base_url, timeout, retry_attempts, retry_delay
- Properties: conversations, messages, branches resources

#### `chatroutes/http_client.py`
- **HttpClient**: HTTP request handler
- Features: retry logic, error handling, streaming support
- Methods: get(), post(), patch(), delete(), stream()

#### `chatroutes/exceptions.py`
Exception hierarchy:
- **ChatRoutesError**: Base exception
- **AuthenticationError**: 401 errors
- **RateLimitError**: 429 errors with retry_after
- **ValidationError**: 400 errors
- **NotFoundError**: 404 errors
- **ServerError**: 5xx errors
- **NetworkError**: Network failures

### Resource Modules

#### `chatroutes/resources/conversations.py`
- **ConversationsResource**
  - `create(data)`: Create new conversation
  - `list(params)`: List conversations with pagination
  - `get(conversation_id)`: Get single conversation
  - `update(conversation_id, data)`: Update conversation
  - `delete(conversation_id)`: Delete conversation
  - `get_tree(conversation_id)`: Get conversation tree structure

#### `chatroutes/resources/messages.py`
- **MessagesResource**
  - `send(conversation_id, data)`: Send message and get response
  - `stream(conversation_id, data, on_chunk, on_complete)`: Stream responses
  - `list(conversation_id, branch_id)`: List messages
  - `update(message_id, content)`: Update message
  - `delete(message_id)`: Delete message

#### `chatroutes/resources/branches.py`
- **BranchesResource**
  - `list(conversation_id)`: List all branches
  - `create(conversation_id, data)`: Create new branch
  - `fork(conversation_id, data)`: Fork from message
  - `update(conversation_id, branch_id, data)`: Update branch
  - `delete(conversation_id, branch_id)`: Delete branch
  - `get_messages(conversation_id, branch_id)`: Get branch messages
  - `merge(conversation_id, branch_id)`: Merge branch

### Type Definitions

#### `chatroutes/types/conversation.py`
TypedDict classes:
- **Conversation**: Conversation object
- **Message**: Message object with metadata
- **Branch**: Branch object
- **CreateConversationRequest**: Conversation creation params
- **SendMessageRequest**: Message sending params
- **SendMessageResponse**: Message response structure
- **CreateBranchRequest**: Branch creation params
- **ForkConversationRequest**: Fork params
- **ConversationTree**: Tree structure
- **TreeNode**: Tree node structure
- **ListConversationsParams**: List pagination params
- **PaginatedResponse**: Paginated response structure
- **StreamChunk**: Streaming chunk structure

## Key Features

### 1. Type Safety
- Full type hints using TypedDict
- Proper typing for all function parameters and returns
- IDE autocomplete support

### 2. Error Handling
- Comprehensive exception hierarchy
- Status code to exception mapping
- Detailed error information with details field

### 3. Retry Logic
- Exponential backoff for failed requests
- Configurable retry attempts and delay
- Automatic retry on 5xx errors

### 4. Streaming Support
- Server-Sent Events (SSE) handling
- Chunk-by-chunk processing
- Completion callbacks

### 5. Resource Organization
- Clean separation of concerns
- Each resource in its own module
- Consistent API patterns

## Installation & Usage

### Install from source:
```bash
pip install -e .
```

### Basic usage:
```python
from chatroutes import ChatRoutes

client = ChatRoutes(api_key="your-api-key")
conversation = client.conversations.create({'title': 'Test'})
```

### With error handling:
```python
from chatroutes import ChatRoutes, NotFoundError

try:
    conv = client.conversations.get('conv_123')
except NotFoundError:
    print("Conversation not found")
```

## API Endpoint Mapping

| SDK Method | HTTP Endpoint |
|------------|---------------|
| `conversations.create()` | `POST /api/v1/conversations` |
| `conversations.list()` | `GET /api/v1/conversations` |
| `conversations.get()` | `GET /api/v1/conversations/{id}` |
| `conversations.update()` | `PATCH /api/v1/conversations/{id}` |
| `conversations.delete()` | `DELETE /api/v1/conversations/{id}` |
| `conversations.get_tree()` | `GET /api/v1/conversations/{id}/tree` |
| `messages.send()` | `POST /api/v1/conversations/{id}/messages` |
| `messages.stream()` | `POST /api/v1/conversations/{id}/messages/stream` |
| `messages.list()` | `GET /api/v1/conversations/{id}/messages` |
| `messages.update()` | `PATCH /api/v1/messages/{id}` |
| `messages.delete()` | `DELETE /api/v1/messages/{id}` |
| `branches.list()` | `GET /api/v1/conversations/{id}/branches` |
| `branches.create()` | `POST /api/v1/conversations/{id}/branches` |
| `branches.fork()` | `POST /api/v1/conversations/{id}/fork` |
| `branches.update()` | `PATCH /api/v1/conversations/{id}/branches/{branch_id}` |
| `branches.delete()` | `DELETE /api/v1/conversations/{id}/branches/{branch_id}` |
| `branches.get_messages()` | `GET /api/v1/conversations/{id}/branches/{branch_id}/messages` |
| `branches.merge()` | `POST /api/v1/conversations/{id}/branches/{branch_id}/merge` |

## Development

### Install dev dependencies:
```bash
pip install -e ".[dev]"
```

### Run type checking:
```bash
mypy chatroutes
```

### Format code:
```bash
black chatroutes
```

### Run tests:
```bash
pytest
```
