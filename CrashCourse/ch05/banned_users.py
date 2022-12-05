
banned_users = ['andrew', 'carolina', 'david']

user = input("Enter the user: ")

if user not in banned_users:
    print(f"Hello {user.title()}, you're welcome")
else:
    print(f"Hey {user.title()}, you can't make any comment here" )
    