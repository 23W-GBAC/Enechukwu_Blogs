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
