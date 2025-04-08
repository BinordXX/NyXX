# NyXX/encephalon/environment/data_provider.py

import requests
import random
from NyXX.utils.logging import log_info, log_error

class DataProvider:
    """
    The DataProvider class acts as the interface to fetch external data for agents and the environment.
    It pulls data from external APIs or simulated data sources.
    """

    def __init__(self):
        """
        Initialize the data provider.
        Can connect to real-world data sources or simulate data for the agents.
        """
        self.external_sources = {
            "stock_market": "https://api.example.com/stockdata",  # Placeholder for a real stock market API
            "weather": "https://api.weather.com/data",  # Placeholder for weather API
            "news": "https://api.news.com/latest",  # Placeholder for a news API
        }

    def get_data(self, data_type, params=None):
        """
        Fetch data from an external source based on the type requested.
        :param data_type: Type of the data (e.g., 'stock_market', 'weather', 'news').
        :param params: Optional parameters for the request (e.g., location for weather).
        :return: Data fetched from the external source.
        """
        if data_type not in self.external_sources:
            log_error(f"Data type '{data_type}' is not a valid source.")
            return None

        url = self.external_sources[data_type]
        try:
            response = requests.get(url, params=params)  # Real-world API call
            if response.status_code == 200:
                log_info(f"Successfully fetched {data_type} data.")
                return response.json()
            else:
                log_error(f"Failed to fetch {data_type} data. Status code: {response.status_code}")
                return None
        except Exception as e:
            log_error(f"Error fetching {data_type} data: {str(e)}")
            return None

    def simulate_stock_data(self):
        """
        Simulate stock data for the trading agents. Randomly generated for now.
        :return: Random simulated stock price data.
        """
        price = random.uniform(50, 500)  # Random price between $50 and $500
        volume = random.randint(1000, 10000)  # Random trade volume between 1,000 and 10,000 shares
        return {"price": price, "volume": volume}

    def simulate_weather_data(self):
        """
        Simulate weather data for environmental agents.
        :return: Random simulated weather data.
        """
        temp = random.uniform(-10, 40)  # Temperature in Celsius
        condition = random.choice(["sunny", "rainy", "cloudy", "snowy"])
        return {"temperature": temp, "condition": condition}

    def get_market_data(self, market_name):
        """
        Get data for a specific market. For now, this will simulate stock market data.
        :param market_name: The name of the market (e.g., 'crypto', 'stock').
        :return: Simulated market data.
        """
        if market_name == "stock":
            return self.simulate_stock_data()
        elif market_name == "weather":
            return self.simulate_weather_data()
        else:
            log_error(f"Market {market_name} data not found.")
            return None

    def get_external_data(self, source_type, params=None):
        """
        Retrieves external data from either simulated or real-world sources.
        :param source_type: The type of data source (e.g., 'weather', 'stock_market').
        :param params: Optional parameters for the request.
        :return: External data or None if the source is unavailable.
        """
        if source_type == "stock_market":
            return self.get_data("stock_market", params)
        elif source_type == "weather":
            return self.get_data("weather", params)
        elif source_type == "news":
            return self.get_data("news", params)
        else:
            log_error(f"Unsupported data source '{source_type}' requested.")
            return None
