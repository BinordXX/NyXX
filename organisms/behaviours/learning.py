# digital_civilization/agents/behavior/learning.py

import random
import numpy as np
from collections import defaultdict

class LearningModule:
    """
    Base class for learning mechanisms across agents.
    Supports Q-Learning for now. Can be extended to Deep RL, evolutionary strategies, imitation learning, etc.
    """

    def __init__(self, learning_rate=0.1, discount_factor=0.95, exploration_rate=0.2):
        self.q_table = defaultdict(lambda: defaultdict(float))
        self.alpha = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        self.learning_log = []

    def choose_action(self, state, possible_actions):
        """
        Chooses an action using an epsilon-greedy strategy.
        """
        if random.random() < self.epsilon:
            action = random.choice(possible_actions)
            self._log_event(f"Exploring: chose random action {action}")
            return action
        else:
            q_values = {a: self.q_table[state][a] for a in possible_actions}
            max_action = max(q_values, key=q_values.get)
            self._log_event(f"Exploiting: chose best action {max_action} with Q-value {q_values[max_action]:.3f}")
            return max_action

    def update(self, state, action, reward, next_state, possible_next_actions):
        """
        Q-learning update rule.
        """
        max_q_next = max([self.q_table[next_state][a] for a in possible_next_actions], default=0)
        old_value = self.q_table[state][action]
        new_value = old_value + self.alpha * (reward + self.gamma * max_q_next - old_value)
        self.q_table[state][action] = new_value

        self._log_event(
            f"Updated Q({state}, {action}) from {old_value:.3f} to {new_value:.3f} with reward {reward}, next best {max_q_next:.3f}"
        )

    def get_q_table(self):
        return dict(self.q_table)

    def _log_event(self, message):
        self.learning_log.append({"timestamp": self._timestamp(), "message": message})
        print(f"[LearningModule] {message}")

    def _timestamp(self):
        from datetime import datetime
        return datetime.utcnow().isoformat()
