# Jan 10: Week 3: Problems I encountered while developing the script:

In this blog and the next, I will be talking about problems I encountered while developing the script and how I solved these problems. I hope that by doing so, it would be helpful to you in case you come across these problems.

# Problem 1: Choosing the Right Libraries for the Python Automation:
Selecting the appropriate libraries is a crucial step that can significantly impact the success of a project on Python and I found myself facing a common dilemma: which libraries should I use?. 

The first challenge was identifying the key functionalities needed for my script. In my case, I required tools to monitor CPU usage, memory usage, and network speed. A quick search on google revealed multiple options, leaving me pondering over the trade-offs between various libraries. I needed something very simple but versatile and efficient because I'm not a very advanced python user yet. 

I decided to divide my searches into various categories to make it easier to find something simple and efficient as that was my target. My first search was regarding the **CPU and Memory monitoring**. I needed a library that could provide real-time information about CPU and memory usage. After some research and consideration, I opted for **psutil**. This versatile library proved to be a go-to choice for system monitoring, offering a simple and efficient way to access vital system statistics. It was also the first result on google. 

![image](https://github.com/23W-GBAC/Enechukwu_Blogs/assets/148862792/c99f93ce-67e9-48e8-817c-83dd6c9ae095)

My next search was for a library that could **test the network speed**. For network speed testing, my research led me to speedtest-cli. This library taps into the Speedtest.net infrastructure, allowing easy and accurate measurement of download and upload speeds. I also figure out how to properly use the library from this website- https://www.tutorialspoint.com/application-for-internet-speed-test-using-pyspeedtest-in-python#:~:text=Pyspeedtest%20is%20a%20Python%20library,of%20an%20internet%20connection%20programmatically

Before I came to a conclusion on the libraries, just for good measure, I quickly went to my very good friend Chatgpt for reassurance and validation of my choice. 
```
Me: "I'm working on a Python script to monitor PC performance and network connection. I'm using **psutil** for CPU and memory monitoring and **speedtest-cli** for network speed testing. Do you think these libraries are suitable?"

ChatGPT: "Using psutil for CPU and memory monitoring is a solid choice; it's widely used and reliable. Similarly, speedtest-cli is a convenient library for network speed testing. Your selections align well with your objectives."
```

For the **smtplib** library, I had already worked with this while I was learning how to code in python. It was the 1st library that came to mind when I needed a library that could send emails.

In conclusion, the collaboration with ChatGPT provided reassurance and validation for my library choices. It emphasized the importance of considering factors such as reliability, community support, and ease of use when making such decisions. I've come to appreciate the significance of a well-informed library selection. It not only streamlines development but also lays the foundation for a robust and efficient automation solution.

# Problem 2: Figuring out how to safely test my python script:
When running a new script or like in my case, a new script for automation for the first time, one of the paramount concerns is ensuring that your code is tested and run in a controlled environment, preventing any damage to your computer system. As I delved into developing a Python script for monitoring PC performance and network connection, the question of where and how to safely test my script became a critical consideration. I knew that there were risks involved in running this script because its a script that would interact with system resources and errors in this script could lead to unintended consequences, potentially impacting the stability and functionality of my computer. To address this, I sought a solution that would allow me to test my script in isolation, shielding my system from any adverse effects.

**The Solution:** 
After various considerations, I decided to run my script on Ubuntu. I chose Ubuntu because I'm familiar with the environment and commands. However, I had no idea on how to safely run my script in Ubuntu without any adverse effect. This is where chatgpt came in. I consulted ChatGPT to refine my approach and seek recommendations for best practices in testing Python scripts.
```
Me: "I'm working on a Python script, and I want to ensure that I can test it safely on Ubuntu without affecting my system. What are the best practices?"

ChatGPT: "Consider using a virtual environment to create an isolated space for your project. This way, you can install dependencies without interfering with your system's Python environment. It's a common practice in Python development."
```
Chatgpt also showed me how to run it and I will share it with you.
```
# Install virtualenv
sudo apt-get install python3-venv

# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate
```
This should be done in the directory you want to run the script in. The virtual environment helped me to isolate my script, ensuring that changes made during script execution were confined to the virtual environment. Also, it is easy to cleanup, you can deactivate and delete the virtual environment.

In conclusion, prioritizing safety in a script development process is essential. Virtual environments on Ubuntu, coupled with recommendations from ChatGPT, provided a robust solution for testing Python scripts securely.

In my next and final blog, I would be sharing more problems I encountered and the way I solved these problems. You can click on the link below to access it. See you there!

## [4th_Automation](Automation_0.4.md)
