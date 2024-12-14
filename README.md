# Auto GitHub Contribution Updater

This script automatically creates daily commits to keep your GitHub contribution graph active.

## Setup Instructions

1. Clone this repository
2. Make sure you have Python installed
3. Initialize git in this directory:
   ```bash
   git init
   git remote add origin https://github.com/saqlainovi/auto_github_update.git
   ```
4. Set up a scheduled task (Windows) or cron job (Linux/Mac) to run the script daily

### Windows Task Scheduler Setup:
1. Open Task Scheduler
2. Create a new Basic Task
3. Set trigger to daily
4. Action: Start a program
5. Program/script: python
6. Arguments: path_to_script/auto_commit.py

Remember to first commit and push this repository manually:
```bash
git add .
git commit -m "Initial commit"
git push -u origin main
``` 