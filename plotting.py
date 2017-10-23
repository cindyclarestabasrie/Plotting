import matplotlib.pyplot as plt
import math

trajectories = int(input("How many trajectories do you want to calculate? "))

# gravitational pull
g = 10

# starting time
second = 0

numbers = {}
results = {}

for i in range(1, trajectories+1):
    try:
        print("Velocity", i, ": ", end="")
        velocity = int(input())
        print("Angle", i, ": ", end="")
        angle = int(input())
        numbers["Velocity" + str(i)] = velocity
        numbers["Angle" + str(i)] = angle
        results["Distance" + str(i)] = []
        results["Motion" + str(i)] = []
    except:
        print("Error, please put integers.")

for j in range(1, trajectories+1):
    # Angle of number n trajectory will be taken from dictionary
    deg = math.degrees(numbers["Angle"+str(j)])
    # velocity of number n trajectory will be taken from dictionary
    velocity = numbers["Velocity"+str(j)]

    # time = (2 * initial velocity * sin( angle )) / g
    total_time = (2 * velocity * math.sin(deg)) / g

    # Vy0 = initial speed * sin degrees
    velocity_y = velocity * math.sin(deg)
    velocity_x = velocity * math.cos(deg)

    for i in range(1, trajectories+1):
        while float(second) < float(total_time):
            # x = velocity x * time
            results["Distance" + str(i)].append( velocity_x * second)
            # y = (velocity y * time - 0.5 * gravity * time ** 2
            results["Motion" + str(i)].append( velocity_y * second - 0.5 * g * second ** 2)
            # it will caculate for every 0.01 second and make a smooth parabola curve
            second += 0.01
i = 1
while i < trajectories:
    plt.plot(results["Distance" + str(i)], results["Motion" + str(i)])
    i += 1
plt.xlabel("Distance x")
plt.ylabel("Distance y")

plt.show()
