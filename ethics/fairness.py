# NyXX/ethics/fairness.py

from NyXX.agents.agent import Agent
from NyXX.utils.logging import log_info, log_error

class FairnessSystem:
    """
    The FairnessSystem class ensures that agents behave fairly in all interactions, especially in trade, decision-making,
    and resource allocation within NyXX's economy.
    """

    def __init__(self):
        # Basic fairness rules
        self.fairness_rules = {
            "no_exploitation": "Agents must not exploit other agents for personal gain.",
            "equal_opportunity": "Agents must provide equal opportunities to other agents, especially in resource allocation."
        }

    def check_fairness(self, agent: Agent):
        """
        Check if an agent’s actions align with fairness guidelines.
        :param agent: The agent whose fairness is being checked.
        :return: None
        """
        if not self.is_fair(agent):
            log_error(f"Agent {agent.agent_id} is acting unfairly.")
            self.impose_penalty(agent)

    def is_fair(self, agent: Agent) -> bool:
        """
        Check whether the agent's actions meet fairness criteria.
        :param agent: The agent to evaluate.
        :return: True if fair, False otherwise.
        """
        if agent.behavior.get("exploitation", False):
            return False
        if agent.behavior.get("unequal_opportunity", False):
            return False
        return True
    
    def impose_penalty(self, agent: Agent):
        """
        Penalize unfair behavior.
        :param agent: The agent to penalize.
        :return: None
        """
        # Penalties could involve loss of resources or reputation.
        agent.reputation -= 30
        log_error(f"Agent {agent.agent_id} has been penalized for unfair behavior.")
