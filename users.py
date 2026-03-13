# The users module of the program
# Again, I used classes because it acts as molds, without needing instructions all the time
# Again, I used list comprehensions, to make the code cleaner and readable

import persistence
import random

class Users:
    def __init__(self, username, user_id, borrowed_books=None):
        self.username = username
        self.user_id = user_id
        self.borrowed_books = borrowed_books or []

class UsersManage:
    def __init__(self):
        data = persistence.load_data() or {}
        user_data = data.get('users', [])
        self.user = [Users(u['username'], int(u['user_id']), u['borrowed_books']) for u in user_data]

    def save_users(self):
        data = persistence.load_data() or {}
        data['users'] = [{'username': u.username, 'user_id': u.user_id, 'borrowed_books': u.borrowed_books} for u in self.user]
        persistence.save_data(data)


    def create_user(self, username): 
        new_id = random.randint(1000, 9999)
        
        while any(u.user_id == new_id for u in self.user):
            new_id = random.randint(1000, 9999)

        new_user = Users(username, new_id)
        self.user.append(new_user)
        self.save_users()
        
        print(f"user created successfully!")
        print(f'user: {username} | ID: {new_id}')


    def delete_users(self, user_id):
        user_to_delete = None
        for u in self.user:
            if u.user_id == user_id:
                self.user.remove(u)
                self.save_users()
                return True
        return False


    def find_user(self, user_id):
        for u in self.user:
            if user_id == u.user_id:
                return u
        return None

    def see_users(self):
        if not self.user:
            print('Dont exist any users here')
        else:
            for u in self.user:
                print(f'ID: {u.user_id} | username: {u.username}')
    

