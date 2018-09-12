### Configure Git for contributing

Work through this page to configure Git and a repository you'll use throughout
the Contributor Guide.
The work you do further in the guide, depends on the work you do here.

## Task 1. Fork and clone the AgavePy repository

Before contributing, you must first fork the AgavePy code repository.
A fork makes a copy of a repository at a particular point in time.
Github tracks for you where a fork originates.

As you make contributions, you change the code in your fork.
When you are ready, you make a pull request back to the original AgavePy
repository.

To fork and clone AgavePy:
1. Go to the [AgavePy repository](https://github.com/TACC/agavepy).

2. Click the "Fork" button in the upper right corner of the Github interface.

3. Copy your fork's clone URL from Github (t will look something like 
`https://github.com/<your-username>/agavecil`).

4. Open a terminal on your local host and change to your home directory.
   ```
   $ cd ~
   ```

5. Create a `repos` directory.
   ```
   $ mkdir repos
   ```

6. Change into your `repos` directory.
   ```
   $ cd repos
   ```

7. Clone your fork into your local host.
   ```
   $ git clone https://github.com/<your-username>/agavepy
   ```

8. Change directory into your new `agavepy` directory.
   ```
   $ cd agavepy
   ```

Take a moment to familiarize yourself with the repository's contents.


## Task 2. Set your signature and an upstream remote

When you contribute to Agavepy, you must certify you agree with the [Developer
Certificate of Origin](https://developercertificate.org/).
You indicate your agreement by signing your `git` commits like this:
```
Signed-off-by: Gopher Smith <gopher@email.com>
```

To create a signature, you configure your username and email address in Git.
You can set these globally or locally on just your agavepy repository.
You must sign with your real name.
You can sign your `git` commit automatically with `git commit -s`. 
AgavePy does not accept anonymous contributions or contributions through
pseudonyms.

As you change code in your fork, you'll want to keep it in sync with the
changes others make in the original AgavePy repository.
To make syncing easier, you'll also add a _remote_ called `upstream` that
points to the original repository. 
A remote is just another project version hosted on the internet or network.

To configure your username, email, and add a remote:
1. Change to the root of your `agavepy` repository.
   ```
   $ cd ~/repos/agavepy
   ```

2. Set you `user.name` for the repository.
   ```
   $ git config --local user.name "firstName LastName"
   ```
   Use the `--global` flag instead, if you want to do this for all your `git`
   projects.

3. Set your `user.email` for the repository.
   ```
   $ git config --local user.email "email@emailcompany.com"
   ```
   Use the `--global` flag instead, if you want to do this for all your `git`
   projects.

4. Set your local repo to track changes upstream, on the original `agavepy`
   repository.
   ```
   $ git remote add upstream https://github.com/alejandrox1/agavepy
   ```

5. Check the results of your `git` configuration.
   ```
   $ git config --local -l
   core.repositoryformatversion=0
   core.filemode=true
   core.bare=false
   core.logallrefupdates=true
   user.name=Gopher Smith
   user.email=gopher@email.com
   remote.origin.url=https://github.com/Talejandrox1/agavepy
   remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
   remote.upstream.url=https://github.com/TACC/agavepy
   remote.upstream.fetch=+refs/heads/*:refs/remotes/upstream/*
   ```

   To list just the remotes use:
   ```
   $ git remote -v
   origin	https://github.com/alejandrox1/agavepy (fetch)
   origin	https://github.com/alejandrox1/agavepy (push)
   upstream https://github.com/TACC/agavepy (fetch)
   upstream https://github.com/TACC/agavepy (push)
   ```

## Task 3. Create and push a branch

As you change code in your fork, make your changes on a repository branch.
The branch name should reflect what you are working on.
In this section, you create a branch, make a change, and push it up to your fork.

This branch is just for testing your config for this guide.
The changes are part of a dry run, so the branch name will be dry-run-test.
To create and push the branch to your fork on GitHub:

1. Open a terminal and go to the root of your `agavepy`.
   ```
   $ cd ~/repos/agavepy
   ```

2. Create a `dry-run-test` branch.
   ```
   $ git checkout -b dry-run-test
   ```
   This command creates the branch and switches the repository to it.

3. Verify you are in your new branch.
   ```
   $ git branch
   * dry-run-test
     master
   ```

4. Create a `Test.md` file in the repository's root.
   ```
   $ touch Test.md
   ```

5. Edit the file and add whatever information you want. Use your favourite text
   editor. For a quick test you can run the following command:
   ```
   $ echo "Hello github" >> Test.md
   ```

6. Check the status of your branch.
   ```
   $ git status
   On branch dry-run-test
   Untracked files:
     (use "git add <file>..." to include in what will be committed)

       TEST.md

   nothing added to commit but untracked files present (use "git add" to track)
   ```
   You've only changed one file. Right now, this file is untracked by git.

7. Add your file.
   ```
   $ git add Test.md
   ```

8. Sign and commit your change.
   ```
   $ git commit -s -m "Making a dry run test"
   [dry-run-test 6e728fb] Making a dry run test
    1 file changed, 1 insertion(+)
    create mode 100644 TEST.md
   ```
   Commit messages should have a short summary sentence of no more than 50
   characters. Optionally, you can also include a more detailed explanation
   after the summary. Separate the summary from any explanation with an empty
   line.

   Another good option is to set your editor, here we are using `vim` as an
   example:
   ```
   $ git config --global core.editor "vim"
   ```
   Then, every time you want to make a commit, do:
   ```
   $ git commit -sv
   ```
   Which will use `vim` to write the commit.

9. Push your changes to GitHub.
   ```
   $ git push --set-upstream origin dry-run-test
   Username for 'https://github.com': gopher
   Password for 'https://gopher@github.com':
   ```
   Git prompts you for your GitHub username and password.
   Then, the command returns as a result.
   ```
   Counting objects: 13, done.
   Compressing objects: 100% (2/2), done.
   Writing objects: 100% (3/3), 320 bytes | 0 bytes/s, done.
   Total 3 (delta 1), reused 0 (delta 0)
   To https://github.com/gopher/agavepy
    * [new branch]      dry-run-test -> dry-run-test
   Branch dry-run-test set up to track remote branch dry-run-test from origin.
   ```

11. Open your brwoser to GitHub.

12. Navigate to your agavepy fork.

13. Make sure the `dry-run-test` branch exists, that it has yourcommit, and
    that the commit is signed.

## Where to go next
Congratulations, you have finished configurating both your local host
environment and Git for contributing.
In the next section you'll [learn how to set up and work in an AgavePy
development container](set-up-dev-end.md)
