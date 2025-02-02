# users = []
users = ['admin', 'arj', 'ian', 'james']

if len(users) == 0:
        print('No user data available.')
else: 
    for user in users:
        
        if user.title() == 'Admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for loggin in again.")