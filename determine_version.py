import sys
import re

def determine_version_bump(commits):
    major_bump = re.compile(r'BREAKING CHANGE')
    minor_bump = re.compile(r'feat')
    patch_bump = re.compile(r'fix|chore|docs|style|refactor|perf|test')

    major = minor = patch = 0
    for commit in [a.strip() for a in commits[0].split('\n')]:
        if major_bump.search(commit):
            major += 1
        elif minor_bump.search(commit):
            minor += 1
        elif patch_bump.search(commit):
            patch += 1

    if major > 0:
        return 'major'
    elif minor > 0:
        return 'minor'
    elif patch > 0:
        return 'patch'
    else:
        return 'patch'

def increment_version(version, bump_type):
    major, minor, patch = map(int, version.split('.'))
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    return f'{major}.{minor}.{patch}'

if __name__ == '__main__':
    latest_tag = sys.argv[1]
    commits = sys.argv[2:]

    bump_type = determine_version_bump(commits)
    new_version = increment_version(latest_tag, bump_type)
    print(new_version)
