from github import GithubPull
from test_counter import TestCounter

counter = TestCounter()
gitpull = GithubPull()

gitpull.pull_changes()
counter.count_occurrences()
