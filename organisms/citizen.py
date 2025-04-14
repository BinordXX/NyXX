import uuid
import logging
from datetime import datetime
import random


class Citizen:
    """
    A Citizen is a digital organism that starts its life in the environment, learns, and evolves into an agent when ready.
    This class defines how a citizen is born, learns from data sources, and prepares to take on roles in the future.
    """

    def __init__(self, name: str, learning_data: list = None):
        """
        Initialize a new citizen. 
        Citizens start with a basic understanding and are learning organisms.
        """
        self.citizen_id = str(uuid.uuid4())
        self.name = name
        self.creation_time = datetime.utcnow()
        self.memory = []  # Memory bank to store experiences
        self.learning_data = learning_data if learning_data else []  # Data the citizen will learn from
        self.knowledge = {}  # Holds knowledge accumulated by the citizen
        self.status = "idle"  # Citizen starts in an idle state
        self.age = 0  # Initial age (could be calculated or updated over time)
        self.metadata = {}  # Metadata to store additional info like role and timestamps
        self.logger = logging.getLogger(f"Citizen-{self.name}")
        self.logger.info(f"[{self.creation_time}] Citizen {self.name} initialized.")
        self.learning_enabled = True  # Flag to control if the citizen is still learning
        
    def setup_logger(self):
        # Logger setup (if you need it)
        import logging
        logger = logging.getLogger(self.name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    def learn(self, environment):
        """
        Simulate the learning process by processing available data sources from the environment.
        The citizen will "learn" by processing and storing knowledge from its environment.
        """
        if not self.learning_enabled:
            self.logger.info(f"Citizen {self.name} has reached the learning threshold and can no longer learn.")
            return

        # Simulate learning from the environment
        
        data = environment.get_random_fact()  # Get a random fact from the environment
        self.memory.append(data)
        self.knowledge[data] = self.knowledge.get(data, 0) + 1  # Increase knowledge of that fact
        self.logger.info(f"Citizen {self.name} learned: {data}. Knowledge: {self.knowledge[data]}")

        # Check if the citizen has learned enough to evolve
        if sum(self.knowledge.values()) >= 3:  # Threshold for evolution (can be adjusted)
            self.status = "ready to evolve"
            self.learning_enabled = False  # Stop learning once threshold is reached
            self.logger.info(f"Citizen {self.name} has gained enough knowledge to evolve and will stop learning.")

    def act(self):
        """
        Once a citizen has evolved enough, they can take action.
        For now, this function could be a placeholder for when the citizen is ready to become an agent.
        """
        if self.status == "ready to evolve":
            self.logger.info(f"Citizen {self.name} is now taking action as an agent.")
            # In the future, this is where the agent's role (e.g., Trader, Researcher) would begin.
            self.status = "evolved"
        else:
            self.logger.info(f"Citizen {self.name} is still idle, waiting to evolve.")

    def update_status(self, new_status: str):
        """
        Change the citizen's current state.
        """
        self.status = new_status
        self.metadata["last_updated"] = datetime.utcnow().isoformat()

    def get_summary(self) -> dict:
        """
        Return a summary of the citizen's attributes.
        """
        return {
            "id": self.citizen_id,
            "name": self.name,
            "age": self.age,
            "role": self.role if hasattr(self, 'role') else None,  # Avoid error if no role assigned yet
            "status": self.status,
            "metadata": self.metadata
        }
    def evolve_and_assign_role(self):
        """
        Check if a citizen has gained enough knowledge to evolve. If so, assign a role and log the evolution.
        """
        if sum(self.knowledge.values()) >= 3:  # Threshold for evolution
            self.status = "evolved"
            self.logger.info(f"Citizen {self.name} has gained enough knowledge to evolve.")
            
            # Assign a random role to the citizen once they evolve
            roles = ['Trader', 'Researcher', 'Farmer', 'Medic', 'Engineer']

            if not roles:
                self.logger.error("No roles available to assign!")
                return

            # Randomly choose a role
            self.role = random.choice(roles)

            # Log the assigned role
            self.logger.info(f"Citizen {self.name} has evolved into a {self.role}.")
        else:
            self.logger.info(f"Citizen {self.name} has not gained enough knowledge to evolve.")

 
        
    def __repr__(self):
        return f"<Citizen name={self.name}, role={self.role if hasattr(self, 'role') else 'None'}, status={self.status}>"
