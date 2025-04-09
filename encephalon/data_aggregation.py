# NyXX/encephalon/data_aggregation.py

from utils.loggings import log_info, log_error

class DataAggregator:
    """
    Collects, processes, and aggregates data from various agents.
    This class helps CoreMind to obtain a unified view of the system's state.
    """

    def __init__(self):
        self.data_store = {}

    def aggregate(self, agent_reports):
        """
        Aggregates data reports from all agents into a unified data structure.
        (This method is used when you have a list of agent reports)
        """
        try:
            log_info("Aggregating data from agent reports...")
            for report in agent_reports:
                self._process_agent_report(report)
            log_info("Data aggregation from reports complete.")
            return self.data_store
        except Exception as e:
            log_error(f"Data aggregation error: {str(e)}")
            return {}

    def _process_agent_report(self, report):
        """
        Process a single agent report and store relevant data in the central repository.
        """
        agent_id = report.get("agent_id")
        if agent_id:
            if agent_id not in self.data_store:
                self.data_store[agent_id] = []
            self.data_store[agent_id].append(report)
        else:
            log_error(f"Invalid agent report: {report}")

    def aggregate_data(self, environment):
        """
        Processes the current state of the environment to update the aggregated data.
        For example, this method iterates through all agents in the environment
        and collects performance metrics or other relevant data.
        """
        log_info("Aggregating data from the environment...")
        aggregated = {}
        try:
            for agent in environment.agents:
                # Assume each agent has an `evaluate_performance()` method returning a metric,
                # and that agent objects have an 'id' attribute.
                aggregated[agent.id] = agent.evaluate_performance()
            self.data_store = aggregated
            log_info("Data aggregation from environment complete.")
        except Exception as e:
            log_error(f"Error aggregating data from environment: {str(e)}")
        return self.data_store

    def get_aggregated_data(self):
        """
        Retrieve the aggregated data that has been stored.
        """
        return self.data_store
