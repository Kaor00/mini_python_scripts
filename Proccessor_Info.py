import psutil


print(f"Physical cores: {psutil.cpu_count(logical=False)}")
print(f"Total cores: {psutil.cpu_count(logical=True)}")

cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}MHZ")
print(f"Min Frequency: {cpufreq.min:.2f}MHZ")
print(f"Current Frequency: {cpufreq.current:.2f}MHZ")

print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
