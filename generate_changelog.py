import subprocess

def generate_changelog():
    # Get git commit messages
    result = subprocess.run(['git', 'log', '--pretty=format:%s'], stdout=subprocess.PIPE)
    commits = result.stdout.decode('utf-8').split('\n')
    if not commits or commits == ['']:
        print("No new commits found.")
        return
    # Read the existing content of CHANGELOG.md if it exists
    try:
        with open('CHANGELOG.md', 'r') as f:
            existing_content = f.read()
    except FileNotFoundError:
        existing_content = ""
    
     # Prepare the new changelog content
    new_content = '## New Changes\n'
    for commit in commits:
        new_content += f'- {commit}\n'
    new_content += '\n'

    # Write the new changelog content to a separate file
    with open('new_changelog.txt', 'w') as f:
        f.write(new_content)

    # Combine the new content with the existing content
    combined_content = new_content + existing_content

    # Write the combined content back to CHANGELOG.md
    with open('CHANGELOG.md', 'w') as f:
        f.write(combined_content)

    # return new_content


if __name__ == '__main__':
    changelog = generate_changelog()
    print(changelog)
