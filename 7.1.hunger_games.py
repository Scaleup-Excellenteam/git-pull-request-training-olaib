import matplotlib.pyplot as plt
import random

# Define the vertices of the triangle
VERTICES = [(0, 0), (2, 2), (4, 0)]


def plot_walks(num_steps):
     """
     Katniss Everdeen is walking in a triangle with vertices at (0,0), (2,2), and (4,0).
     She starts at a random vertex and takes num_steps steps.
     At each step, she chooses a random vertex and walks halfway to it.
     This function plots the path she takes.
     Blue dots are the midpoints between the current location and the chosen vertex.
     Red dots are the vertices.
     :param num_steps: number of steps to take in the walk
     :return:
     """
     # Initialize the plot
     fig, ax = plt.subplots()
     # Limits of the plot
     ax.set_xlim([-0.5, 4.5])
     ax.set_ylim([-0.5, 3.5])
     # Initialize the current location to a random vertex
     current_location = random.choice(VERTICES)

     # Plot the starting location
     ax.scatter(current_location[0], current_location[1], color='red', s=100)
     # ========================== WALK ====================== ====
     # walk num_steps times
     for i in range(num_steps):
         # choose a rand vertex
         chosen_vertex = random.choice(VERTICES)
         # calculate the midpoint between the current location and the chosen vertex
         midpoint = ((current_location[0] + chosen_vertex[0]) / 2,
                     (current_location[1] + chosen_vertex[1]) / 2)
         # plot the midpoint
         ax.scatter(midpoint[0], midpoint[1], color='blue')
         # update the current location
         current_location = midpoint
     # Show the plot
     plt.show()


if __name__ == '__main__':
     plot_walks(5)