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

**Writing the Python Script in Vim:**
Press i to Enter Insert Mode:
Vim has different modes, and pressing i allows you to start inserting text.

Write Your Python Script:
Input your Python script into Vim. Once done, press Esc to exit Insert Mode.

Save and Exit Vim:
Save your changes by typing :w and pressing Enter. To exit Vim, type :q and press Enter. If you've made changes, you can combine both commands by typing :wq.

**Setting Execution Permissions:**
