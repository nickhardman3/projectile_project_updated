import matplotlib.pyplot as plt

def plot_xy(x_positions, y_positions):
    plt.plot(x_positions, y_positions) #adds the values in the lists into the function so they can be plotted in a graph
    plt.title("Projectile Motion")
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.show() 
