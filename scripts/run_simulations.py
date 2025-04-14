import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../organisms')))

from organisms.citizen import Citizen
from environment.environment import Environment
from utils.loggings import log_info, log_error

def run_simulation(steps: int = 10):
    """
    Run a basic simulation where citizens learn from the environment.
    """
    # Initialize the environment
    env = Environment(name="NyXX-World")
    log_info("Simulation starting...")

    # Create citizens and add them to the environment
    citizen1 = Citizen(name="Citizen1")
    citizen2 = Citizen(name="Citizen2")
    citizen3 = Citizen(name="Citizen3")

    env.add_organism(citizen1)
    env.add_organism(citizen2)
    env.add_organism(citizen3)

    # Run the simulation for a specified number of steps
    for step in range(steps):
        log_info(f"\n--- Simulation Step {step + 1} ---")
        env.run(steps=1)  # Run one simulation step

        # Log the current knowledge of the citizens
        for organism in env.organisms:
            if isinstance(organism, Citizen):
                log_info(f"{organism.name}'s Knowledge: {organism.knowledge}")

    log_info("Simulation finished.")

if __name__ == "__main__":
    try:
        # Run the simulation for 10 steps (can be adjusted)
        run_simulation(steps=5)
    except Exception as e:
        log_error(f"Error running simulation: {e}")
