# GitHub for Classroom Clone

## Dependencies
[github3.py](https://github.com/sigmavirus24/github3.py)

## Usage
```
 ./list-repos.py -h
usage: list-repos.py [-h] user org repo_prefix

positional arguments:
  user         Github Username to auth with
  org          Name of GitHub organization to query
  repo_prefix  Prefix for repos to clone

optional arguments:
  -h, --help   show this help message and exit
```

Running `list-repos.py` will print out one git url (SSH) per line of all repos within the given organization whose names start with the given phrase. This output is meant to be piped to `xargs` to do stuff with
