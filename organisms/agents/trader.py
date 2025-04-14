# NyXX/organisms/agents/trader.py

from organisms.agent import Agent
import random
import logging


class Trader(Agent):
    """
    A Trader is an Agent capable of making decisions related to buying, selling, and trading
    goods or data in the environment. The logic here can grow into market simulations,
    reinforcement learning-based pricing, or game-theoretic bargaining.
    """

    def __init__(self, citizen, market_knowledge=None):
        super().__init__(citizen=citizen, role="trader", capabilities=["trade", "negotiate", "evaluate"])
        self.market_knowledge = market_knowledge if market_knowledge else []
        self.inventory = []  # Holds items available for trade
        self.trade_history = []
        self.logger = logging.getLogger(f"Trader-{self.name}")
        self.logger.info(f"Trader {self.name} is ready to barter in the bazaar.")

    def perform_task(self, task: dict) -> dict:
        """
        Perform a trading task. The task dict can include 'action', 'item', 'value', etc.
        """
        action = task.get("action")
        item = task.get("item")
        value = task.get("value")

        if action == "buy":
            return self.buy(item, value)
        elif action == "sell":
            return self.sell(item, value)
        elif action == "evaluate":
            return self.evaluate_market(item)
        else:
            self.logger.warning(f"Unknown task action: {action}")
            return {"status": "error", "message": "Unknown action"}

    def buy(self, item, value):
        """
        Buy an item (pseudo logic, in future may involve smart contracts, auction dynamics, etc.)
        """
        self.inventory.append(item)
        self.trade_history.append({"type": "buy", "item": item, "value": value})
        self.logger.info(f"{self.name} bought {item} for {value}")
        return {"status": "success", "action": "buy", "item": item, "value": value}

    def sell(self, item, value):
        """
        Sell an item if it's in inventory.
        """
        if item in self.inventory:
            self.inventory.remove(item)
            self.trade_history.append({"type": "sell", "item": item, "value": value})
            self.logger.info(f"{self.name} sold {item} for {value}")
            return {"status": "success", "action": "sell", "item": item, "value": value}
        else:
            self.logger.warning(f"{self.name} tried to sell {item}, but it was not in inventory.")
            return {"status": "error", "message": f"{item} not in inventory"}

    def evaluate_market(self, item):
        """
        Use random market simulation to evaluate an item's potential value.
        Can be replaced by ML predictors later.
        """
        estimated_value = random.uniform(10, 100)
        self.market_knowledge.append({"item": item, "estimated_value": estimated_value})
        self.logger.info(f"{self.name} evaluated {item} at {estimated_value}")
        return {"status": "success", "action": "evaluate", "item": item, "estimated_value": estimated_value}
