# lightup-py

Initially I wanted a really small binary, that I was going to build in C++ and use `libgit2`, learn `bazel` for builds, and all would be joyous.

However that turned into such a vast faff that I'm going with Python 3 instead, where I sort of just know I can get _something_ working in a reasonable time!

## To use this module

### Set up the install script

Get the code as a submodule of your project:

```bash
git submodule add git@github.com:/CJTozer/lightup
```

Copy the install script and commit it to your repo:

```bash
cp lightup/install.py .
git add install.py
git commit
```

### Configure

@@@ TODO

## Installation

After checking out your code on the target box, run

```bash
./install.py
```
