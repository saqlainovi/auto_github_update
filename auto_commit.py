import os
import datetime
import subprocess
import sys

def run_git_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, f"Error executing {command}: {e.stderr}"

def make_commit():
    # Get current date
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    try:
        # Create or update the commit file
        with open('commit_log.txt', 'a') as f:
            f.write(f'Auto commit on {date}\n')
        
        # Git commands with error handling
        commands = [
            'git add .',
            f'git commit -m "Auto commit {date}"',
            'git push'
        ]
        
        for cmd in commands:
            success, output = run_git_command(cmd)
            if not success:
                print(f"Failed to execute git command: {output}")
                return False
            print(f"Successfully executed: {cmd}")
            print(output)
        
        return True
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    # Change to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if git is initialized
    success, output = run_git_command('git status')
    if not success:
        print("Git repository not initialized or git not installed")
        sys.exit(1)
    
    # Make a commit
    if make_commit():
        print("Auto commit completed successfully")
    else:
        print("Auto commit failed")
        sys.exit(1) 