import sys
import os

def push_repo_with_comments(comments):
    """
    Example usage:
    python git_push.py "Added new files and updated README"
    """
    # Print initial git status
    os.system('git status')
    input('Press any key to continue...')
    
    # Remove any .DS_Store files
    os.system('find . -name ".DS_Store" -type f -delete')
    
    # Print updated git status
    os.system('git status')
    input('Press any key to continue...')
    
    # Add all changes
    os.system('git add .')
    
    # Print updated git status
    os.system('git status')
    input('Press any key to continue...')
    
    # Commit changes with comments
    os.system(f'git commit -m "{comments}"')
    
    # Print updated git status
    os.system('git status')
    input('Press any key to continue...')
    
    # Push changes to remote repo
    os.system('git push')

if __name__ == '__main__':
    # Get comments from command-line argument
    comments = ' '.join(sys.argv[1:])
    
    # Call push_repo_with_comments with comments argument
    push_repo_with_comments(comments)
