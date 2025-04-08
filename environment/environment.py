# NyXX/encephalon/environment.py

import random
from NyXX.utils.logging import log_info, log_error


class Environment:
    """
    The Environment class represents the virtual ecosystem where agents interact.
    It serves as the world in which agents perform their tasks, trade, and make decisions.
    """

    def __init__(self):
        """
        Initialize the environment.
        Set up necessary resources such as simulated markets, external data, and scenarios.
        """
        self.markets = {}  # Dictionary to hold market states
        self.external_data_sources = []  # List of external data sources (e.g., APIs)
        self.scenarios = []  # List of pre-configured scenarios for testing agent behaviors

    def add_market(self, market_name, market_data):
        """
        Add a new market to the environment.
        :param market_name: The name of the market (e.g., "CryptoMarket", "StockMarket").
        :param market_data: The data related to the market (e.g., stock prices, market trends).
        """
        self.markets[market_name] = market_data
        log_info(f"Market '{market_name}' added to the environment.")

    def remove_market(self, market_name):
        """
        Remove a market from the environment.
        :param market_name: The name of the market to remove.
        """
        if market_name in self.markets:
            del self.markets[market_name]
            log_info(f"Market '{market_name}' removed from the environment.")
        else:
            log_error(f"Market '{market_name}' not found in environment.")

    def add_external_data_source(self, data_source):
        """
        Add a new external data source to the environment.
        :param data_source: An external data provider (e.g., API endpoint, database connection).
        """
        self.external_data_sources.append(data_source)
        log_info("External data source added to the environment.")

    def add_scenario(self, scenario_name, scenario_data):
        """
        Add a new scenario for testing agents in the environment.
        :param scenario_name: The name of the scenario (e.g., "MarketCrash", "HighDemand").
        :param scenario_data: Data or conditions associated with the scenario.
        """
        self.scenarios.append((scenario_name, scenario_data))
        log_info(f"Scenario '{scenario_name}' added to the environment.")

    def simulate_event(self):
        """
        Simulate an event within the environment (e.g., market fluctuation, data update).
        This could trigger agent actions or decisions.
        """
        event = random.choice(self.scenarios)
        scenario_name, scenario_data = event
        log_info(f"Simulating scenario: {scenario_name}. Data: {scenario_data}")
        # Event simulation logic could trigger agent tasks
        return scenario_name, scenario_data

    def get_market_data(self, market_name):
        """
        Retrieve data for a specific market.
        :param market_name: The name of the market (e.g., "CryptoMarket").
        :return: Market data or None if not found.
        """
        return self.markets.get(market_name, None)

