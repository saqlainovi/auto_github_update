import os
import datetime
import random
import time

def make_commit():
    # Get current date
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    # Create or update the commit file
    with open('commit_log.txt', 'a') as f:
        f.write(f'Auto commit on {date}\n')
    
    # Git commands
    os.system('git add .')
    os.system(f'git commit -m "Auto commit {date}"')
    os.system('git push')

if __name__ == "__main__":
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Make a commit
    make_commit() 