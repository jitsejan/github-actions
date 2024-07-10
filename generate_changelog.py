import subprocess

def generate_changelog():
    # Get git commit messages
    result = subprocess.run(['git', 'log', '--pretty=format:%s'], stdout=subprocess.PIPE)
    commits = result.stdout.decode('utf-8').split('\n')

    # Write to CHANGELOG.md
    changelog_content = '# Changelog\n\n'
    for commit in commits:
        changelog_content += f'- {commit}\n'
    
    with open('CHANGELOG.md', 'w') as f:
        f.write(changelog_content)
    
    return changelog_content

if __name__ == '__main__':
    changelog = generate_changelog()
    print(changelog)