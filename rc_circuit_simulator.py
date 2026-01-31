
import numpy as np
import matplotlib.pyplot as plt


R = 1000          # Resistance
C = 0.000001      # capacitance
V_initial = 5     # voltage (5V)


time = np.linspace(0, 0.01, 1000)
Vc = V_initial * np.exp(-time / (R * C))

plt.plot(time, Vc)

plt.title("RC Circuit Discharging Curve")
plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (Volts)")
plt.grid(True)
plt.show()