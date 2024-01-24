import os
from github import Github

# Загружены скриншоты в репозиторий https://github.com/vsuet-237345/screenshots

token = '#######'
repo_name = 'screenshots'
repo_owner = 'vsuet-237345'
directory_path = '.'

def upload_photos_to_repo(directory, repo):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'rb') as file:
                content = file.read()
                repo.create_file(os.path.join(directory[len(directory_path):], filename), f"Add {filename}", content)


g = Github(token)
repo = g.get_user(repo_owner).get_repo(repo_name)

upload_photos_to_repo(directory_path, repo)
