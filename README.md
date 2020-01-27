# Clone All

A tool for cloning/copying all repos from a given GitHub user, all in one go. Written in Python.

## Dependencies

- Python 3
- Requests module (pip install requests or pip3 install requests)

## How to use it

After you've cloned the clone_all repo, cd to the clone_all directory, and then use the following command:

```
./clone_all.py username_goes_here
```

The repos will be cloned in repos/username_goes_here/repo_name. Example: repos/0x416c616e/filehider.

## How to delete all downloaded data

```
./clone_all.py --reset
```

All repos you downloaded will be deleted.
