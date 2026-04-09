import matplotlib.pyplot as plt
import numpy as np
import time


def plot_simulation(grid, path, agent_position, start, goal):
    """
    Plot the current simulation state
    """
    plt.clf()
    plt.imshow(grid, cmap="binary")

    if path:
        path = np.array(path)
        plt.plot(path[:, 1], path[:, 0], color="blue", linewidth=2, label="Path")

    plt.scatter(agent_position[1], agent_position[0], color="yellow", s=80, label="Agent")
    plt.scatter(start[1], start[0], color="green", s=50, label="Start")
    plt.scatter(goal[1], goal[0], color="red", s=50, label="Goal")

    plt.title("Street Navigation Simulation")
    plt.legend()
    plt.pause(0.2)


def animate_simulation(grid, path, agent, start, goal):
    """
    Animate agent moving along the path
    """
    plt.figure(figsize=(8, 8))

    while True:
        plot_simulation(grid, path, agent.position, start, goal)
        moved = agent.move_along_path(path)
        if not moved:
            break
        time.sleep(0.1)

    plt.show()