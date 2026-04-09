import time
from src.environment import create_street_grid, get_start_goal
from src.planner import astar
from src.agent import Agent
from src.visualization import animate_simulation


def main():
    print("\n🚀 AI Autonomous Navigation System Starting...\n")

    # Create environment
    grid = create_street_grid(rows=40, cols=40)

    # Get start and goal
    start, goal = get_start_goal(grid)

    print(f"📍 Start Position: {start}")
    print(f"🎯 Goal Position: {goal}")

    # Plan path
    start_time = time.time()
    path = astar(grid, start, goal)
    end_time = time.time()

    if not path:
        print("❌ No path found!")
        return

    print(f"✅ Path found in {end_time - start_time:.4f} seconds")
    print(f"✅ Path Length: {len(path)}")

    # Start simulation
    print("\n▶️ Starting Simulation...\n")
    agent = Agent(start)

    animate_simulation(grid, path, agent, start, goal)


if __name__ == "__main__":
    main()