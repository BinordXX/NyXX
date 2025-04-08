# digital_civilization/agents/behavior/communication.py

import json
from datetime import datetime
from typing import Any, Dict, List

class Message:
    """
    Encapsulates a communication packet between agents.
    """
    def __init__(self, sender_id: str, receiver_id: str, msg_type: str, content: Dict[str, Any]):
        self.timestamp = datetime.utcnow().isoformat()
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.msg_type = msg_type  # e.g., 'request', 'response', 'broadcast', 'negotiate'
        self.content = content

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "sender": self.sender_id,
            "receiver": self.receiver_id,
            "type": self.msg_type,
            "content": self.content
        }

    def serialize(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def deserialize(message_str: str) -> 'Message':
        data = json.loads(message_str)
        return Message(
            sender_id=data["sender"],
            receiver_id=data["receiver"],
            msg_type=data["type"],
            content=data["content"]
        )


class CommunicationModule:
    """
    Handles the sending and receiving of messages between agents.
    Agents can use this module to broadcast, request data, or negotiate tasks.
    """

    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.inbox: List[Message] = []
        self.outbox: List[Message] = []

    def send(self, receiver_id: str, msg_type: str, content: Dict[str, Any]):
        msg = Message(self.agent_id, receiver_id, msg_type, content)
        self.outbox.append(msg)
        print(f"[{self.agent_id}] Queued message to {receiver_id}: {msg_type}")

    def receive(self, message: Message):
        self.inbox.append(message)
        print(f"[{self.agent_id}] Received message from {message.sender_id}: {message.msg_type}")

    def process_inbox(self):
        responses = []
        while self.inbox:
            message = self.inbox.pop(0)
            response = self._handle_message(message)
            if response:
                responses.append(response)
        return responses

    def _handle_message(self, message: Message) -> Any:
        print(f"[{self.agent_id}] Processing message: {message.msg_type}")
        if message.msg_type == "request":
            return self._handle_request(message.content)
        elif message.msg_type == "negotiate":
            return self._handle_negotiation(message.content)
        elif message.msg_type == "broadcast":
            return self._handle_broadcast(message.content)
        # Add more handlers as needed
        return None

    def _handle_request(self, content: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "acknowledged", "data": "request processed"}

    def _handle_negotiation(self, content: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "negotiated", "details": content}

    def _handle_broadcast(self, content: Dict[str, Any]) -> None:
        print(f"[{self.agent_id}] Received broadcast: {content}")
