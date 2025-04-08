# NyXX/encephalon/coremind.py

from datetime import datetime
from NyXX.encephalon.strategy import Strategy
from NyXX.encephalon.data_aggregation import DataAggregator
from NyXX.encephalon.feedback_loop import FeedbackLoop
from NyXX.encephalon.memory import Memory
from NyXX.utils.logging import log_info, log_error


class CoreMind:
    """
    The CoreMind of NyXX.
    Coordinates all agents, orchestrates global decision-making,
    and evolves strategy based on data and feedback.
    """

    def __init__(self):
        self.memory = Memory()
        self.strategy = Strategy()
        self.aggregator = DataAggregator()
        self.feedback = FeedbackLoop()
        self.current_state = {}

    def initialize(self):
        log_info("CoreMind initializing...")
        self.memory.load_state()
        self.strategy.initialize()
        log_info("Initialization complete.")

    def perceive(self, agent_reports):
        """
        Ingest observations and status reports from agents.
        """
        try:
            aggregated = self.aggregator.aggregate(agent_reports)
            self.current_state.update(aggregated)
            log_info("CoreMind perception complete.")
        except Exception as e:
            log_error(f"Perception error: {str(e)}")

    def think(self):
        """
        Generate high-level strategies based on the current global state.
        """
        try:
            decision = self.strategy.decide(self.current_state)
            log_info(f"Strategic decision made: {decision}")
            return decision
        except Exception as e:
            log_error(f"Thinking error: {str(e)}")
            return {}

    def act(self):
        """
        Broadcast decisions back to agents.
        """
        actions = self.think()
        log_info("CoreMind broadcasting actions.")
        return actions

    def reflect(self, agent_feedback):
        """
        Analyze feedback from agents and update internal models.
        """
        try:
            self.feedback.process(agent_feedback)
            self.memory.save_state(self.current_state)
            log_info("CoreMind reflection complete.")
        except Exception as e:
            log_error(f"Reflection error: {str(e)}")

    def pulse(self, agent_reports, agent_feedback):
        """
        One cycle of CoreMind's cognitive loop.
        """
        log_info(f"--- CoreMind Pulse @ {datetime.utcnow()} ---")
        self.perceive(agent_reports)
        actions = self.act()
        self.reflect(agent_feedback)
        return actions
