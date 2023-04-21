Import math

C = 300000000 # speed of light in m/s

Mass = int(input(“Enter mass (in kilograms): “))
Energy = mass * math.pow(c, 2)

Print(“The equivalent energy is:”, int(energy), “Joules”)

