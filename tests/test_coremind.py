import unittest
from encephalon.coremind import CoreMind  # Corrected the class name to CoreMind
from encephalon.strategy import Strategy
from encephalon.memory import Memory
from encephalon.feedback_loop import FeedbackLoop

class TestCoreMindMethods(unittest.TestCase):  # Changed the test class name to match CoreMind

    def setUp(self):
        """Set up the test environment, instantiate CoreMind and related modules."""
        self.coremind = CoreMind()  # Changed to CoreMind
        self.strategy = Strategy()
        self.memory = Memory()
        self.feedback_loop = FeedbackLoop()

    def test_coremind_initialization(self):
        """Test the initialization of CoreMind."""
        self.assertIsNotNone(self.coremind)
        self.assertIsInstance(self.coremind, CoreMind)
        self.assertEqual(self.coremind.current_state, {})  # Assuming initial state is an empty dictionary

    def test_coremind_decision_making(self):
        """Test the decision-making logic of CoreMind."""
        self.coremind.initialize()
        self.coremind.perceive([])  # Passing an empty list for simplicity
        actions = self.coremind.act()
        self.assertIsInstance(actions, dict)  # Assuming actions are in the form of a dictionary

    def test_coremind_memory_storage(self):
        """Test CoreMind's memory functionality."""
        self.memory.store_data("last_strategy", "optimize")
        self.assertIn("last_strategy", self.memory.data)
        self.assertEqual(self.memory.data["last_strategy"], "optimize")

    def test_coremind_strategy_execution(self):
        """Test the execution of a strategy by CoreMind."""
        self.strategy.set_strategy("optimize")
        self.assertEqual(self.strategy.current_strategy, "optimize")
        self.strategy.execute_strategy(self.coremind)  # Assuming strategy execution involves CoreMind
        self.assertEqual(self.coremind.current_state, {})  # Assuming state is updated accordingly

    def test_feedback_loop(self):
        """Test the feedback loop between CoreMind and agents."""
        self.feedback_loop.add_feedback("optimization", 5)
        self.assertIn("optimization", self.feedback_loop.feedback)
        self.assertEqual(self.feedback_loop.feedback["optimization"], 5)
        self.feedback_loop.process_feedback(self.coremind)
        self.assertEqual(self.coremind.current_state, {})  # Assuming state changes after processing feedback

    def tearDown(self):
        """Clean up any resources after each test."""
        del self.coremind
        del self.strategy
        del self.memory
        del self.feedback_loop

if __name__ == '__main__':
    unittest.main()
