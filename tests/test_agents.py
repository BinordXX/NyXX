import unittest
from organisms.agent import Agent
from organisms.agents.trader import Trader
from organisms.agents.researcher import Researcher
from organisms.agents.analyst import Analyst
from organisms.agents.optimizer import Optimizer

class TestAgentMethods(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment, instantiate agents."""
        self.trader = Trader(agent_id=1, name="TraderOne")
        self.researcher = Researcher(agent_id=2, name="ResearcherOne")
        self.analyst = Analyst(agent_id=3, name="AnalystOne")
        self.optimizer = Optimizer(agent_id=4, name="OptimizerOne")
        
    def test_agent_initialization(self):
        """Test agent initialization with basic parameters."""
        self.assertEqual(self.trader.name, "TraderOne")
        self.assertEqual(self.researcher.agent_id, 2)
        self.assertIsInstance(self.trader, Trader)
        self.assertIsInstance(self.researcher, Researcher)
        
    def test_trader_behavior(self):
        """Test trader-specific behaviors."""
        self.trader.perform_trade("item1", 100)
        self.assertTrue(self.trader.has_traded)
        self.assertEqual(self.trader.current_trade_item, "item1")
        
    def test_researcher_behavior(self):
        """Test researcher-specific behaviors."""
        self.researcher.conduct_research("AI Trends")
        self.assertTrue(self.researcher.is_researching)
        self.assertEqual(self.researcher.research_topic, "AI Trends")
        
    def test_analyst_behavior(self):
        """Test analyst-specific behaviors."""
        self.analyst.analyze_data([10, 20, 30, 40])
        self.assertTrue(self.analyst.is_analyzing)
        self.assertEqual(self.analyst.analysis_result, 25)  # Example: average of the list
        
    def test_optimizer_behavior(self):
        """Test optimizer-specific behaviors."""
        self.optimizer.optimize_strategy("Market Growth")
        self.assertTrue(self.optimizer.is_optimizing)
        self.assertEqual(self.optimizer.optimization_target, "Market Growth")
    
    def tearDown(self):
        """Clean up any resources after each test."""
        del self.trader
        del self.researcher
        del self.analyst
        del self.optimizer

if __name__ == '__main__':
    unittest.main()
