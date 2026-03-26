import projectilemotion

v_initial = 20.0
theta_initial = 11.0

distance, height = projectilemotion.projectilemotion_solver(v_initial, theta_initial)

print("A long jumper leaves the ground at an angle of 20.0° above the horizontal and at a speed of 11.0 m/s. ")

print(f"(a) Horizontal Distance: {distance:.2f} meters")
print(f"Maximum Height: {height:.2f} meters")   




