#!/usr/bin/env python


import subprocess as spr
import itertools


def files_changed(sha='origin/master', prefix='exercises/'):
    cmd = ['git', 'diff', '--name-only', '{}...HEAD'.format(sha)]
    process = spr.run(cmd, stdout=spr.PIPE)
    diff = process.stdout.decode('utf-8').splitlines()
    print("Files changed: ", " ".join(diff))
    return [fn for fn in diff
            if fn.startswith(prefix) and fn.endswith('.py')]


def ex_identifier(path):
    # 'exercises/ex3_0.py' -> ex3
    return path.split('/')[1].split('_')[0]


def exercise_groups(changed_files):
    return dict(itertools.groupby(
        changed_files,
        ex_identifier,
    )).keys()


if __name__ == "__main__":
    groups = exercise_groups(files_changed())
    print('Exercises groups to test: ', ', '.join(groups))
    results = []
    for group in groups:
        cmd = ['python3', '-m', 'unittest',
               'tests.test_{}'.format(group), '-vvv']
        p = spr.run(cmd, stdout=spr.PIPE, stderr=spr.PIPE)
        print("Result of test for {}".format(group))
        print(p.stderr.decode('utf-8'))
        print(p.stdout.decode('utf-8'))
        print('*' * 20)
        results.append(p.returncode)

    if all(map(lambda x: x == 0, results)) is True:
        exit(0)
    else:
        exit(1)
