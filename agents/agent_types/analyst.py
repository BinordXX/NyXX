# digital_civilization/agents/agent_types/analyst.py

from agents.agent import Agent
from datetime import datetime
import numpy as np

class AnalystAgent(Agent):
    def __init__(self, name: str, domain: str = "strategy"):
        super().__init__(name=name, role="Analyst", capabilities=["interpret", "predict", "recommend"])
        self.domain = domain
        self.insights_archive = []

    def perform_task(self, task: dict) -> dict:
        """
        Executes analyst-related tasks.
        Example task:
        {
            "type": "interpret",
            "data": [...]
        }
        """
        task_type = task.get("type")
        if task_type == "interpret":
            return self._interpret_insights(task.get("data", []))
        elif task_type == "predict":
            return self._predict_outcomes(task.get("trend_data", []))
        elif task_type == "recommend":
            return self._recommend_action(task.get("context", {}))
        else:
            self.log_event(f"Unsupported task type: {task_type}")
            return {"status": "failed", "reason": "unsupported task"}

    def _interpret_insights(self, data: list) -> dict:
        """
        Interprets incoming insights into meaningful summaries.
        """
        if not data:
            return {"status": "failed", "reason": "no data provided"}

        avg = np.mean(data)
        std = np.std(data)
        interpretation = {
            "average": avg,
            "volatility": std,
            "timestamp": datetime.utcnow()
        }

        self.insights_archive.append(interpretation)
        self.log_event(f"Interpreted insights with avg={avg:.2f}, volatility={std:.2f}")
        return {"status": "success", "interpretation": interpretation}

    def _predict_outcomes(self, trend_data: list) -> dict:
        """
        Predicts future trends based on simple linear extrapolation.
        """
        if len(trend_data) < 2:
            return {"status": "failed", "reason": "insufficient data for prediction"}

        x = np.arange(len(trend_data))
        y = np.array(trend_data)
        coef = np.polyfit(x, y, 1)
        slope, intercept = coef
        prediction = intercept + slope * (len(trend_data) + 1)

        self.log_event(f"Predicted next value as {prediction:.2f} from trend data")
        return {"status": "success", "prediction": prediction, "slope": slope, "intercept": intercept}

    def _recommend_action(self, context: dict) -> dict:
        """
        Offers a recommendation based on context.
        """
        domain = context.get("domain", self.domain)
        urgency = context.get("urgency", "medium")
        risk = context.get("risk", "moderate")

        # Simple logic engine (can be replaced with a rule engine)
        if urgency == "high" and risk != "high":
            action = "Act immediately with calculated buffer."
        elif risk == "high":
            action = "Delay action, seek more data."
        else:
            action = "Proceed with pilot implementation."

        recommendation = {
            "domain": domain,
            "recommendation": action,
            "timestamp": datetime.utcnow()
        }

        self.log_event(f"Recommendation made for {domain}: {action}")
        return {"status": "success", "recommendation": recommendation}
