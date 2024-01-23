# Dec 23: Week_1: Introduction to my automation script and how to run it:

Have you ever wondered how much of your computer's processing power is being used or how quickly it's communicating with the internet while gaming? These are crucial questions a gamer should always ask, especially gamers that play games like Call of duty and other games that require a stable internet connection and peek perfomance.

My Python script provides a straight forward answer to these questions. Its important to note that this script can also be used by non-gamers that need constant information regarding their computer performance and internet speed. So!, lets get right into it.

Its important to know that my blog will be divided into four parts and I will be adding a link to the next automation blog at the end of each blog. Please, feel free to contribute to my blog, by doing so, we can improve the script and share ideas on how to make it better. Also let me know if you encounter any problems while running the script.

My first blog provides an introduction to my script and how to run it properly. Its important to note that the language used to run the script is python.

# FULL AUTOMATION SCRIPT AND EXPLANATION:
**Note:** Please do not run the script until you have read how to run it.

```
import psutil
import speedtest
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_network_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6
    upload_speed = st.upload() / 10**6
    return download_speed, upload_speed

def monitor_and_output():
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        
        download_speed, upload_speed = get_network_speed()
  
    print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")
    print(f"Download Speed: {download_speed:.2f} Mbps | Upload Speed: {upload_speed:.2f} Mbps")

     time.sleep(5)

if __name__ == "__main__":
    monitor_and_output()
```

I will explain the script in groups or lines to ease understanding. So, let's go through the script group by group:

# Group 1
```
import psutil
import speedtest
import time
```
These lines import the necessary libraries needed to ensure the code runs properly. 

The **psutil** library provides an interface to retrieve system utilization information, like CPU, memory, disk, and network usage.
The **speedtest** library in Python facilitates network speed testing by connecting to Speedtest.net servers. It measures download and upload speeds, aiding in assessing internet connection performance.
The **time** library is a module that provides functions to manipulate time, measure elapsed time, and create delays in code execution. 

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

In conclusion, this Python script uses the **psutil** and **speedtest** libraries to monitor CPU and memory usage, as well as download and upload speeds. The **monitor_and_output** function continuously collects and prints this information in an infinite loop with a specified interval.


# HOW TO PROPERLY RUN THE SCRIPT:
After a lot of trial and error in trying to figure out how to run the script properly which I will share on my other blogs, I was finally able to figure out how to run it properly. I will explain it in steps to ease understanding.

# Step 1: Command line
First, a **command line (cli)** is needed to run the code. In my case, I used Ubuntu through WSL on windows, because of these my commands would be mostly based on Ubuntu but it could also be similar to other command line commands. 

# Step 2: Create a new directory and a virtual environment
Create a new directory on your cli.
```
mkdir my_directory
```
Change 'my_directory' to any name you want.

In the new directory, create a virtual environment. Using a virtual environment in cli allows you to create isolated Python environments for your projects, each with its own set of dependencies. This helps prevent conflicts between different projects that might require different package versions.
Run the following commands to create a virtual environment:
```
cd my_directory
```
```
# Always update your cli (you're welcome)
sudo apt update
```
Install virtualenv if not already installed
```
sudo apt install python3-venv
```
Create a virtual environment named 'venv'
```
python3 -m venv venv
```

# Step 2: Activate the Virtual Environment
Activate the virtual environment by running the following command:
```
source venv/bin/activate
```

# Step 3: Install the required tools
The tools needed to run this code properly is **psutil and speedtest-cli**.

**psutil** is a python library that allows us to access information about system utilization, including CPU and memory usage. 

On the other hand, **speedtest-cli** is also a python library that we can use to perform internet speed tests, measuring both download and upload speeds.
Both tools can be installed using the following command:
```
pip install psutil speedtest-cli
```

# Step 4: Save the script in a file
The next step is to create a file (e.g., performance_script.py), copy and paste the Python script into it and save it.
You can create a file using the following command.
```
touch performance_script.py
```

Use the following command to open the file in vim text editor.
```
vim performance_script.py
```
You can also use nano and other text editors. Once you have opened the file, copy and paste the full script, then save and exit.

# Step 5: Run the Script
This is the final step. Once you've saved the script and exited, you can run it using the following command:
```
python performance_script.py
```

# HOW TO STOP RUNNING THE SCRIPT AND HOW TO DEACTIVATE THE VIRTUAL ENVIRONMENT:
Once you're done running the script, you can stop it using **ctrl+c** to stop running it. You can also deactivate the virtual environment by running the following command:
```
deactivate
```

On my next blog, I will be sharing the Cost-Benefit Analysis of My Automation Journey. You can access my next blog by clicking the link below.

## [2nd_Automation](Automation_0.2.md)
