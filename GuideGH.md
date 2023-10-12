# Guide to Modifying the SolverSLEquations Repository using PyCharm

This guide will help you understand how to modify the `SolverSLEquations` repository using PyCharm and some basic Git commands.

## Setting up PyCharm

1. Install [PyCharm](https://www.jetbrains.com/pycharm/download/) if you haven't already.
2. Open PyCharm and click on `Get from VCS`.
3. In the URL field, paste the following link: `https://github.com/930r91na/SolverSLEquations.git`
4. Choose a directory to save the project and click `Clone`.

## Basic Git Commands in PyCharm

### Pulling Changes from the Remote Repository

1. Open the `VCS` menu at the top.
2. Hover over `Git` and select `Pull...`.
3. Ensure the remote and branch are correct and click `Pull`.

### Pushing Changes to the Remote Repository

1. After making and saving your changes, open the `VCS` menu.
2. Hover over `Git` and select `Commit...`.
3. Write a meaningful commit message, select the files you want to commit, and click `Commit and Push...`.
4. Confirm the push in the following dialog.

### Creating a New Branch

1. In the bottom-right corner, click on the Git branch name (e.g., `main`).
2. Select `New Branch`.
3. Name your branch and click `OK`.

### Switching Between Branches

1. In the bottom-right corner, click on the Git branch name.
2. From the list, select the branch you want to switch to.

### Merging Branches

1. First, switch to the branch you want to merge into (e.g., `main`).
2. In the bottom-right corner, click on the Git branch name.
3. Hover over the branch you want to merge from and select `Merge into Current`.

## Pushing to the Main Branch

Before pushing to the `main` branch:

1. Ensure you've pulled the latest changes.
2. Test your code thoroughly.
3. If you're working on a separate branch, merge it into `main` first.
4. Follow the steps above to push your changes.

Remember, always communicate with your team before making significant changes or pushing to the `main` branch.


