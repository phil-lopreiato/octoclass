#! /usr/bin/env python

import argparse
import os.path
import github3
from github3.auths import Authorization
from github3 import authorize
from getpass import getpass

CREDENTIALS_FILE = "github_token.json"


def twofac_callback():
    prompt_str = "Enter 2fa pass: "
    try:
        token = raw_input(prompt_str)
    except NameError:
        token = input(prompt_str)
    return token


def get_gh_token(args):
    user = args.user
    password = ''

    while not password:
        password = getpass('Password for {}: '.format(user))

    note = "Github Classroom Repo Downloader"
    note_url = "http://classroom.github.com"
    scopes = ['user', 'repo']

    auth = authorize(user, password, scopes, note, note_url, two_factor_callback=twofac_callback)

    with open(CREDENTIALS_FILE, 'w') as fd:
        fd.write(auth.as_json())

    return auth


def get_repo_list(args, gh):
    org = gh.organization(args.org)
    repos = org.repositories()
    count = 0
    for repo in repos:
        if not repo.name.startswith(args.repo_prefix):
            # Ignore repos without proper prefix
            # So you can filter only repos from a single GH Classroom Assignment
            continue
        print('{0.git_url} {0.pushed_at}'.format(repo))
        count = count + 1


def load_gh_auth():
    with open(CREDENTIALS_FILE, 'r') as fd:
        data = fd.read()
        return Authorization.from_json(data)
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user", help="Github Username to auth with")
    parser.add_argument("org", help="Name of GitHub organization to query")
    parser.add_argument("repo_prefix", help="Prefix for repos to clone")
    args = parser.parse_args()

    if os.path.isfile(CREDENTIALS_FILE):
        auth = load_gh_auth()
    else:
        auth = get_gh_token(args)

    gh = github3.login(token=auth.token)
    get_repo_list(args, gh)
