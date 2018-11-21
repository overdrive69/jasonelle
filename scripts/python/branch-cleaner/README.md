# Branch Cleaner

This is a quick way to archive a git branch. Maybe you do not use the code anymore and the branch is cluttering the repo but for backup or historical reasons you need to keep it somewhere.

## Using Cleaner

You need `python 3` and run `./cleaner`. 
Make sure you are in the branch that should be keep.

If you want to preserve more branches add them to the `protected` list
inside the `cleaner` script.

## Manual Process

If you like to do the same thing as the `cleaner` script. Follow these steps.

The first thing is to checkout to the branch

```
$ git checkout my-branch
```

Then create a new tag. The recommended format is `archive/branch-{name}`

```
$ git tag archive/branch-my-branch
```

Now we can upload the tags to Github or Gitlab

```
$ git push origin --tags
```

And delete the branch from local and origin repos.

Be sure to be in another branch like master

```
$ git checkout master
```

Then

```
$ git branch -d my-branch
$ git push origin :my-branch
```

If you need to delete the tag (an all the branch backup) from local

```
$ git tag -d archive/branch-my-branch
```

Or from origin

```
$ git push --delete origin archive/branch-my-branch
```

This will erase all tagged branch data though. Please be careful.