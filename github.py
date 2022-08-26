import os


class GithubPull:
    def __init__(self):
        self.root_dict = {
            1: "<root_project_path>",
            2: "<root_project_path>",
            # delete this comment and  add as many key values as you need

        }

    def pull_changes(self):
        length = len(self.root_dict) + 1
        for i in range(1, length):
            os.chdir(self.root_dict.get(i))
            os.popen('git pull')
