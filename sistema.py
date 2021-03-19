import psutil
print(psutil.cpu_times()) 
print(psutil.cpu_percent(1)) 
print("Number of cores in system", psutil.cpu_count()) 
print("\nNumber of physical cores in system",) 
print("CPU Statistics", psutil.cpu_stats()) 
print(psutil.virtual_memory()) 
print(psutil.swap_memory()) 
print(psutil.disk_usage('/')) 

print(psutil.sensors_fans()) 