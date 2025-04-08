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
