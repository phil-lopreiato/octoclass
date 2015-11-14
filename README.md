# GitHub for Classroom Clone

## Dependencies
 - [github3.py](https://github.com/sigmavirus24/github3.py)
 - [gitpython](https://github.com/gitpython-developers/GitPython)

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
```
./clone-and-check.py -h
usage: clone-and-check.py [-h] url timestamp tag

positional arguments:
  url         Git url to clone
  timestamp   Deadline timestamp in format YYYY-MM-DDTHH:MM:SS (eastern time)
  tag         Tag to mark the latest valid commit

optional arguments:
  -h, --help  show this help message and exit

```

Running `list-repos.py` will print out one git url (SSH) per line of all repos within the given organization whose names start with the given phrase. This output is meant to be piped to `xargs` to do stuff with
