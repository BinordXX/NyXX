# NyXX/encephalon/economy/trade_system.py

import random
from NyXX.utils.logging import log_info, log_error
from NyXX.agents.agent import Agent

class TradeSystem:
    """
    The TradeSystem class facilitates the buying and selling of goods, services, and other assets
    within the NyXX economy. It manages trade transactions between agents, monitors supply and demand,
    and tracks trade history.
    """

    def __init__(self, trade_fee_rate=0.02):
        """
        Initialize the trade system.
        :param trade_fee_rate: The percentage fee charged on each transaction.
        """
        self.trade_fee_rate = trade_fee_rate  # Default 2% fee for each trade
        self.trade_history = []  # List to store completed trade transactions

    def initiate_trade(self, buyer: Agent, seller: Agent, asset, amount, price):
        """
        Initiate a trade transaction between two agents.
        :param buyer: The agent buying the asset.
        :param seller: The agent selling the asset.
        :param asset: The asset being traded (could be any object or resource).
        :param amount: The quantity of the asset being traded.
        :param price: The price per unit of the asset.
        :return: None
        """
        total_price = price * amount  # Calculate the total price of the trade
        trade_fee = total_price * self.trade_fee_rate  # Calculate trade fee
        net_price = total_price - trade_fee  # Net price to seller after trade fee

        if buyer.get_balance() >= total_price:  # Ensure buyer has enough balance
            buyer.update_balance(-total_price)
            seller.update_balance(net_price)
            self.record_trade(buyer, seller, asset, amount, price, trade_fee)
            log_info(f"Trade successful! Agent {buyer.agent_id} bought {amount} of {asset} from Agent {seller.agent_id} for {total_price}.")
        else:
            log_error(f"Trade failed: Agent {buyer.agent_id} does not have enough funds.")

    def record_trade(self, buyer: Agent, seller: Agent, asset, amount, price, fee):
        """
        Record the trade transaction in the trade history.
        :param buyer: The agent who bought the asset.
        :param seller: The agent who sold the asset.
        :param asset: The asset being traded.
        :param amount: The quantity of the asset being traded.
        :param price: The price of the asset.
        :param fee: The fee charged by the system for the trade.
        :return: None
        """
        trade_details = {
            "buyer_id": buyer.agent_id,
            "seller_id": seller.agent_id,
            "asset": asset,
            "amount": amount,
            "price_per_unit": price,
            "total_value": price * amount,
            "trade_fee": fee,
            "net_price_to_seller": (price * amount) - fee,
            "trade_timestamp": random.randint(1, 1000000),  # Random timestamp for trade
        }
        self.trade_history.append(trade_details)
        log_info(f"Trade recorded: {trade_details}")

    def get_trade_history(self):
        """
        Get the history of all completed trades.
        :return: A list of trade history records.
        """
        return self.trade_history

    def get_trade_fee(self, price):
        """
        Calculate the trade fee for a given price.
        :param price: The total value of the trade.
        :return: The fee applied to the trade.
        """
        return price * self.trade_fee_rate

    def adjust_market_price(self, asset, demand_factor=1.0, supply_factor=1.0):
        """
        Adjust the price of an asset based on market demand and supply.
        :param asset: The asset whose price is being adjusted.
        :param demand_factor: The demand factor affecting price (e.g., demand increase = price increase).
        :param supply_factor: The supply factor affecting price (e.g., limited supply = price increase).
        :return: Adjusted price of the asset.
        """
        base_price = random.randint(50, 500)  # Base price for an asset
        adjusted_price = base_price * demand_factor / supply_factor
        log_info(f"Adjusted price for {asset}: {adjusted_price}")
        return adjusted_price
