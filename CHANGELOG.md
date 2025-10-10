# Changelog

All notable changes to the ChatRoutes Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2025-10-10

### Added
- Checkpoint API support for managing conversation context
- New `CheckpointsResource` with methods:
  - `list(conversation_id, branch_id=None)` - List checkpoints
  - `create(conversation_id, branch_id, anchor_message_id)` - Create manual checkpoint
  - `delete(checkpoint_id)` - Delete checkpoint
  - `recreate(checkpoint_id)` - Recreate checkpoint
- Enhanced message metadata with checkpoint-related fields:
  - `context_truncated` - Indicates if context was truncated
  - `checkpoint_used` - Indicates if a checkpoint was used
  - `prompt_tokens` - Token count for the prompt
  - `context_message_count` - Number of messages in context
- New types for checkpoint support:
  - `Checkpoint` - Checkpoint object type
  - `CheckpointCreateRequest` - Request type for creating checkpoints
  - `CheckpointListResponse` - Response type for listing checkpoints
- Example code demonstrating checkpoint usage in `examples/checkpoint_example.py`

### Changed
- Updated `MessageMetadata` TypedDict to include new optional checkpoint fields
- Updated client initialization to include `checkpoints` resource

## [0.1.0] - 2025-10-04

### Added
- Initial beta release of ChatRoutes Python SDK
- ⚠️ **Beta Notice**: API may change without backward compatibility
- Full API support for conversations, messages, and branches
- Streaming response support with Server-Sent Events (SSE)
- Automatic retry logic with exponential backoff
- Type-safe implementation using TypedDict
- Comprehensive error handling with specific exception types
- Complete documentation and usage examples

### Features
- **Conversations**: Create, list, get, update, delete, and get tree structure
- **Messages**: Send, stream, list, update, and delete messages
- **Branches**: Create, fork, list, update, delete, get messages, and merge branches
- **HTTP Client**: Robust HTTP client with retry mechanism and streaming support
- **Type Safety**: Full type hints for all API responses and requests
- **Examples**: Basic usage, streaming, branching, and error handling examples

### Supported Python Versions
- Python 3.8+
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

### Dependencies
- requests >= 2.31.0
- typing-extensions >= 4.0.0

[Unreleased]: https://github.com/chatroutes/chatroutes-python-sdk/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/chatroutes/chatroutes-python-sdk/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/chatroutes/chatroutes-python-sdk/releases/tag/v0.1.0
