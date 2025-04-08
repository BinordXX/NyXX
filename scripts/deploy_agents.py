# NyXX/scripts/deploy_agents.py

import random
from NyXX.agents.agent_types.trader import Trader
from NyXX.agents.agent_types.researcher import Researcher
from NyXX.agents.agent_types.analyst import Analyst
from NyXX.agents.agent_types.optimizer import Optimizer
from NyXX.environment.environment import Environment
from NyXX.utils.logging import log_info, log_error
from NyXX.config.system_config import load_config


class AgentDeploymentSystem:
    """
    AgentDeploymentSystem handles the initialization and deployment of agents into the NyXX ecosystem.
    This includes configuring agents, assigning them to the environment, and starting their tasks.
    """

    def __init__(self):
        # Load system configuration
        self.config = load_config('system_config.json')
        self.environment = Environment()  # Create an instance of the environment
        self.deployed_agents = []

    def create_agent(self, agent_type: str, agent_id: int):
        """
        Create a new agent based on the specified agent type.
        :param agent_type: Type of agent to create (e.g., 'trader', 'researcher').
        :param agent_id: Unique identifier for the agent.
        :return: The created agent.
        """
        if agent_type == 'trader':
            agent = Trader(agent_id)
        elif agent_type == 'researcher':
            agent = Researcher(agent_id)
        elif agent_type == 'analyst':
            agent = Analyst(agent_id)
        elif agent_type == 'optimizer':
            agent = Optimizer(agent_id)
        else:
            log_error(f"Agent type {agent_type} is not recognized.")
            return None
        return agent

    def configure_agent(self, agent):
        """
        Configure the agent with the necessary parameters such as initial resources, tasks, and environment setup.
        :param agent: The agent to configure.
        :return: None
        """
        agent.resources = self.config.get("initial_resources", 100)
        agent.reputation = self.config.get("initial_reputation", 50)
        log_info(f"Agent {agent.agent_id} configured with resources: {agent.resources} and reputation: {agent.reputation}.")

    def deploy_agents(self, num_agents: int):
        """
        Deploy a number of agents into the environment.
        :param num_agents: Number of agents to deploy.
        :return: None
        """
        agent_count = 0
        while agent_count < num_agents:
            agent_type = random.choice(['trader', 'researcher', 'analyst', 'optimizer'])  # Randomly pick agent type
            agent = self.create_agent(agent_type, agent_count)
            if agent:
                self.configure_agent(agent)  # Configure agent before deployment
                self.environment.add_agent(agent)  # Add agent to the environment
                self.deployed_agents.append(agent)
                log_info(f"Agent {agent.agent_id} of type {agent_type} deployed successfully.")
                agent_count += 1

    def start_agents(self):
        """
        Start all deployed agents, allowing them to begin interacting with the environment.
        :return: None
        """
        for agent in self.deployed_agents:
            log_info(f"Agent {agent.agent_id} is starting.")
            agent.start_task()

    def log_deployment(self):
        """
        Log the details of the deployment process.
        :return: None
        """
        for agent in self.deployed_agents:
            log_info(f"Deployed agent {agent.agent_id} of type {agent.__class__.__name__} with resources {agent.resources} and reputation {agent.reputation}.")

# Main script execution

if __name__ == "__main__":
    deployment_system = AgentDeploymentSystem()
    
    # Deploy 10 agents as an example (could be dynamically configured)
    deployment_system.deploy_agents(num_agents=10)
    
    # Start agents in the system
    deployment_system.start_agents()
    
    # Log deployment details
    deployment_system.log_deployment()
