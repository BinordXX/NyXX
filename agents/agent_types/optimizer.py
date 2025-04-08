# digital_civilization/agents/agent_types/optimizer.py

from agents.agent import Agent
import numpy as np
import random
from datetime import datetime

class OptimizerAgent(Agent):
    def __init__(self, name: str, objective: str = "maximize_output"):
        super().__init__(name=name, role="Optimizer", capabilities=["tune", "evolve", "refactor"])
        self.objective = objective
        self.optimization_log = []

    def perform_task(self, task: dict) -> dict:
        """
        Executes optimizer-related tasks.
        Example task:
        {
            "type": "tune",
            "params": {"learning_rate": [0.01, 0.1, 0.001]},
            "metric_fn": some_function
        }
        """
        task_type = task.get("type")

        if task_type == "tune":
            return self._hyperparameter_tuning(task.get("params"), task.get("metric_fn"))
        elif task_type == "evolve":
            return self._genetic_optimize(task.get("population", []), task.get("fitness_fn"))
        elif task_type == "refactor":
            return self._refactor_logic(task.get("codebase", {}))
        else:
            self.log_event(f"Unsupported task type: {task_type}")
            return {"status": "failed", "reason": "unsupported task"}

    def _hyperparameter_tuning(self, params: dict, metric_fn) -> dict:
        """
        Simple grid search optimizer.
        """
        if not params or not metric_fn:
            return {"status": "failed", "reason": "missing parameters or metric function"}

        best_score = float('-inf')
        best_combo = None
        log = []

        # Basic grid search
        keys = list(params.keys())
        combinations = self._cartesian_product(params)

        for combo in combinations:
            config = dict(zip(keys, combo))
            score = metric_fn(**config)
            log.append((config, score))
            if score > best_score:
                best_score = score
                best_combo = config

        self.optimization_log.append({"best": best_combo, "score": best_score})
        self.log_event(f"Optimized with best config: {best_combo}, score: {best_score}")
        return {"status": "success", "best_config": best_combo, "score": best_score, "log": log}

    def _genetic_optimize(self, population: list, fitness_fn) -> dict:
        """
        Evolutionary optimizer (mocked basic form).
        """
        if not population or not fitness_fn:
            return {"status": "failed", "reason": "missing population or fitness function"}

        scored = [(indiv, fitness_fn(indiv)) for indiv in population]
        scored.sort(key=lambda x: x[1], reverse=True)
        top = scored[:2]

        # "Crossover"
        child = self._crossover(top[0][0], top[1][0])

        # "Mutation"
        mutation_index = random.randint(0, len(child)-1)
        child[mutation_index] = random.random()

        self.log_event("Evolved next generation with crossover + mutation.")
        return {"status": "success", "next_gen": child, "top_fitness": top[0][1]}

    def _refactor_logic(self, codebase: dict) -> dict:
        """
        Placeholder for automatic code refactoring or rewriting logic trees.
        """
        if not codebase:
            return {"status": "failed", "reason": "empty codebase"}

        # Just log and return mocked response
        self.log_event("Refactored logic structure (simulated).")
        return {"status": "success", "refactored": True, "details": "Logic optimized for efficiency."}

    def _cartesian_product(self, param_grid: dict) -> list:
        """
        Generates all combinations from param grid.
        """
        from itertools import product
        return list(product(*param_grid.values()))
