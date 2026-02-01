import csv
import random
import matplotlib.pyplot as plt

times = []
temps = []
hums = []

filename = "data_log.csv"
try:
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Temperature", "Humidity"])

        for i in range(10):
            t = i
            temp = random.uniform(20, 30)
            hum = random.uniform(40, 60)

            writer.writerow([t, temp, hum])
            times.append(t)
            temps.append(temp)
            hums.append(hum)

    print("Data saved successfully.")

    plt.plot(times, temps, label="Temperature")
    plt.plot(times, hums, label="Humidity")
    plt.legend()
    plt.show()

except Exception:
    print("An error occurred while saving the file.")
