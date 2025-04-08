import unittest
from economy.agent_earnings import AgentEarnings
from economy.trade_system import TradeSystem
from economy.value_exchange import ValueExchange
from economy.monetization import Monetization

class TestEconomyMethods(unittest.TestCase):

    def setUp(self):
        """Set up the test environment, instantiate the economy systems."""
        self.agent_earnings = AgentEarnings(agent_id=1)
        self.trade_system = TradeSystem()
        self.value_exchange = ValueExchange()
        self.monetization = Monetization()

    def test_agent_earnings_initialization(self):
        """Test agent earnings initialization."""
        self.assertEqual(self.agent_earnings.agent_id, 1)
        self.assertEqual(self.agent_earnings.balance, 0)  # Assuming initial balance is 0
        self.agent_earnings.add_earnings(100)
        self.assertEqual(self.agent_earnings.balance, 100)

    def test_trade_system_transaction(self):
        """Test the trade system transaction."""
        self.trade_system.add_trade("TraderOne", "ItemA", 50)
        self.assertIn("ItemA", self.trade_system.trades)
        self.assertEqual(self.trade_system.trades["ItemA"]["quantity"], 50)
        self.trade_system.execute_trade("ItemA")
        self.assertEqual(self.trade_system.trades["ItemA"]["status"], "executed")

    def test_value_exchange(self):
        """Test the value exchange system."""
        self.value_exchange.add_transaction("TraderOne", "Knowledge", 200)
        self.assertIn("Knowledge", self.value_exchange.transactions)
        self.assertEqual(self.value_exchange.transactions["Knowledge"]["value"], 200)
        self.value_exchange.exchange("Knowledge")
        self.assertEqual(self.value_exchange.transactions["Knowledge"]["status"], "exchanged")

    def test_monetization(self):
        """Test monetization strategies."""
        self.monetization.activate_strategy("Subscription")
        self.assertTrue(self.monetization.is_active)
        self.assertEqual(self.monetization.strategy, "Subscription")
        self.monetization.deactivate_strategy()
        self.assertFalse(self.monetization.is_active)

    def tearDown(self):
        """Clean up any resources after each test."""
        del self.agent_earnings
        del self.trade_system
        del self.value_exchange
        del self.monetization

if __name__ == '__main__':
    unittest.main()
