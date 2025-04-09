
import uuid
import logging
from abc import ABC, abstractmethod
from datetime import datetime

class Agent(ABC):
    def __init__(self, name: str, role: str, capabilities: list = None):
        self.agent_id = str(uuid.uuid4())
        self.name = name
        self.role = role
        self.capabilities = capabilities if capabilities else []
        self.creation_time = datetime.utcnow()
        self.memory = []
        self.status = "idle"
        self.logger = logging.getLogger(f"Agent-{self.name}")
        self.logger.info(f"[{self.creation_time}] Agent {self.name} initialized.")

    @abstractmethod
    def perform_task(self, task: dict) -> dict:
        """
        Perform a task based on the agent's capabilities and return results.
        """
        pass

    def communicate(self, message: str, target_agent: 'Agent'):
        """
        Send a message to another agent.
        """
        self.logger.info(f"{self.name} -> {target_agent.name}: {message}")
        target_agent.receive_message(message, self)

    def receive_message(self, message: str, sender: 'Agent'):
        """
        Process a received message.
        """
        self.logger.info(f"{self.name} received message from {sender.name}: {message}")
        self.memory.append({"from": sender.name, "message": message})

    def update_status(self, new_status: str):
        """
        Update the agent's internal status.
        """
        self.logger.info(f"{self.name} status changed from {self.status} to {new_status}")
        self.status = new_status

    def log_event(self, event: str):
        """
        Log any event in the agent's lifetime.
        """
        timestamp = datetime.utcnow()
        self.logger.info(f"[{timestamp}] {self.name}: {event}")
        self.memory.append({"timestamp": timestamp, "event": event})
