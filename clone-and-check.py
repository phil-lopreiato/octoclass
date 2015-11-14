#! /usr/bin/env python

import argparse
import datetime
import subprocess

from git import Repo
from pytz import timezone
from os.path import basename

"""
Clones and verifies timestamp on a single repo
Repo passed as first arg, timestamp as second
"""


# Clones the repo and return local path
def clone_repo(args):
    subprocess.call(["git", "clone", args.url])
    path = basename(args.url)[:-4]
    return path


# Traverse backwards until we've found a commit from before the deadline
def find_submit_commit(args, repo):
    deadline = datetime.datetime.strptime(args.timestamp, "%Y-%m-%dT%H:%M:%S")
    tz = timezone('US/Eastern')
    deadline = tz.localize(deadline)
    print "DEADLINE: {}".format(deadline)
    commit = Repo.rev_parse(repo, "HEAD")
    commit_time = datetime.datetime.fromtimestamp(commit.committed_date)
    commit_time = tz.localize(commit_time)
    while commit_time > deadline:
        parents = commit.parents
        if len(parents) == 0:
            # No more valid commits. No submission :(
            print "No valid commit found"
            return None
        commit = parents[0]
        commit_time = datetime.datetime.fromtimestamp(commit.committed_date)
        commit_time = tz.localize(commit_time)
        print "SUBMITTED: {}".format(commit_time)
    sha = commit.name_rev.split()[0]
    print "SUBMIT COMMIT: {}".format(sha)
    return sha


# Create a tag at the given sha with name passed in args
def create_tag(args, repo, sha):
    repo.create_tag(args.tag, sha)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Git url to clone")
    parser.add_argument("timestamp", help="Deadline timestamp in format YYYY-MM-DDTHH:MM:SS (eastern time)")
    parser.add_argument("tag", help="Tag to mark the latest valid commit")
    args = parser.parse_args()

    path = clone_repo(args)
    print "REPO: {}".format(path)
    repo = Repo(path)
    sha = find_submit_commit(args, repo)
    create_tag(args, repo, sha)
