import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import colors

# How does it work?
# This function generates a random initial state for an elementary cellular automaton.
# It creates a row of cells (either in state 1 or 2) and evolves it over multiple generations.

def random_initial_state(n_cells=100, n_generations=100):
    # Generate a random initial row of cells (either 1 or 2)
    first_row = np.random.choice([1, 2], size=n_cells)
    
    # Create a spacetime array to store cell states over time
    spacetime = np.zeros(shape=(n_generations, n_cells))
    spacetime[0] = first_row
    
    # Spacetime is used to analyze the data that the cellular automaton will process
    return spacetime
def initialize(n_cells=0, n_generations=100, rule={}):
    # Generate a random initial state for the cellular automaton
    initial_state = random_initial_state(n_cells, n_generations)

    # Set up the colormap and normalization for cell states
    cmap = colors.ListedColormap(['cyan', 'black', 'pink'])
    bounds = [0, 1, 2, 2]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Create a figure for displaying the automaton
    fig = plt.figure()

    # Hide the x and y axes
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)

    # Display the initial state using imshow
    grid = plt.imshow(initial_state, interpolation='nearest', cmap=cmap, norm=norm)

    # Create an animation for evolving the automaton
    ani = animation.FuncAnimation(fig, next_generation,
                                  fargs=(grid, initial_state, rule),
                                  frames=n_generations - 1,
                                  interval=50,
                                  blit=False)

    # Show the plot
    plt.show()


def next_generation(i, grid, initial_state, rule):
    # Get the current generation
    current_generation = initial_state[i]
    new_state = initial_state.copy()

    # Compute the next generation using the specified rule
    new_generation = process(current_generation, rule)

    # Update the state for the next generation
    new_state[i + 1] = new_generation

    # Update the displayed grid
    grid.set_data(new_state)
    initial_state[:] = new_state[:]

    return grid,


def process(generation, rule):
    # Compute the next generation based on the rule
    new_generation = []

    for i, cell in enumerate(generation):
        neighbours = []
        if i == 0:
            neighbours = [generation[len(generation) - 1], cell, generation[1]]
        elif i == len(generation) - 1:
            neighbours = [generation[len(generation) - 2], cell, generation[0]]
        else:
            neighbours = [generation[i - 1], cell, generation[i + 1]]

        new_generation.append(rule[tuple(neighbours)])

    return new_generation


def generate_rule(rule):
    # Convert the rule number to a dictionary of transition rules
    rule_str = format(rule, '#010b')[2:]

    rule = {
        (2, 2, 2): int(rule_str[0]) + 1,
        (2, 2, 1): int(rule_str[1]) + 1,
        (2, 1, 2): int(rule_str[2]) + 1,
        (2, 1, 1): int(rule_str[3]) + 1,
        (1, 2, 2): int(rule_str[4]) + 1,
        # ... (continue with other rules if needed)
    }

    return rule

# This part will allow my user to just choose the numbers they want for cell, gens, and rule 
# maybe I could add more specific instructions for a user 
def main():
    print("Hi Welcome to my cell autonma project!")
    print("If you don't know how this works link to a useful rule video: https://www.youtube.com/watch?v=M_pkidxeGMY")
    n_cells = int(input("Number of cells: ")) # Imagine a linear array of cells, each representing a discrete position.
# The automaton evolves over generations, where each generation corresponds to a new configuration of cell states.
    n_generations = int(input("Number of generations: ")) 
    rule = int(input("Rule number: ")) # 256 possible patterns 
    rule = generate_rule(rule)
    initial_state = initialize(n_cells, n_generations, rule)

if __name__ == '__main__':
    main()



