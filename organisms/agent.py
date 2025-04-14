# NyXX/organisms/agent.py

from organisms.citizen import Citizen
from abc import ABC, abstractmethod
from datetime import datetime
import logging
import uuid


class Agent(Citizen, ABC):
    """
    An Agent is an evolved Citizen that has acquired sufficient foundational knowledge
    to assume a specific role and perform specialized tasks.
    """

    def __init__(self, citizen: Citizen, role: str, capabilities: list = None):
        super().__init__(
            name=citizen.name,
            age=citizen.age,
            metadata=citizen.metadata
        )
        self.agent_id = str(uuid.uuid4())
        self.role = role
        self.capabilities = capabilities if capabilities else []
        self.knowledge_base = citizen.knowledge_base  # inherits what it learned as a citizen
        self.status = "active"
        self.creation_time = datetime.utcnow()
        self.logger = logging.getLogger(f"Agent-{self.name}")
        self.logger.info(f"[{self.creation_time}] Agent {self.name} (Role: {self.role}) initialized.")

    @abstractmethod
    def perform_task(self, task: dict) -> dict:
        """
        Perform a task based on the agent's capabilities and return results.
        """
        pass

    def update_capabilities(self, new_capability: str):
        """
        Add a new capability to the agent's list.
        """
        if new_capability not in self.capabilities:
            self.capabilities.append(new_capability)
            self.logger.info(f"{self.name} learned a new capability: {new_capability}")

    def receive_new_data(self, data):
        """
        Handle domain-specific data as part of specialized learning (e.g. trading, researching).
        """
        self.knowledge_base.append(data)
        self.logger.info(f"{self.name} received new domain data for role {self.role}.")

    def communicate(self, message: str, target_agent: 'Agent'):
        """
        Send a message to another agent.
        """
        self.logger.info(f"{self.name} -> {target_agent.name}: {message}")
        target_agent.receive_message(message, self)

    def receive_message(self, message: str, sender: 'Agent'):
        """
        Receive and process a message from another agent.
        """
        self.logger.info(f"{self.name} received message from {sender.name}: {message}")
        self.memory.append({
            "timestamp": datetime.utcnow().isoformat(),
            "from": sender.name,
            "message": message
        })

    def update_status(self, new_status: str):
        """
        Update the agent’s internal operational status.
        """
        self.logger.info(f"{self.name} status changed from {self.status} to {new_status}")
        self.status = new_status
        self.metadata["last_updated"] = datetime.utcnow().isoformat()

    def log_event(self, event: str):
        """
        Log any meaningful event in the agent’s lifetime.
        """
        timestamp = datetime.utcnow()
        self.logger.info(f"[{timestamp}] {self.name}: {event}")
        self.memory.append({
            "timestamp": timestamp.isoformat(),
            "event": event
        })
