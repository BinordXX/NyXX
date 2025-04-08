# NyXX/encephalon/data_aggregation.py

from NyXX.utils.logging import log_info, log_error


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
        """
        try:
            log_info("Aggregating data from agents...")
            for report in agent_reports:
                self._process_agent_report(report)
            log_info("Data aggregation complete.")
            return self.data_store
        except Exception as e:
            log_error(f"Data aggregation error: {str(e)}")
            return {}

    def _process_agent_report(self, report):
        """
        Process a single agent report and store relevant data in the central repository.
        """
        # Here we would process and filter the report data to keep relevant details
        agent_id = report.get("agent_id")
        if agent_id:
            if agent_id not in self.data_store:
                self.data_store[agent_id] = []
            self.data_store[agent_id].append(report)
        else:
            log_error(f"Invalid agent report: {report}")

    def get_aggregated_data(self):
        """
        Retrieve the aggregated data for further processing or decision making.
        """
        return self.data_store
