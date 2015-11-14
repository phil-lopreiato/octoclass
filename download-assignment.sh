#! /usr/bin/env sh

# Script to fetch all repos from the org
# Usage: ./download-assignment.sh <GitHub username> <GitHub Classroom Organization> <GH Classroom Assignent prefix> <Deadline as YYYY-MM-DDTHH:MM:SS> <git tag name>

GH_USER=$1
GH_ORG=$2
GH_REPO_PREFIX=$3
DEADLINE=$4
TAG_NAME=$5

./list-repos.py $GH_USER $GH_ORG $GH_REPO_PREFIX | xargs -n 1 sh -c "./clone-and-check.py \$0 $DEADLINE $TAG_NAME"
