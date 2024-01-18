# Jan 1: Week_2: Explanation of the script:

This blog includes the explanation of my automation script. Its important you read it as it will give you a full understanding of the script and would help you modify it to suit your needs.

I will explain the script in groups or lines to ease understanding. So, let's go through the script group by group:

# Group 1
```
import psutil
import speedtest
import time
```
These lines import the necessary libraries needed to ensure the code runs properly. 

The **psutil** library provides an interface to retrieve system utilization information, like CPU, memory, disk, and network usage. It makes the process of monitoring and interacting with system resources easier and it also offers functions to gather real-time data on processes and system performance. You can access vital information about a system's state, enable efficient resource management and automate system-related tasks with psutil.

The **speedtest** library in Python facilitates network speed testing by connecting to Speedtest.net servers. It measures download and upload speeds, aiding in assessing internet connection performance. The library enables coders to integrate network speed tests into their applications. This can be valuable for diagnosing connection issues and optimizing network-related processes.

The **time** library is a module that provides functions to manipulate time, measure elapsed time, and create delays in code execution. Basically, it can be used to create time intervals.

# Group 2
```
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)
```

This defines a function **get_cpu_usage** that uses the psutil library to measure CPU usage percentage. The interval parameter is set to 1, meaning the CPU usage will be measured over a 1-second interval.

# Group 3
```
def get_memory_usage():
    return psutil.virtual_memory().percent
```

This defines a function **get_memory_usage** to retrieve the percentage of used virtual memory using psutil.

# Group 4
```
def get_network_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  
    upload_speed = st.upload() / 10**6 
    return download_speed, upload_speed
```

This defines a function **get_network_speed** that uses the speedtest library to measure download and upload speeds in megabits per second (Mbps). The **download_speed** and **upload_speed** contains a formula that converts the download and upload speed to Mbps.

# Group 5
```
def monitor_and_output():
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()

        download_speed, upload_speed = get_network_speed()

        print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")
        print(f"Download Speed: {download_speed:.2f} Mbps | Upload Speed: {upload_speed:.2f} Mbps")

        time.sleep(5)
```

The def function defines the main function **monitor_and_output**. It contains an infinite loop (while True) to continuously monitor and output system and network information. Inside the loop:
- CPU and memory usage are obtained using the previously defined functions.
- Network speed is measured using the get_network_speed function.
- The information is then printed to the console, displaying CPU and memory usage percentages, 
  as well as download and upload speeds in Mbps.
- There is a 5-second delay (time.sleep(5)) at the end of each iteration to control the 
  monitoring interval. You can adjust this value based on how often you want to collect data.

# Group 6
```
if __name__ == "__main__":
    monitor_and_output()
```

This block ensures that the **monitor_and_output** function is executed only if the script is run as the main program (not imported as a module).

In conclusion, this Python script uses the psutil and speedtest libraries to monitor CPU and memory usage, as well as download and upload speeds. The **monitor_and_output** function continuously collects and prints this information in an infinite loop with a specified interval.

In my next two blogs I would talk about the problems I faced while trying to develop the script and how I figured it out. Hopefully, they would provide solutions to problems you may face. The link is below

## [3rd_Automation](Automation_0.3.md)
