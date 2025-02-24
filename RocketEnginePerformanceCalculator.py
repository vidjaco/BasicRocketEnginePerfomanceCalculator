# Rocket Engine Perfomance Calculator

print("Rocket Engine Perfomance Calculator")
thurst = float(input("What is the Rocket engine thrust? "))
mass_flow = float(input("What is the Rocket engine mass flow rate the propellant? "))
specific_impulse = thurst / (mass_flow * 9.81)
exhaust_velocity = specific_impulse * 9.81
print("Specific Impulse: " + str(specific_impulse)) 
print("Exhaust Velocity: " + str(exhaust_velocity)) 


