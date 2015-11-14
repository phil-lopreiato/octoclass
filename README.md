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
```
./download-assignment.sh <GitHub username> <GitHub Classroom Organization> <GH Classroom Assignent prefix> <Deadline as YYYY-MM-DDTHH:MM:SS> <git tag name>

```

Running `list-repos.py` will print out one git url (SSH) per line of all repos within the given organization whose names start with the given phrase. This output is meant to be piped to `xargs` to do stuff with

## Putting it all together
To download all assignments from the `GWU-CSCI2113-F15` Organization prefixed with `zombie` and tag all commits before `11/14/2015` with the git tag `part1`, run the following:
```
./download-assignment.sh phil-lopreiato GWU-CSCI2113-F15 zombie 2015-11-14T00:00:00 part1
```
