#!/bin/bash

# Given big files from
# https://stackoverflow.com/questions/2100907/how-to-remove-delete-a-large-file-from-commit-history-in-git-repository
# git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | sed -n 's/^blob //p' | sort --numeric-sort --key=2
# list the bad file names and identify branches, remove those branches to keep
# repo size small
# E.g
# 7bc356af13559b913f9593133ebed9fa6253fb0f 659456 exercises/jobs/jobs.db
# c74ec1cbec3cf88681fb101d28ad36e57481f08e 757760 exercises/ex10/job_github.db
# 15ffb3201b555409381fb4ebf0fcb70389fa8888 419953550 ex_5_4.txt
# fba0487ae4effba0149fe393758e5a040fba848f 597222229 tenfile

for badfile in ex_5_4 exercises/ex10/job_github.db exercises/jobs/jobs.db; do
    echo $badfile
    echo "Here is the commit"
    commit=$(git log --all --pretty=format:%H -- $badfile | xargs -n1 -I% sh -c "git ls-tree % -- $badfile | grep -q $badfile && echo %")
    branch=$(git branch -r --contains $commit)
    echo "Branches contains the commit: "
    echo $branch
    echo
done
