# digital_civilization/agents/agent_types/trader.py

from agents.agent import Agent
import random
from datetime import datetime

class TraderAgent(Agent):
    def __init__(self, name: str, trading_strategy: str = "random"):
        super().__init__(name=name, role="Trader", capabilities=["trade", "analyze_market"])
        self.trading_strategy = trading_strategy
        self.balance = 1000.0  # virtual currency
        self.portfolio = {}  # item -> quantity
        self.resources = 100 # Define resources attribute, e.g., starting with 100 units
        self.reputation = 0  # Initialize reputation attribute if needed

    

    def perform_task(self, task: dict) -> dict:
        """
        Execute trading-related tasks based on task instructions.
        Example task:
        {
            "type": "trade",
            "market_data": {...}
        }
        """
        task_type = task.get("type")
        if task_type == "trade":
            return self._execute_trade(task.get("market_data", {}))
        else:
            self.log_event(f"Unsupported task type: {task_type}")
            return {"status": "failed", "reason": "unsupported task"}

    def _execute_trade(self, market_data: dict) -> dict:
        """
        Simple example: trader selects a random item and decides to buy or sell.
        """
        if not market_data:
            return {"status": "failed", "reason": "no market data"}

        item = random.choice(list(market_data.keys()))
        price = market_data[item]
        action = random.choice(["buy", "sell"])
        amount = round(random.uniform(1, 10), 2)

        timestamp = datetime.utcnow()

        if action == "buy" and self.balance >= price * amount:
            self.balance -= price * amount
            self.portfolio[item] = self.portfolio.get(item, 0) + amount
            self.log_event(f"Bought {amount} of {item} at {price} each.")
            return {
                "status": "success",
                "action": "buy",
                "item": item,
                "amount": amount,
                "price": price,
                "timestamp": timestamp
            }

        elif action == "sell" and self.portfolio.get(item, 0) >= amount:
            self.balance += price * amount
            self.portfolio[item] -= amount
            self.log_event(f"Sold {amount} of {item} at {price} each.")
            return {
                "status": "success",
                "action": "sell",
                "item": item,
                "amount": amount,
                "price": price,
                "timestamp": timestamp
            }

        else:
            self.log_event(f"Failed to {action} {amount} of {item} at {price} each.")
            return {
                "status": "failed",
                "reason": "insufficient resources",
                "action": action,
                "item": item,
                "price": price,
                "timestamp": timestamp
            }
    def execute_task(self, environment):
        """
        Wrapper method expected by the simulation engine.
        Constructs a task from the environment and delegates to perform_task.
        """
        # Extract market data from environment
        market_data = environment.get_market_data("CryptoMarket")  # You may need to implement this
        task = {
            "type": "trade",
            "market_data": market_data
        }
        return self.perform_task(task)
    def evaluate_performance(self, environment) -> dict:
        """
        Evaluate agent's performance, e.g., by checking profit/loss and portfolio value.
        Returns a dict summary.
        """
        # Calculate total value based on the agent's resources and portfolio
        total_value = self.resources  # Start with current resources (resources or balance as per previous context)
        market_data = environment.get_market_data("CryptoMarket")  # Adjust if you use market names

        # Loop through the portfolio and calculate its value based on the market data
        for item, quantity in self.portfolio.items():
            price = market_data.get(item, 0)  # Default to 0 if no price data is available
            total_value += price * quantity

        # Calculate the performance score as a combination of resources and reputation
        performance_score = self.resources + self.reputation  # Example performance metric

        # Log the agent's performance
        self.logger.info(f"Trader {self.name} performance: Resources={self.resources}, Reputation={self.reputation}, Performance Score={performance_score}")

        # Return the performance as a dictionary summary
        return {
            "agent_id": self.agent_id,  # Correct agent ID to be used here
            "total_value": total_value,  # Total value includes resources and portfolio value
            "performance_score": performance_score,  # Include performance score for this agent
            "resources": self.resources,  # Include resources for clarity
            "reputation": self.reputation,  # Include reputation for reference
            "portfolio": self.portfolio.copy()  # Return a copy of the portfolio for safety
        }
