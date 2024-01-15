# Jan 15: Week 4: Problems I encountered while developing the script:

In this last section of my blog, I will be talking about two more problems I encountered during the development of my script and how I solved these problems. 

# Problem 3: Figuring out how to safely test my python script:
A new challenge presented itself as I made progress with my automation project: The process of running a Python script from the command line. Navigating the Ubuntu terminal and executing scripts can be daunting for beginners like myself, but armed with determination and a bit of guidance, I discovered a solution that I would share with as you read on. 

Running a Python script involves understanding the intricacies of the compiler or in my case, the (Ubuntu) terminal which involves navigating directories, setting execution permissions, and invoking the Python interpreter. Initially, this seemed very overwhelming for me, but with practice, proper research, the right tools and a step-by-step approach, the process becomes more manageable.

**The Solution:** 
After a lot of reasearch I discovered that a text editor was what I needed. I always use vim text editor when it comes to editing a file. I never knew it could be used to run a python script. I didn't really know how to do this but I knew where to get my solutions from. Can you guess?... Chatgpt of course! If you guessed chatgpt, you guessed right. 
I will share my chatgpt prompt and the answer it gave me.

```
Me: "I'm having trouble running a Python script on Ubuntu using Vim. Can you guide me through the process?"

ChatGPT: "Certainly! After editing your script in Vim, make sure to save and exit. Then, set execution permissions using chmod +x. Finally, run the script with python3 script.py."
```

Incase you have never used vim, here's a step-by-step process you can follow:

**Step 1: Install Vim:**
If Vim is not already installed, you can install it using the following command:
```
sudo apt-get update
sudo apt-get install vim
```

**Step 2: Open Vim:**
Use Vim to create and edit your Python script. For example, to create a script named monitor.py, you can run:
```
vim monitor.py
```
This opens the Vim text editor, allowing you to input and edit your Python script.

**Step 3: Writing the Python Script in Vim:**
Press i to Enter Insert Mode:
Vim has different modes, and pressing i allows you to start inserting text.

Write Your Python Script:
Input your Python script into Vim. Once done, press Esc to exit Insert Mode.

Save and Exit Vim:
Save your changes by typing :w and pressing Enter. To exit Vim, type :q and press Enter. If you've made changes, you can combine both commands by typing ':wq'.

**Step 4: Setting Execution Permissions:**
**Navigate to the Script Directory:**
Use the 'cd' command to change into the directory where your Python script is located.
```
cd path/to/your/script
```

**Set Execution Permissions:**
Ensure your script has execution permissions. Use the 'chmod' command:
```
chmod +x monitor.py
```

**Step 5: Executing the Script:**
**Run the Script:** 
Finally, execute your Python script using the Python interpreter. In the terminal, type:
```
python3 monitor.py
```

In conclusion, navigating the Ubuntu terminal and running Python scripts with Vim may seem daunting initially, but with practice and guidance, it becomes a valuable skill. Leveraging the capabilities of Vim and seeking assistance from tools like ChatGPT opens up a world of possibilities, empowering you to script with confidence


# Problem 4: Crafting Readable Python Scripts:
The significance of writing clean, organized, and readable scripts cannot be overstated. Recently, as I tackled an automation task with Python, I found myself facing the common challenge of script organization. The need to structure my code in a way that promotes clarity and readability was paramount, and with the help of ChatGPT, I discovered an approach that significantly improved the overall organization of my script.

When confronted with a task as intricate as automation, the temptation to quickly draft a script without much consideration for structure can be strong. However, the result is often a tangled web of code that is difficult to understand, maintain, and debug. Recognizing this, I embarked on a mission to organize my script in a way that would make it comprehensible to both present and future collaborators.

In my pursuit of script organization, I turned to ChatGPT for guidance on best practices. The importance of clear function and variable naming, modularization, and adherence became apparent. Below is my prompt and answer:

```
Me: "I'm struggling with organizing my Python script. Any advice on best practices?"

ChatGPT: "Consider breaking down your script into functions, each serving a specific purpose. Use meaningful names for functions and variables. Also, follow the PEP 8 style guide for consistency."
```

Heres a sample of my initial script:
```
import psutil
import speedtest
import time

def monitor():
    c = psutil.cpu_percent(interval=1)
    m = psutil.virtual_memory().percent
    st = speedtest.Speedtest()
    d = st.download() / 10**6
    u = st.upload() / 10**6
    print(f"CPU Usage: {c}% | Memory Usage: {m}%")
    print(f"Download Speed: {d:.2f} Mbps | Upload Speed: {u:.2f} Mbps")

while True:
    monitor()
    time.sleep(5)
```

After applying the advice from ChatGPT and incorporating best practices, the script evolved into a more structured and readable form:
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

**The Transformation:**
**Modular Functions:**
Functions were introduced to encapsulate specific functionalities, making the code more modular.

**Descriptive Naming:**
Descriptive names were chosen for functions and variables, providing clarity on their roles.

**Main Function:**
The main functionality was encapsulated within the monitor_and_output function, making it more organized and easy to follow.

**Script Entrypoint:**
The if __name__ == "__main__": block was included to ensure that the script runs only when executed directly, not when imported as a module.

In conclusion, the journey to organize my Python script taught me valuable lessons in code structure and readability. With a combination of best practices and guidance from ChatGPT, the transformation was significant. The resulting script not only functions effectively but is also a testament to the importance of clear organization in facilitating collaboration and maintainability. 

I hope these problem and solution blogs were helpful. If you have read my blog from beginning to this moment, I really do appreciate. If you haven't or you started from this blog, I advice you read the others as they are all connected. Below, I have attached the link to my other blogs.

## [Blog on Health benefits of video gaming](README.md)
## [Automation_blog1](Automation_0.1.md)
## [Automation_blog2](Automation_0.2.md)
## [Automation_blog3](Automation_0.3.md)
