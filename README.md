# Monthly Challenges [study.py]

This is the repository for the monthly challenges. Here you can:

* See the challenges for every month
* Upload your solutions to tasks

## Folder Structure

There is a toplevel folder for each Month. Inside you can find subfolders for every challenge.

The solutions are stored inside the challenge folders.
Inside the monthly folder you can find the markdown document explaining the challenges.

* May/
  * 1_beginner/
    * `username1.py`
    * `username2.py`
  * 2_web_scraping/
    * `username1.py`
  * 3_data/
  * `challenges.md`

## How to submit solutions

Please name your python file as your Slack username. For me that would be `cripcate.py`.

### Via github.com

1. Navigate to a folder on your machine where you would like to store the repository.
3. Navigate into the folder for the correct month you're trying to submit to (e.g. `cd May`)
4. Navigate into the sub-folder for the correct challenge you're trying to submit to (e.g. `cd 1_beginner`)
5. Upload your python script into the folder: ![uploading](https://i.imgur.com/gbdCvKF.png)
6. Create a pull request: ![pull](https://i.imgur.com/0ngU8Wy.png)

### Via Terminal

1. Navigate to a folder on your machine where you would like to store the repository.
2. Clone the repository: `git clone https://github.com/py-study-group/challenges`.
3. Create a new branch and switch to it: `git branch xyz && git checkout xyz`
4. Navigate into the folder for the correct month you're trying to submit to (e.g. `cd May`)
5. Navigate into the sub-folder for the correct challenge you're trying to submit to (e.g. `cd 1_beginner`)
6. Copy your python script into the folder: `cp /path/to/script/[username].py .`
7. Add the file and commit the change: `git add [username].py` & `git commit -m "Added solution for challenge x by user y"`
8. Push the changes to the remote branch: `git push origin xyz`
9. Create a pull request: ![pull](https://i.imgur.com/0ngU8Wy.png)
