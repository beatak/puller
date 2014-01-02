puller
======

This small tool fires `git-pull` in many directories.

Requirements
============

- python: I only test this with my environment. I have now Python 2.7.6 that runs on Mac OS X.
- sh: http://amoffat.github.io/sh/ - Install it via pip
- git: I'm sure you have it.

Scenario
========

Say you have the directory structure as follows:

- Your home directory
    - Repository
        - git_project_1
        - git_project_2
        - git_project_3
        - ...

And you want to do `git-pull` for each git project. Once you call `puller` when you're in the `Repository` directory, it will do `git-pull` for each git repository.

Install
=======

`git-clone` this repository and make a symbolic link to the `src/puller.py`

License
=======

MIT

