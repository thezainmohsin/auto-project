import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 0.5
K_I = 0.2
K_D = 0.11

STEPS = 550

car = make_car(desired_v=20.0, dt=0.1)

times = []
velocities = []
errors = []

for step in range(STEPS):
    accel, error = calculate_desired_acceleration(car, K_P, K_I, K_D)
    throttle = acceleration_to_throttle_percentage(accel)
    update(car, throttle)

    times.append(car["t"])
    velocities.append(car["v"])
    errors.append(error)

plt.plot(times, velocities)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity over Time")
plt.show()

plt.plot(times, errors)
plt.xlabel("Time (s)")
plt.ylabel("Error (m/s)")
plt.title("Error over Time")
plt.show()
