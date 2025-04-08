# NyXX/encephalon/economy/agent_earnings.py

import random
from NyXX.utils.logging import log_info, log_error

class AgentEarnings:
    """
    The AgentEarnings class is responsible for managing the financial transactions
    and earnings of agents in the NyXX system. This includes tracking income,
    managing balances, and processing transactions.
    """

    def __init__(self, agent_id, initial_balance=1000):
        """
        Initialize the agent's financial system.
        :param agent_id: Unique identifier for the agent.
        :param initial_balance: Starting balance for the agent (default is 1000).
        """
        self.agent_id = agent_id
        self.balance = initial_balance
        self.assets = {}  # Dictionary to track assets owned by the agent
        self.transactions = []  # List to track all transactions (income/spending)

        log_info(f"Agent {self.agent_id} initialized with balance: {self.balance}.")

    def update_balance(self, amount):
        """
        Update the agent's balance by adding or subtracting the amount.
        :param amount: The amount to add (positive) or subtract (negative) from the balance.
        """
        self.balance += amount
        log_info(f"Agent {self.agent_id} balance updated by {amount}. New balance: {self.balance}.")

    def buy_asset(self, asset_name, quantity, asset_price):
        """
        Simulate buying an asset. The agent's balance is updated accordingly.
        :param asset_name: Name of the asset to purchase.
        :param quantity: Quantity of the asset to buy.
        :param asset_price: Price of one unit of the asset.
        :return: None
        """
        total_cost = asset_price * quantity
        if self.balance >= total_cost:
            self.update_balance(-total_cost)
            self.assets[asset_name] = self.assets.get(asset_name, 0) + quantity
            self.transactions.append(f"Bought {quantity} units of {asset_name} for {total_cost}.")
            log_info(f"Agent {self.agent_id} bought {quantity} units of {asset_name} for {total_cost}.")
        else:
            log_error(f"Agent {self.agent_id} does not have enough funds to buy {quantity} units of {asset_name}.")

    def sell_asset(self, asset_name, quantity, asset_price):
        """
        Simulate selling an asset. The agent's balance is updated accordingly.
        :param asset_name: Name of the asset to sell.
        :param quantity: Quantity of the asset to sell.
        :param asset_price: Price of one unit of the asset.
        :return: None
        """
        if asset_name in self.assets and self.assets[asset_name] >= quantity:
            total_earnings = asset_price * quantity
            self.update_balance(total_earnings)
            self.assets[asset_name] -= quantity
            self.transactions.append(f"Sold {quantity} units of {asset_name} for {total_earnings}.")
            log_info(f"Agent {self.agent_id} sold {quantity} units of {asset_name} for {total_earnings}.")
        else:
            log_error(f"Agent {self.agent_id} doesn't own enough {asset_name} to sell.")

    def earn_income(self, amount):
        """
        Add income to the agent’s balance, simulating earned money from tasks, work, etc.
        :param amount: The amount of income to add.
        """
        self.update_balance(amount)
        self.transactions.append(f"Earnings of {amount} added to balance.")
        log_info(f"Agent {self.agent_id} earned {amount}.")

    def get_balance(self):
        """
        Retrieve the current balance of the agent.
        :return: Current balance of the agent.
        """
        return self.balance

    def get_transactions(self):
        """
        Retrieve the list of all financial transactions for the agent.
        :return: List of transactions.
        """
        return self.transactions

    def get_assets(self):
        """
        Retrieve the list of assets owned by the agent.
        :return: Dictionary of assets.
        """
        return self.assets
