# digital_civilization/agents/agent_types/researcher.py

from ..agent import Agent
import random
from datetime import datetime
import math

class ResearcherAgent(Agent):
    def __init__(self, name: str, domain: str = "general"):
        super().__init__(name=name, role="Researcher", capabilities=["analyze", "generate_hypothesis", "run_experiments"])
        self.domain = domain
        self.knowledge_base = {}  # concept -> insight
        self.research_log = []
        self.resources = 100  # Add this if the agent doesn't manage resources.
        self.reputation = 5  # Reputation attribute.
        self.portfolio = {}  # Or any other necessary attributes.

    def perform_task(self, task: dict) -> dict:
        """
        Executes research-related tasks.
        Example task:
        {
            "type": "analyze",
            "data": [...]
        }
        """
        task_type = task.get("type")
        if task_type == "analyze":
            return self._analyze_data(task.get("data", []))
        elif task_type == "hypothesize":
            return self._generate_hypothesis(task.get("topic", "unknown"))
        elif task_type == "experiment":
            return self._run_experiment(task.get("parameters", {}))
        else:
            self.log_event(f"Unsupported task type: {task_type}")
            return {"status": "failed", "reason": "unsupported task"}

    def _analyze_data(self, data: list) -> dict:
        """
        Performs a basic statistical analysis on the data.
        """
        if not data:
            return {"status": "failed", "reason": "no data provided"}

        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std_dev = math.sqrt(variance)

        insight = {
            "mean": mean,
            "std_dev": std_dev,
            "sample_size": n,
            "timestamp": datetime.utcnow()
        }

        self.knowledge_base[f"analysis_{len(self.knowledge_base)}"] = insight
        self.research_log.append(insight)
        self.log_event(f"Analyzed data: mean={mean:.2f}, std_dev={std_dev:.2f}")
        return {"status": "success", "insight": insight}
    

    def _generate_hypothesis(self, topic: str) -> dict:
        """
        Randomly generate a hypothesis.
        """
        hypothesis = f"If conditions in {topic} change, then outcome X might occur due to unknown variable Y."
        self.knowledge_base[f"hypothesis_{len(self.knowledge_base)}"] = hypothesis
        self.log_event(f"Generated hypothesis on {topic}")
        return {"status": "success", "hypothesis": hypothesis}

    def _run_experiment(self, parameters: dict) -> dict:
        """
        Simulate a basic experiment using parameters.
        """
        outcome = random.choice(["positive", "negative", "inconclusive"])
        result = {
            "parameters": parameters,
            "outcome": outcome,
            "timestamp": datetime.utcnow()
        }
        self.research_log.append(result)
        self.log_event(f"Ran experiment with result: {outcome}")
        return {"status": "success", "result": result}
    def execute_task(self, environment):
        """
        Wrapper method for compatibility with the simulation engine.
        ResearcherAgent performs research based on market data.
        """
        market_data = environment.get_market_data("default_market")  # Adjust market name as needed
        task = {
            "type": "research",
            "market_data": market_data
        }
        return self.perform_task(task)
    def evaluate_performance(self, environment):
        """
        Evaluates the performance of the researcher in the given environment.
        This can include checking if the agent's research goals are met, 
        if the agent's contributions are being utilized, etc.
        """
        # Example of evaluation logic
        performance_score = 0
        # For simplicity, assume you check the presence of certain research data
        if self.research_log:
            performance_score = len(self.research_log)  # Score based on the number of research outputs

        # Log the performance evaluation
        self.logger.info(f"Researcher {self.name} with ID {self.agent_id} has performance score: {performance_score}")
        
        return performance_score