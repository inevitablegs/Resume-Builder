import os
import sys

if len(sys.argv) < 2:
    print("❌ Please provide a commit message.")
    print("✅ Example: python gitpush.py 'Initial commit'")
    sys.exit(1)

commit_message = sys.argv[1]

os.system("git init")
os.system("git add .")
os.system(f'git commit -m "{commit_message}"')
os.system("git push")
