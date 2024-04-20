import os
import random
import string
import time
from datetime import datetime, timedelta
from faker import Faker
from github import Github

# GitHub API access token
github_token = os.environ.get('GITHUB_TOKEN')
# Repository owner and name
repo_owner = 'prvnmali2017'
repo_name = 'temp_ai'

# Initialize Faker
faker = Faker()

# Generate random commit message
def generate_commit_message():
    return faker.sentence()

# Create a fake file with random data
def create_fake_file():
    filename = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.txt'
    with open(filename, 'w') as f:
        f.write(faker.text())
    return filename

# Create a commit with a fake file
def create_fake_commit():
    filename = create_fake_file()
    commit_message = generate_commit_message()
    os.system(f'git add {filename}')
    os.system(f'git commit -m "{commit_message}"')

# Create a pull request
def create_pull_request():
    g = Github(github_token)
    repo = g.get_user(repo_owner).get_repo(repo_name)
    branch_name = ''.join(random.choices(string.ascii_lowercase, k=10))
    repo.create_git_ref(ref=f'refs/heads/{branch_name}', sha=repo.get_branch('main').commit.sha)
    pull_request_title = generate_commit_message()
    pull_request_body = faker.paragraph()
    pull_request = repo.create_pull(title=pull_request_title, body=pull_request_body, base='main', head=branch_name)
    return pull_request

# Close a pull request
def close_pull_request(pull_request):
    pull_request.edit(state='closed')

# Main function
def main():
    while True:
        # Generate more commits on weekdays and fewer on weekends
        if datetime.now().weekday() < 5:
            for _ in range(random.randint(5, 10)):
                create_fake_commit()
        else:
            for _ in range(random.randint(1, 3)):
                create_fake_commit()

        # Create a pull request and close it after 10 minutes
        pull_request = create_pull_request()
        time.sleep(600)  # 10 minutes
        close_pull_request(pull_request)

if __name__ == "__main__":
    main()
