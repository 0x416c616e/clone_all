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

## Cloning tons of repos can lead to performance issues!

If you clone tons of repos on Windows, the OS will have issues with indexing stuff because it tries to build local searches. In order to fix this, go to Control Panel -> Indexing Options -> Advanced -> Rebuild and hit Yes.

On other OSes (which I haven't tested cloning tons and tons of repos on anything except Windows 10), you might have similar issues with local search indexes, so keep that in mind.

In the future, I might add the ability to choose to download repos instead of cloning them. I'm not sure if that will be better for performance or not.



