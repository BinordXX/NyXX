import random
from typing import List
from utils.loggings import log_info, log_error
from organisms.citizen import Citizen
from environment.data_provider import BasicDataSource  # Import the basic data source class

class Environment:
    """
    The Environment class represents the world where all digital organisms—citizens and agents—live.
    This is the central simulation space where citizens learn, grow, and evolve into agents.
    """

    def __init__(self, name: str = "NyXX-World"):
        self.name = name
        self.organisms: List[Citizen] = []  # All citizens, including agents
        self.markets = {}  # Market simulations
        self.external_data_sources = []  # APIs, files, generated data
        self.scenarios = []  # Optional global scenarios

        # Create a basic data source for initial learning
        self.basic_data_source = BasicDataSource()

        log_info(f"[{self.name}] Environment initialized.")

    def add_organism(self, citizen: Citizen):
        """
        Add a new citizen (or agent) into the world.
        """
        if isinstance(citizen, Citizen):
            self.organisms.append(citizen)
            log_info(f"Citizen {citizen.name} (ID: {citizen.citizen_id}) entered {self.name}.")
        else:
            log_error("Only citizens (including agents) can be added to the environment.")

    def step(self):
        """
        Advance the simulation one tick.
        Each organism learns or acts depending on its current state.
        Citizens learn from the environment in this step.
        """
        for organism in self.organisms:
            if hasattr(organism, "learn"):
                organism.learn(self)  # Pass the environment to the citizen for learning
            if hasattr(organism, "act"):
                organism.act()

    def add_market(self, market_name, market_data):
        """
        Add a market into the world for agents to interact with.
        """
        self.markets[market_name] = market_data
        log_info(f"Market '{market_name}' added to {self.name}.")

    def get_market(self, market_name):
        """
        Retrieve a market by name.
        """
        return self.markets.get(market_name, None)

    def simulate_event(self):
        """
        Simulate a scenario, like a data shift or market change.
        """
        if self.scenarios:
            scenario = random.choice(self.scenarios)
            scenario_name, data = scenario
            log_info(f"Simulating scenario: {scenario_name}")
            return scenario_name, data
        else:
            log_info("No scenarios to simulate.")
            return None

    def add_external_data_source(self, source):
        """
        Add an external data source to the environment.
        Citizens will use this to learn.
        """
        self.external_data_sources.append(source)
        log_info("External data source added to environment.")

    def run(self, steps: int = 1):
        """
        Run the simulation for a number of steps.
        """
        log_info(f"Starting simulation in {self.name} for {steps} steps.")
        for _ in range(steps):
            self.step()
        log_info(f"Simulation completed.")

    def get_random_fact(self):
        """
        Retrieve a random fact from the basic data source.
        """
        return self.basic_data_source.get_random_fact()
