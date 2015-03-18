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
$ python main
```

Thats it, you have the CSV file with the people you follow.
