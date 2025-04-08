# NyXX/scripts/train_agents.py

import time
from NyXX.agents.agent_types.trader import Trader
from NyXX.agents.agent_types.researcher import Researcher
from NyXX.agents.agent_types.analyst import Analyst
from NyXX.agents.agent_types.optimizer import Optimizer
from NyXX.environment.environment import Environment
from NyXX.encephalon.encephalon import CoreMind
from NyXX.utils.logging import log_info, log_error

class AgentTrainer:
    """
    The AgentTrainer class is responsible for training the agents through interaction with the environment
    and utilizing feedback mechanisms to improve agent behavior.
    """

    def __init__(self, num_agents: int, training_steps: int = 100):
        self.environment = Environment()  # Set up the environment
        self.coremind = CoreMind()  # Central intelligence for the system
        self.num_agents = num_agents
        self.training_steps = training_steps
        self.agents = []

    def initialize_agents(self):
        """
        Initialize the agents in the simulation.
        """
        for i in range(self.num_agents):
            agent_type = 'trader' if i % 4 == 0 else 'researcher' if i % 4 == 1 else 'analyst' if i % 4 == 2 else 'optimizer'
            agent = self.create_agent(agent_type, i)
            self.agents.append(agent)
            self.environment.add_agent(agent)  # Add agent to the environment
            log_info(f"Initialized {agent_type} agent with ID {i}.")

    def create_agent(self, agent_type: str, agent_id: int):
        """
        Create a new agent based on the specified type.
        """
        if agent_type == 'trader':
            return Trader(agent_id)
        elif agent_type == 'researcher':
            return Researcher(agent_id)
        elif agent_type == 'analyst':
            return Analyst(agent_id)
        elif agent_type == 'optimizer':
            return Optimizer(agent_id)
        else:
            log_error(f"Unrecognized agent type: {agent_type}.")
            return None

    def train_agents(self):
        """
        Train the agents by running them through a series of interactions with the environment.
        During each interaction, agents will learn and adapt based on rewards/penalties.
        """
        log_info(f"Training {self.num_agents} agents for {self.training_steps} steps.")
        
        # Step 1: Initialize the agents in the environment
        self.initialize_agents()

        # Step 2: Training loop
        for step in range(self.training_steps):
            log_info(f"Training step {step + 1}/{self.training_steps}")
            
            # Step 2.1: CoreMind evaluates the environment and formulates strategy
            self.coremind.evaluate_environment(self.environment)
            self.coremind.formulate_strategy()

            # Step 2.2: Agents execute their tasks based on CoreMind's strategy
            for agent in self.agents:
                agent.execute_task(self.environment)

            # Step 2.3: Evaluate agent performance and provide rewards/penalties
            for agent in self.agents:
                agent.evaluate_performance()

            # Step 2.4: Apply learning from the environment feedback (e.g., reinforcement learning)
            for agent in self.agents:
                agent.learn_from_feedback()

            # Step 2.5: Log progress and performance
            self.log_training_progress(step)

            # Optional: Adjust training pace or simulation time
            time.sleep(0.5)

    def log_training_progress(self, step: int):
        """
        Log the progress of the training, including agent actions and performance.
        :param step: Current training step.
        """
        log_info(f"Logging progress at training step {step + 1}.")
        for agent in self.agents:
            log_info(f"Agent {agent.agent_id} - Type: {agent.__class__.__name__} - Resources: {agent.resources} - Reputation: {agent.reputation}")

    def save_trained_agents(self):
        """
        Save the trained agents' models for future use.
        """
        log_info("Saving trained agent models.")
        for agent in self.agents:
            agent.save_model()  # Assuming agents have a save_model method to save their trained state.

    def stop_training(self):
        """
        Stop the training session and clean up.
        """
        log_info("Training session completed. Stopping.")
        # Optionally, you could save logs or perform analysis of the training session results.
        self.save_trained_agents()


# Main script execution
if __name__ == "__main__":
    # Define number of agents and training steps
    num_agents = 10
    training_steps = 100
    
    # Initialize the trainer and start training
    trainer = AgentTrainer(num_agents, training_steps)
    trainer.train_agents()

    # Stop training and clean up
    trainer.stop_training()
