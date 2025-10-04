# Changelog

All notable changes to the ChatRoutes Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2025-10-04

### Added
- Initial release of ChatRoutes Python SDK
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

[Unreleased]: https://github.com/chatroutes/chatroutes-python-sdk/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/chatroutes/chatroutes-python-sdk/releases/tag/v1.0.0
