# NyXX/encephalon/environment/scenario.py

import random
from datetime import datetime
from NyXX.utils.logging import log_info, log_error
from NyXX.environment.data_provider import DataProvider

class Scenario:
    """
    The Scenario class defines various events or conditions that simulate different environments
    that agents will operate in. Scenarios are dynamic and affect the agents' decisions and strategies.
    """

    def __init__(self, scenario_type):
        """
        Initialize a specific scenario based on type.
        :param scenario_type: Type of the scenario (e.g., 'market_crash', 'weather_change').
        """
        self.scenario_type = scenario_type
        self.data_provider = DataProvider()

    def activate_scenario(self):
        """
        Activate the scenario and adjust the environment accordingly.
        """
        log_info(f"Activating scenario: {self.scenario_type}")
        if self.scenario_type == 'market_crash':
            return self._market_crash_scenario()
        elif self.scenario_type == 'weather_change':
            return self._weather_change_scenario()
        elif self.scenario_type == 'political_tension':
            return self._political_tension_scenario()
        elif self.scenario_type == 'new_technology':
            return self._new_technology_scenario()
        else:
            log_error(f"Scenario {self.scenario_type} is not recognized.")
            return None

    def _market_crash_scenario(self):
        """
        Simulate a sudden market crash, reducing stock prices drastically.
        :return: Simulated market crash data.
        """
        log_info("Simulating a market crash...")
        crash_data = self.data_provider.simulate_stock_data()
        crash_data['price'] *= random.uniform(0.1, 0.3)  # Reduce the price drastically to simulate a crash
        crash_data['event'] = "Market Crash"
        return crash_data

    def _weather_change_scenario(self):
        """
        Simulate a dramatic weather change, affecting temperature and conditions.
        :return: Simulated weather data with extreme conditions.
        """
        log_info("Simulating a dramatic weather change...")
        weather_data = self.data_provider.simulate_weather_data()
        weather_data['temperature'] = random.uniform(-20, 50)  # Extreme temperature change
        weather_data['condition'] = random.choice(['stormy', 'flooding', 'heatwave'])
        weather_data['event'] = "Weather Change"
        return weather_data

    def _political_tension_scenario(self):
        """
        Simulate a scenario where political tensions are high, affecting markets and behavior.
        :return: Simulated event affecting agent behavior.
        """
        log_info("Simulating political tensions...")
        political_event = random.choice(['election', 'war', 'treaty', 'embargo'])
        tension_level = random.uniform(0.5, 1.5)  # Random tension multiplier
        event_data = {
            'event': "Political Tension",
            'type': political_event,
            'tension_level': tension_level,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return event_data

    def _new_technology_scenario(self):
        """
        Simulate the release of a groundbreaking new technology that impacts the economy and agents.
        :return: Simulated technology event.
        """
        log_info("Simulating new technological breakthrough...")
        tech_breakthrough = random.choice(['quantum_computing', 'artificial_intelligence', 'blockchain'])
        breakthrough_impact = random.uniform(0.3, 2.0)  # Random multiplier for market impact
        tech_data = {
            'event': "New Technology",
            'type': tech_breakthrough,
            'impact_level': breakthrough_impact,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return tech_data

    def get_current_scenario(self):
        """
        Retrieve the current active scenario data.
        :return: Current scenario data.
        """
        log_info(f"Current scenario is {self.scenario_type}.")
        return self.activate_scenario()

    def reset_scenario(self):
        """
        Reset the scenario to its initial state. (Useful for simulation restart or reinitialization).
        :return: None
        """
        log_info("Resetting scenario to initial state...")
        self.scenario_type = None
