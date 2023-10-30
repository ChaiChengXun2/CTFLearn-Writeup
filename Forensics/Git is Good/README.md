**Name of Challenge:** Git is Good
**Points:** 30
**Category:** Forensics

**Objective:** The primary objective of this challenge is to familiarize participants with Git's commit history and how to extract information from it.

**Solution:**
- In this challenge, you are provided with a Git repository. Git is a popular version control system used to track changes in code and other text files.
- Within the Git repository, there is a flag hidden, although it appears to be redacted.
- To reveal the actual value of the flag before it was redacted, you can utilize Git commands.
- The crucial command for this challenge is `git log`. This command allows you to view the commit history of the Git repository.
- In the Git log, you will see a list of commits, each associated with a unique identifier (commit hash). The commit history shows who made changes to the repository and when those changes were made.
- By using the `git show` command for each commit, you can explore the details of what was changed in that particular commit. This includes viewing the content that was added or removed in that commit.
- As you navigate through the commit history using `git log` and inspect the contents using `git show`, you can identify the commit that reveals the flag without the redaction.

**Flag:** CTFlearn{XXXXXXXXXX}

By solving this challenge, participants will gain valuable experience in using Git for forensic analysis. Understanding the history of changes within a Git repository is an essential skill for digital forensics and cybersecurity.
