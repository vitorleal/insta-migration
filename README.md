# Instagram Migration

This is a simple project for a friend of mine so he can migrate his instagram account. It get's the users he follow nad put in a CSV file.

## How to run
Edit the **main.py** file.
```python
def main():
    # insert you user name here
    insta = InstaMigration('YOUR_INSTAGRAM_USER_NAME')
    insta.make_migration()
```

Then run the code
```
$ python main.py
```

Thats it, you have the CSV file with the people you follow.


##Author

| [![twitter/vitorleal](http://gravatar.com/avatar/e133221d7fbc0dee159dca127d2f6f00?s=80)](http://twitter.com/vitorleal "Follow @vitorleal on Twitter") |
|---|
| [Vitor Leal](http://vitorleal.com) |