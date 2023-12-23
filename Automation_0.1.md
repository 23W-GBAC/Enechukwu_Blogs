# Dec 23: Week_1: Script Explanation

My blog will be divided into 4 parts and I will be adding a link to the next automation blog at the end of each blog. Please, feel free to contribute to my blog, by doing so, we can improve the script and share ideas on how to make it better. Also let me know if you encounter any problems while running the script.

My first blog provides a proper explanation of the script and how to run it properly. 

# Introdution:
Have you ever wondered how much of your computer's processing power is being used or how quickly it's communicating with the internet while gaming? These are crucial questions a gamer should always ask, especially gamers that play games like Call of duty and other games that require stable internet connection to peek perfomance.

My Python script provides a straight forward answer to these questions. Its important to note that this script can also be used by non-gamers that need constant information regarding their computer performance and internet speed. Lets get right into it.

# Full Script:
**Note:** Please do not run the script until you have read how to run it.

'''python
import psutil
import speedtest
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_network_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps
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
    monitor_and_output() '

# How to proper run the script:
