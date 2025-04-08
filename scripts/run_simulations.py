# NyXX/scripts/run_simulation.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from NyXX.agents.agent_types.trader import Trader


import time
from NyXX.agents.agent_types.trader import Trader
from NyXX.agents.agent_types.researcher import Researcher
from NyXX.agents.agent_types.analyst import Analyst
from NyXX.agents.agent_types.optimizer import Optimizer
from NyXX.environment.environment import Environment
from NyXX.encephalon.encephalon import CoreMind
from NyXX.utils.logging import log_info, log_error


class SimulationEngine:
    """
    SimulationEngine handles the overall execution of the NyXX digital civilization simulation.
    It orchestrates the environment, agents, and their interactions.
    """

    def __init__(self):
        self.environment = Environment()  # Create an instance of the environment
        self.coremind = CoreMind()  # Initialize the centralized intelligence (CoreMind/Encephalon)
        self.agents = []  # List to store all agents in the simulation

    def initialize_agents(self, num_agents: int):
        """
        Initialize agents based on the number of agents.
        :param num_agents: Number of agents to create and initialize.
        :return: None
        """
        for i in range(num_agents):
            agent_type = 'trader' if i % 4 == 0 else 'researcher' if i % 4 == 1 else 'analyst' if i % 4 == 2 else 'optimizer'
            agent = self.create_agent(agent_type, i)
            self.agents.append(agent)
            self.environment.add_agent(agent)  # Add agent to the environment
            log_info(f"Initialized {agent_type} agent with ID {i}.")

    def create_agent(self, agent_type: str, agent_id: int):
        """
        Create a new agent of a specific type.
        :param agent_type: Type of the agent (e.g., 'trader', 'researcher', etc.).
        :param agent_id: Unique identifier for the agent.
        :return: The created agent.
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

    def start_simulation(self, num_agents: int, simulation_steps: int = 100):
        """
        Start the simulation for a given number of steps.
        :param num_agents: Number of agents to create and initialize.
        :param simulation_steps: Number of steps to run the simulation.
        :return: None
        """
        log_info(f"Starting simulation with {num_agents} agents.")
        self.initialize_agents(num_agents)
        
        for step in range(simulation_steps):
            log_info(f"Simulation Step {step + 1} of {simulation_steps}")
            
            # Step 1: CoreMind evaluates the environment and sets a high-level strategy
            self.coremind.evaluate_environment(self.environment)
            self.coremind.formulate_strategy()
            
            # Step 2: Agents execute their actions based on strategy and environment conditions
            for agent in self.agents:
                agent.execute_task(self.environment)
            
            # Step 3: Evaluate the agents' performance and adjust if necessary
            for agent in self.agents:
                agent.evaluate_performance()
            
            # Step 4: Wait for next simulation step (for real-time pacing)
            time.sleep(1)  # Adjust timing for your needs

            # Step 5: Log the current state of the environment and agents
            self.log_simulation_state(step)

    def log_simulation_state(self, step: int):
        """
        Log the current state of the simulation, including agents' performance and environment changes.
        :param step: The current simulation step.
        :return: None
        """
        log_info(f"Logging state at simulation step {step + 1}")
        for agent in self.agents:
            log_info(f"Agent {agent.agent_id} - Type: {agent.__class__.__name__} - Resources: {agent.resources} - Reputation: {agent.reputation}")
        # You can log environment states like market, economy, etc., here too

    def stop_simulation(self):
        """
        Stop the simulation, possibly saving results and cleaning up resources.
        :return: None
        """
        log_info("Stopping simulation.")
        # Here, you can add logic for saving logs, analyzing results, or cleaning up resources.


# Main script execution

if __name__ == "__main__":
    simulation_engine = SimulationEngine()

    # Run simulation with 10 agents and 100 simulation steps
    simulation_engine.start_simulation(num_agents=10, simulation_steps=100)

    # Stop the simulation (optionally after completion)
    simulation_engine.stop_simulation()
