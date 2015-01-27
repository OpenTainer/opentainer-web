========================
Contribute to OpenTainer
========================

To start contributing to OpenTainer, here is some info you might want to check out.

Typical Github workflow
=======================

To set up the environment, first fork the repository. Once the fork is complete, create a local copy and work on a feature branch.

::

    git clone git@github.com:{yourUsername}/opentainer-web
    cd opentainer-web
    # Add a second remote to the upstream OpenTainer repository your fork came from.
    # This lets users use commands such as 'git pull opentainer master' to update a
    # branch from the original trunk, as we will see below.
    git remote add opentainer git@github.com:OpenTainer/opentainer-web.git
    # Create a feature branch to work on.
    git checkout -b {featureBranchName}

To push code for review, the steps to be followed are:

::

    git rebase -i --autosquash
    git push origin {featureBranchName}:{featureBranchName}

Issues
======

The current issues related to OpenTainer can be seen at https://github.com/OpenTainer/opentainer-web/issues

Community
=========

Our users and developers use Internet Relay Chat (IRC).
:IRC: http://webchat.freenode.net/?channels=opentainer
