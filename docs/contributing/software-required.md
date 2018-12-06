### Get the required software for Linux or macOS

Before you begin contributing you must have:

* `git`
* `make`
* `docker`

You'll notice that `python`, the language that agavepy is written on, is not
listed.
That's because you don't need it installed; AgavePy's development environment
provides it for you.
You'll learn more about the development environment later.


## Task 1. Install git
Install `git` on your local system.
Try running the following command to check if `git` is already on your system
and properly installed:
```
$ git --version
```

This documentation is written using `git` version 2.17.1.
Your version may be different depending on your OS.


## Task 2. Install make
Install `make`.
To check if `make` is already on your system or if it has been properly installed
try running the following command:
```
$ make -v
```
This documentation is written using GNU Make 4.1.
Your version may be different depending on your OS.


## Task 3. Install or upgrade Docker
Install `docker` on your local system.
To check if `docker` is already on your system or if it has been properly installed
try running the following command:
```
$ docker --version
```
This documentation is written using Docker version 18.03.1-ce.


### Tip for Linux users
This guide assumes you have added your user to the docker group on your system.
To check, list the group's contents:
```
$ getent group docker
docker:x:999:<username>
```

If the command returns no matches, you have two choices. 
You can preface this guide's docker commands with sudo as you work. 
Alternatively, you can add your user to the docker group as follows:
```
$ sudo usermod -aG docker <username>
```
You must log out and log back in for this modification to take effect.


## Where to go next
In the next section, yu'll [learn how to set up and configure Git for
contributing to agavepy](set-up-git.md)
