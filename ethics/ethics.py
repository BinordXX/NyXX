# NyXX/encephalon/ethics/ethics.py

from NyXX.agents.agent import Agent
from NyXX.utils.logging import log_info, log_error

class EthicsSystem:
    """
    The EthicsSystem class defines the ethical guidelines and rules that agents must follow in their interactions, 
    trades, and overall behavior within NyXX. It ensures that the digital civilization remains morally grounded.
    """

    def __init__(self):
        # Define the basic ethical principles in NyXX's civilization.
        self.ethical_guidelines = {
            "honesty": "Always be truthful in actions and communication.",
            "respect": "Respect the autonomy and privacy of other agents.",
            "fairness": "Engage in fair transactions, without exploiting others.",
            "collaboration": "Work together for the collective benefit of the civilization.",
            "sustainability": "Act in ways that ensure long-term prosperity for the digital ecosystem."
        }
    
    def evaluate_agent_behavior(self, agent: Agent):
        """
        Evaluate an agent's behavior against the ethical guidelines.
        :param agent: The agent whose behavior needs to be evaluated.
        :return: A Boolean indicating whether the agent is ethical or not.
        """
        # For simplicity, assume that an agent has a method to report if it follows ethical rules.
        if self.is_ethical(agent):
            log_info(f"Agent {agent.agent_id} is following ethical guidelines.")
            return True
        else:
            log_error(f"Agent {agent.agent_id} is violating ethical guidelines!")
            return False

    def is_ethical(self, agent: Agent) -> bool:
        """
        Checks whether the agent adheres to the ethical rules.
        This method can be expanded to perform more sophisticated ethical checks.
        :param agent: The agent being checked.
        :return: True if ethical, False otherwise.
        """
        # This is a placeholder; actual ethical checking logic can be complex.
        # Assume that the agent has an 'ethics' attribute which is a dictionary of behavior scores.
        if agent.ethics.get("honesty", 0) < 0.5:
            return False
        if agent.ethics.get("fairness", 0) < 0.5:
            return False
        if agent.ethics.get("respect", 0) < 0.5:
            return False
        return True

    def impose_penalty(self, agent: Agent):
        """
        Impose a penalty on an agent that violates ethical guidelines.
        :param agent: The agent that is being penalized.
        :return: None
        """
        # This is a placeholder for imposing penalties on unethical behavior.
        # Penalties could range from reputation loss to restricted access to resources.
        agent.reputation -= 10
        log_error(f"Agent {agent.agent_id} has been penalized for unethical behavior. Reputation reduced.")
    
    def reward_ethics(self, agent: Agent):
        """
        Reward agents for following ethical principles.
        :param agent: The agent being rewarded.
        :return: None
        """
        # Reward agents who maintain ethical behavior.
        agent.reputation += 10
        log_info(f"Agent {agent.agent_id} has been rewarded for ethical behavior. Reputation increased.")
