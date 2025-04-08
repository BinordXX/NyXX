# NyXX/encephalon/economy/value_exchange.py

from NyXX.agents.agent import Agent
from NyXX.utils.logging import log_info, log_error

class ValueExchangeSystem:
    """
    The ValueExchangeSystem class manages the exchange of non-monetary assets, such as knowledge, resources, 
    skills, and services, between agents in the NyXX civilization. 
    It facilitates bartering, collaborations, and sharing of expertise.
    """

    def __init__(self):
        self.exchange_history = []  # List to store exchange records

    def initiate_exchange(self, initiator: Agent, receiver: Agent, value_type: str, value, trade_terms: str):
        """
        Initiate an exchange of value between two agents (could be knowledge, resources, etc.).
        :param initiator: The agent initiating the exchange.
        :param receiver: The agent receiving the value.
        :param value_type: Type of value (e.g., knowledge, resource, skill).
        :param value: The actual value being exchanged.
        :param trade_terms: Terms of the exchange (e.g., time-bound, condition-based).
        :return: None
        """
        # Validate the exchange request
        if not self.validate_value(value_type, value):
            log_error(f"Exchange failed: Invalid value for type {value_type}.")
            return

        # Initiate the exchange (successful if value is valid)
        self.process_exchange(initiator, receiver, value_type, value, trade_terms)

    def process_exchange(self, initiator: Agent, receiver: Agent, value_type: str, value, trade_terms: str):
        """
        Process the exchange by transferring the value and recording the transaction.
        :param initiator: The agent initiating the exchange.
        :param receiver: The agent receiving the value.
        :param value_type: Type of value being exchanged.
        :param value: The value being exchanged.
        :param trade_terms: Terms of the trade.
        :return: None
        """
        # Transfer the value from initiator to receiver
        receiver.receive_value(value_type, value)

        # Record the exchange in the history
        self.record_exchange(initiator, receiver, value_type, value, trade_terms)

        # Log the successful exchange
        log_info(f"Exchange successful: {initiator.agent_id} exchanged {value} of {value_type} with {receiver.agent_id} on terms: {trade_terms}.")

    def record_exchange(self, initiator: Agent, receiver: Agent, value_type: str, value, trade_terms: str):
        """
        Record the exchange in the exchange history.
        :param initiator: The agent initiating the exchange.
        :param receiver: The agent receiving the value.
        :param value_type: Type of value exchanged.
        :param value: The actual value exchanged.
        :param trade_terms: The conditions or terms of the trade.
        :return: None
        """
        exchange_details = {
            "initiator_id": initiator.agent_id,
            "receiver_id": receiver.agent_id,
            "value_type": value_type,
            "value": value,
            "trade_terms": trade_terms,
            "exchange_timestamp": self.generate_timestamp(),
        }
        self.exchange_history.append(exchange_details)
        log_info(f"Exchange recorded: {exchange_details}")

    def validate_value(self, value_type: str, value) -> bool:
        """
        Validate the value being exchanged based on its type (e.g., is knowledge valid? Is resource amount reasonable?).
        :param value_type: The type of value being exchanged (e.g., knowledge, resource).
        :param value: The actual value.
        :return: True if valid, False otherwise.
        """
        # For simplicity, assume all values are valid if they are not None.
        # Further checks could be implemented based on value types.
        if value is not None:
            return True
        return False

    def generate_timestamp(self):
        """
        Generate a unique timestamp for the exchange.
        :return: A simulated timestamp.
        """
        import random
        return random.randint(1, 1000000)

    def get_exchange_history(self):
        """
        Get the history of all completed exchanges.
        :return: A list of exchange records.
        """
        return self.exchange_history

    def adjust_value(self, value, value_type, demand_factor=1.0, supply_factor=1.0):
        """
        Adjust the value of an asset based on external conditions like demand or supply.
        :param value: The original value.
        :param value_type: The type of asset being exchanged.
        :param demand_factor: The demand factor (e.g., higher demand = higher value).
        :param supply_factor: The supply factor (e.g., limited supply = higher value).
        :return: The adjusted value.
        """
        adjusted_value = value * demand_factor / supply_factor
        log_info(f"Adjusted {value_type} value: {adjusted_value}")
        return adjusted_value
