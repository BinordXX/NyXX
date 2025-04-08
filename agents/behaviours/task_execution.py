# digital_civilization/agents/behavior/task_execution.py

from typing import Dict, Any, List
from time import sleep
import random

class Task:
    """
    Represents a task an agent can perform.
    """
    def __init__(self, task_id: str, task_type: str, parameters: Dict[str, Any]):
        self.task_id = task_id
        self.task_type = task_type
        self.parameters = parameters
        self.status = "pending"  # pending, in_progress, completed, failed
        self.result = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "parameters": self.parameters,
            "status": self.status,
            "result": self.result
        }


class TaskExecutor:
    """
    Executes tasks based on type and input.
    Can be extended or mapped to more complex functions, APIs, or agents.
    """

    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.task_queue: List[Task] = []

    def add_task(self, task: Task):
        print(f"[{self.agent_id}] Task added to queue: {task.task_id} ({task.task_type})")
        self.task_queue.append(task)

    def execute_all(self):
        print(f"[{self.agent_id}] Executing all queued tasks...")
        for task in self.task_queue:
            self._execute_task(task)
        self.task_queue.clear()

    def _execute_task(self, task: Task):
        task.status = "in_progress"
        print(f"[{self.agent_id}] Executing task: {task.task_type} with params {task.parameters}")
        
        try:
            # Simulate task execution time
            sleep(random.uniform(0.2, 0.6))

            # Handle specific task types
            if task.task_type == "analyze_data":
                task.result = self._analyze_data(task.parameters)
            elif task.task_type == "send_message":
                task.result = self._send_message(task.parameters)
            elif task.task_type == "train_model":
                task.result = self._train_model(task.parameters)
            else:
                task.result = {"note": "No-op or unknown task."}

            task.status = "completed"
            print(f"[{self.agent_id}] Task {task.task_id} completed.")
        except Exception as e:
            task.status = "failed"
            task.result = {"error": str(e)}
            print(f"[{self.agent_id}] Task {task.task_id} failed: {e}")

    def _analyze_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        # Placeholder for data analysis logic
        return {"insights": f"Analyzed data with {params}"}

    def _send_message(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "message_sent", "details": params}

    def _train_model(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return {"model": f"trained_model_{random.randint(1,100)}"}

