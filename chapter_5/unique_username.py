current_users = ['arj', 'james', 'nicole', 'merna', 'obet']
new_users = ['ARJ', 'jHoneaH', 'Nicole', 'khaye', 'dong']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'{new_user.title()} is already taken. Please choose another one.')
    else:
        print('Username available.')