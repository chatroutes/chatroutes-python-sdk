from typing import TYPE_CHECKING, List, Optional, Callable
from ..types import (
    Message,
    SendMessageRequest,
    SendMessageResponse,
    StreamChunk
)

if TYPE_CHECKING:
    from ..client import ChatRoutes


class MessagesResource:
    def __init__(self, client: 'ChatRoutes'):
        self._client = client

    def send(self, conversation_id: str, data: SendMessageRequest) -> SendMessageResponse:
        response = self._client._http.post(f'/conversations/{conversation_id}/messages', data)

        if not response.get('success') or 'data' not in response:
            raise Exception(response.get('message', 'Failed to send message'))

        return response['data']

    def stream(
        self,
        conversation_id: str,
        data: SendMessageRequest,
        on_chunk: Callable[[StreamChunk], None],
        on_complete: Optional[Callable[[SendMessageResponse], None]] = None
    ) -> None:
        full_content = ''
        user_message_id = ''
        assistant_message_id = ''
        model = ''
        finish_reason = None

        def handle_chunk(chunk: StreamChunk):
            nonlocal full_content, user_message_id, assistant_message_id, model, finish_reason

            if chunk.get('choices') and len(chunk['choices']) > 0:
                choice = chunk['choices'][0]
                delta = choice.get('delta', {})

                if delta.get('content'):
                    full_content += delta['content']

                if choice.get('finish_reason'):
                    finish_reason = choice['finish_reason']

            if chunk.get('model'):
                model = chunk['model']

            on_chunk(chunk)

            if finish_reason and on_complete:
                import datetime
                complete_response: SendMessageResponse = {
                    'userMessage': {
                        'id': user_message_id or f"msg_{int(datetime.datetime.now().timestamp())}_user",
                        'conversationId': conversation_id,
                        'role': 'user',
                        'content': data['content'],
                        'createdAt': datetime.datetime.now().isoformat()
                    },
                    'assistantMessage': {
                        'id': assistant_message_id or f"msg_{int(datetime.datetime.now().timestamp())}_assistant",
                        'conversationId': conversation_id,
                        'role': 'assistant',
                        'content': full_content,
                        'createdAt': datetime.datetime.now().isoformat(),
                        'metadata': {
                            'model': model,
                            'finishReason': finish_reason
                        }
                    }
                }
                on_complete(complete_response)

        self._client._http.stream(
            f'/conversations/{conversation_id}/messages/stream',
            data,
            handle_chunk
        )

    def list(self, conversation_id: str, branch_id: Optional[str] = None) -> List[Message]:
        params = {}
        if branch_id:
            params['branchId'] = branch_id

        response = self._client._http.get(f'/conversations/{conversation_id}/messages', params=params)

        if not response.get('success') or 'data' not in response:
            raise Exception(response.get('message', 'Failed to list messages'))

        return response['data']['messages']

    def update(self, message_id: str, content: str) -> Message:
        response = self._client._http.patch(f'/messages/{message_id}', {'content': content})

        if not response.get('success') or 'data' not in response:
            raise Exception(response.get('message', 'Failed to update message'))

        return response['data']['message']

    def delete(self, message_id: str) -> None:
        response = self._client._http.delete(f'/messages/{message_id}')

        if not response.get('success'):
            raise Exception(response.get('message', 'Failed to delete message'))
