# Jan 1: Week_2: Explanation of the script:
This blog will include the explanation of my automation script. Its important you read it as it will give you a full understanding of the script and would help you modify it to suit your needs.

I will explain the script in groups or lines to ease understanding. So, let's go through the code line by line:

```
import psutil
import speedtest
import time
```
These lines import the necessary libraries needed to ensure the code runs properly. 

The **psutil** library provides an interface to retrieve system utilization information, like CPU, memory, disk, and network usage. It makes the process of monitoring and interacting with system resources easier and it also offers functions to gather real-time data on processes and system performance. You can access vital information about a system's state, enable efficient resource management and automate system-related tasks with psutil.
