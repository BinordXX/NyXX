import unittest
from NyXX.environment.environment import Environment
from NyXX.environment.market import Market
from NyXX.environment.data_provider import DataProvider
from NyXX.environment.scenario import Scenario

class TestEnvironmentMethods(unittest.TestCase):

    def setUp(self):
        """Set up the test environment and instantiate relevant components."""
        self.environment = Environment()
        self.market = Market()
        self.data_provider = DataProvider()
        self.scenario = Scenario()

    def test_environment_initialization(self):
        """Test the initialization of the environment."""
        self.assertIsNotNone(self.environment)
        self.assertIsInstance(self.environment, Environment)
        self.assertEqual(self.environment.state, "idle")  # Assuming initial state is "idle"

    def test_market_simulation(self):
        """Test the market system functionality."""
        self.market.initialize_market()
        self.assertEqual(self.market.state, "active")  # Assuming market starts as active
        self.market.simulate_trade()
        self.assertTrue(self.market.trades)  # Assuming market simulates trades correctly

    def test_data_provider_integration(self):
        """Test the integration of external data provider."""
        data = self.data_provider.fetch_data("external_data_source")
        self.assertIsNotNone(data)  # Check that data is successfully fetched
        self.assertGreater(len(data), 0)  # Ensure the data is not empty

    def test_scenario_execution(self):
        """Test scenario execution in the environment."""
        self.scenario.load_scenario("test_scenario_1")
        self.assertEqual(self.scenario.state, "loaded")  # Assuming scenario loads successfully
        self.scenario.run_scenario(self.environment)
        self.assertEqual(self.scenario.state, "running")  # Check if scenario starts running

    def tearDown(self):
        """Clean up any resources after each test."""
        del self.environment
        del self.market
        del self.data_provider
        del self.scenario

if __name__ == '__main__':
    unittest.main()
