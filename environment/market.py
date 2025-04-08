# NyXX/encephalon/environment/market.py

import random
from datetime import datetime
from NyXX.utils.logging import log_info, log_error

class Market:
    """
    The Market class simulates a financial market in which trading agents can buy and sell assets.
    The market has fluctuating prices, supply/demand dynamics, and random events that affect asset prices.
    """

    def __init__(self, market_type="stock"):
        """
        Initialize the market.
        :param market_type: Type of the market (e.g., 'stock', 'real_estate', 'commodity').
        """
        self.market_type = market_type
        self.assets = self._initialize_assets()

    def _initialize_assets(self):
        """
        Initialize the assets in the market. For a stock market, this could be a set of stocks or commodities.
        :return: A dictionary of assets with initial prices.
        """
        log_info(f"Initializing assets for {self.market_type} market.")
        assets = {
            "Stock A": random.uniform(50, 100),
            "Stock B": random.uniform(30, 80),
            "Stock C": random.uniform(20, 60),
            "Commodity X": random.uniform(100, 200),
            "Commodity Y": random.uniform(5, 20)
        }
        return assets

    def get_asset_price(self, asset_name):
        """
        Get the current price of a specified asset.
        :param asset_name: Name of the asset (e.g., 'Stock A', 'Commodity X').
        :return: The current price of the asset.
        """
        price = self.assets.get(asset_name)
        if price is None:
            log_error(f"Asset {asset_name} not found in market.")
            return None
        return price

    def buy_asset(self, asset_name, quantity):
        """
        Simulate buying an asset from the market.
        :param asset_name: Name of the asset to buy.
        :param quantity: Quantity of the asset to buy.
        :return: Total cost of the purchase.
        """
        price = self.get_asset_price(asset_name)
        if price is None:
            return None
        total_cost = price * quantity
        log_info(f"Bought {quantity} units of {asset_name} at {price} each. Total cost: {total_cost}")
        return total_cost

    def sell_asset(self, asset_name, quantity):
        """
        Simulate selling an asset on the market.
        :param asset_name: Name of the asset to sell.
        :param quantity: Quantity of the asset to sell.
        :return: Total earnings from the sale.
        """
        price = self.get_asset_price(asset_name)
        if price is None:
            return None
        total_earnings = price * quantity
        log_info(f"Sold {quantity} units of {asset_name} at {price} each. Total earnings: {total_earnings}")
        return total_earnings

    def simulate_market_fluctuations(self):
        """
        Simulate price fluctuations in the market. This can simulate the influence of supply/demand, 
        news, or market sentiment.
        :return: None
        """
        log_info("Simulating market fluctuations...")
        for asset in self.assets:
            fluctuation = random.uniform(-0.05, 0.05)  # Random fluctuation between -5% and +5%
            self.assets[asset] += self.assets[asset] * fluctuation

    def simulate_market_event(self):
        """
        Simulate a random event that could affect the market, such as a crash or a boom.
        :return: None
        """
        event = random.choice(["boom", "crash", "neutral"])
        log_info(f"Simulating market event: {event}")
        
        if event == "boom":
            self._market_boost()
        elif event == "crash":
            self._market_crash()
        else:
            log_info("No major event in the market.")

    def _market_boost(self):
        """
        Simulate a market boom, causing all asset prices to increase by a fixed percentage.
        :return: None
        """
        boost_factor = random.uniform(0.1, 0.3)
        for asset in self.assets:
            self.assets[asset] *= (1 + boost_factor)
        log_info(f"Market boom! All asset prices have increased by {boost_factor * 100:.2f}%.")

    def _market_crash(self):
        """
        Simulate a market crash, causing all asset prices to decrease drastically.
        :return: None
        """
        crash_factor = random.uniform(0.3, 0.6)
        for asset in self.assets:
            self.assets[asset] *= (1 - crash_factor)
        log_info(f"Market crash! All asset prices have decreased by {crash_factor * 100:.2f}%.")
    
    def get_market_status(self):
        """
        Get the current status of the market, including the prices of all assets.
        :return: Dictionary of asset prices.
        """
        log_info("Fetching market status...")
        return self.assets
