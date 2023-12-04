

import matplotlib.pyplot as plt
from numpy import sign

 

def update_state(t, x, v, a, dt=0.1):
    distance_moved = v*dt + (1/2)*a*(dt**2)
    v += a*dt
    t += dt

    x += distance_moved
    
    return t, x, v

def calculate_acceleration_y(v, k=0.0, mass=1.0, gravity=-9.81):
 
    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_gravity + force_air
    a = total_force/mass
    
    return a   #calculates the acceleration in teh y axis


def calculate_acceleration_x(v, k=0.0, mass=1.0):
    
    force_gravity = mass
    force_air = -sign(v)*k*v**2
    total_force = force_gravity + force_air
    a = total_force/mass
    
    return a   #calculates the acceleration in the x axis (without gravity factor)

def flying_mass(initial_x, initial_y, x_velocity=0.0, y_velocity=0.0, k=0.0, mass=1.0, dt=0.1):

    gravity = -9.81  # m/s^2

 
    x_position, y_position = initial_x, initial_y
    x_vel, y_vel = x_velocity, y_velocity
    t = 0.0


    time = []
    x_positions = []
    y_positions = []
    x_velocities = []
    y_velocities = [] #creates empty lists for values needed for plotting to go into 

    
    while y_position > 0:
        
        x_acceleration = calculate_acceleration_x(x_vel, k=k, mass=mass)
        y_acceleration = calculate_acceleration_y(y_vel, k=k, mass=mass, gravity=gravity)
 #calculates the acceleration in the x and y axis of the mass given in the funtion
        time.append(t) 
        x_positions.append(x_position)
        y_positions.append(y_position) #adds the position of the mass to the lists
        x_velocities.append(x_vel)
        y_velocities.append(y_vel) #adds the velocities of the mass to the lists

       
        t, x_position, x_vel = update_state(t, x_position, x_vel, x_acceleration, dt=dt)
        t, y_position, y_vel = update_state(t, y_position, y_vel, y_acceleration, dt=dt)
#updates the position, time, acceleration and velocity of the mass in both axis so the code can be looped with the updated values

    
    return time, x_positions, y_positions, x_velocities, y_velocities

#hello
