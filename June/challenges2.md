# Monthly programming challenges for the study.py group. June edition.

Hello everybody!

It was nice seeing people participate in last month's challenges. Looking back at the results, we had the most people participating in the beginner challenges. A few in the web scraping segment, and only one in the data task.

Drawing feedback from that, I'll try to keep this month's tasks more beginner friendly, short, and precisely formulated.

Here are the challenges for June:

## 1. [DateTime] The final Countdown

Handling dates and time data in python is an essential skill. Python has multiple standard and additional libraries that support it. Here we are going to develop a fun little program to learn the basics.

**Problem:**

You got an important event in the future, that you can't forget. Pick an event that you'd like to target (your dogs birthday, the next superbowl, in my case the deadline for my master thesis). Write a python program, that when called will print the remaining time till that event. It should print:

1. The remaining weeks (plus leftover days)
2. The remaining days
3. The remaining working days (Mo - Fr)
4. The remaining absolute time (days:hours:mins:secs)

**Bonus:**

1. Find a way to let the program run and update continuously (ideas: updated command line, gui clock).
2. Let the program show the time that has passed since the first execution.



## 2. [StringValidation] AutoFill-Forms

A lot of you guys are aspiring WebDevs. Everyone knows the registration pages of websites, requiring you to input an E-Mail adress, a password and additional personal information. Today we look at how to validate inputs from them.

**Problem:** On online registration pages, you often want to have a text-field where the user inputs his/her E-Mail adress. Write a python function to check, whether the E-Mail (input string) is valid. The rules for a valid E-Mail adress are:

1. Contains a <kbd>@</kbd>-character.
2. Contains at least 1 character before the <kbd>@</kbd>.
3. Contains at least 1 <kbd>.</kbd>-character.
4. The <kbd>.</kbd> has to be in the correct place. (e.g. dalai-lama.email@com is invalid, dalai.lama@email.com is valid)

Addinally: Look up common trash-mail suppliers. Try to pass their domains (e.g. 1234@trash-mail.com) as invalid, because you're an evil company and want all of your user's data.

**Bonus:** Try to think of rules for address / name / phone number validation and write functions for them. Let the user of your program chose what type of string to check for by specifying command line arguments (e.g. `python checker.py 'main street 123' --address`)


## 3. [Automation] Auto-Remove

Assuming you're a person who doesn't clean his pc very much, you probably would look for a way to tidy it up in one click. Also assuming you don't care too much about backing up and security, you decide to write a python script that deletes old files.

**Problem:** Your whole desktop is littered in files of which you don't even know anymore what they are. Going for the radical way to tidy up your desktop you write a program, that:

1. Searches for files older than two years.
2. Moves them into a newly created 'to_be_deleted' folder.
3. Asks for confimation if the files should really be deleted
4. Deletes them if confirmed.

Be cautious to **only use one folder** for this program, and only use data that you can afford losing. 

**Bonus:** After the operation, show to the user how much disk space was freed up and how many files were deleted. Also look for a way to implement data-recovery.

---------

Happy Coding!
