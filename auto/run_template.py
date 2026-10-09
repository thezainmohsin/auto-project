import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 0.5
K_I = 0.14
K_D = 0.18

STEPS = 550

car = make_car(desired_v=20.0, dt=0.1)

times = []
velocities = []
errors = []
frictions = []

for step in range(STEPS):
    # Base friction is 2.0
    # Introduce a high friction patch (4.0) between steps 250 and 400
    if 250 <= step <= 400:
        current_friction = 4.0
    else:
        current_friction = 2.0
    
    accel, error = calculate_desired_acceleration(car, K_P, K_I, K_D) #calculating desired acceleration and error
    throttle = acceleration_to_throttle_percentage(accel) #calculating throttle percentage
    
    # Pass the dynamic friction into the update call
    update(car, throttle, friction=current_friction) #updating car state

    times.append(car["t"]) # Appending time to times list
    velocities.append(car["v"]) # Appending velocity to velocities list
    errors.append(error) # Appending error to errors list
    #frictions.append(current_friction) # Appending friction to frictions list

# Create 1 row, 2 columns of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

# Left plot: Velocity vs Time
ax1.plot(times, velocities)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Velocity (m/s)")
ax1.set_title("Velocity vs Time")
ax1.axhline(y=20, color="r", linestyle="--")

# Right plot: Error vs Time
ax2.plot(times, errors)
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Error (m/s)")
ax2.set_title("Error vs Time")
ax2.axhline(y=0, color="g", linestyle="--")

# Adjust spacing so labels don't overlap, then display
plt.tight_layout()
plt.show()