import subprocess
file_name="branches.txt"
cur_branch = "users/nikunjg/GenExpandBleed"
main = "main"

# Define the Git command you want to execute
git_command = ["git", "branch", "-D"]

# Execute the command
with open(file_name,'r') as files:
    for file in files:
        file = file.strip()
        if file == cur_branch or file == main:
            continue
        git_command.append(file)
        print(git_command)
        
        result = subprocess.run(git_command, capture_output=True, text=True)
        print("Output:", result.stdout)
        if result.stderr:
            print("Error:")
            print(result.stderr)
        git_command.pop()

