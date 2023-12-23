# Dec 23: Week_1: Script Explanation

My blog will be divided into 4 parts and I will be adding a link to the next automation blog at the end of each blog. Please, feel free to contribute to my blog, by doing so, we can improve the script and share ideas on how to make it better. Also let me know if you encounter any problems while running the script.

My first blog provides a proper explanation of the script and how to run it properly. 

# INTRODUCTION:
Have you ever wondered how much of your computer's processing power is being used or how quickly it's communicating with the internet while gaming? These are crucial questions a gamer should always ask, especially gamers that play games like Call of duty and other games that require stable internet connection to peek perfomance.

My Python script provides a straight forward answer to these questions. Its important to note that this script can also be used by non-gamers that need constant information regarding their computer performance and internet speed. Lets get right into it.

# FULL SCRIPT:
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

# HOW TO PROPERLY RUN THE SCRIPT:
After a lot of trial and error in trying to figure out how to run the script properly which I will share on my other blogs, I was finally able to figure out how to run it properly. I will explain it in steps to ease understanding.

# Step 1: Command line
First, a **command line (cli)** is needed to run the code. In my case, I used Ubuntu through WSL on windows, because of these my commands would be mostly based on Ubuntu but it could also be similar to other command line commands. 

# Step 2: Create a new file and a virtual environment
Create a new directory on your cli.
```
mkdir my_directory
```
Change 'my_directory' to whatever name you want.

In the new directory, create a virtual environment. Using a virtual environment in Ubuntu allows you to create isolated Python environments for your projects, each with its own set of dependencies. This helps prevent conflicts between different projects that might require different package versions.
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

# Step 3:
The tools required to run a code properly is **psutil and speedtest-cli**. 
**psutil** is a python library that allows us to access information about system utilization, including CPU and memory usage. 
On the other hand, **speedtest-cli** is also a python library that we can use to perform internet speed tests, measuring both download and upload speeds.

