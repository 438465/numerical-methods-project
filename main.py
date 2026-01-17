import numpy as np
import matplotlib.pyplot as plt

# Parameters
beta = 1.2   # viral spread rate
gamma = 0.4  # forgetting rate

# Time settings
dt = 0.01
t_end = 20
t = np.arange(0, t_end + dt, dt)

# Arrays
S = np.zeros(len(t))
I = np.zeros(len(t))
R = np.zeros(len(t))

# Initial conditions (S + I + R = 1)
S[0] = 0.99
I[0] = 0.01
R[0] = 0.0

# Euler method
for n in range(len(t) - 1):
    dS = -beta * S[n] * I[n]
    dI = beta * S[n] * I[n] - gamma * I[n]
    dR = gamma * I[n]

    S[n + 1] = S[n] + dt * dS
    I[n + 1] = I[n] + dt * dI
    R[n + 1] = R[n] + dt * dR

# Plot
plt.plot(t, S, label="S")
plt.plot(t, I, label="I")
plt.plot(t, R, label="R")
plt.xlabel("Time")
plt.ylabel("Fraction of population")
plt.title("SIR Model - Euler Method")
plt.legend()
plt.grid(True)
plt.show()
