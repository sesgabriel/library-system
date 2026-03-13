# The menu interface for the main.py
# I added  verification for all options that requires an user input

from library import Library
from users import UsersManage

def run():
    library = Library()
    users = UsersManage()

    while True:
        print('1 - Add a book')
        print('2 - Take a book')
        print('3 - Return a book')
        print('4 - Create a user')
        print('5 - Delete a user')
        print('6 - See all users')
        print('7 - See all books')
        print('8 - Search books by author')
        print('9 - Exit')
        option = input('Select an option: ')

        if option == '1':
            author = input('Author: ').strip()
            if not author:
                print('Author cannot be empty!')
                continue

            title = input('Title: ').strip()

            if not title: 
                print('Title cannot be empty!')
                continue

            library.add_books(author, title)
            print('Book added successfully!')

        elif option == '2':
            title = input('Title: ').strip()
            if not title:
                print('Title cannot be empty!')
                continue

            author = input('Author: ').strip()
            if not author:
                print('Author cannot be empty!')
                continue

            try:
                user_id = int(input('User ID: '))
                if not user_id:
                    print('User ID cannot be empty!')
                    continue

            except ValueError:
                print('ID must be a number!')
                continue

            user = users.find_user(user_id)
            if not user: 
                print('User not found!')
                continue

            book = library.take_books(title, author, user_id)
            if book:
                user.borrowed_books.append(book.title)
                users.save_users()
                print('Book loaned successfully!')
            else:
                print('This book is already loaned or not exist!')

        elif option == '3':
            title = input('Title: ').strip()
            if not title:
                print('Please, type the title!')
                continue
            
            author = input('Author: ')
            if not author:
                print('Please, type the author!')
                continue

            try:
                user_id = int(input('User ID: '))
                if not user_id:
                    print('Please, type the user ID.')
                    continue
                
            except ValueError: 
                print('ID must be a number!')
                continue

            book = library.return_books(title, author)
            if book:
                user = users.find_user(user_id)
                if user and title in user.borrowed_books:
                    if book.borrowed_by == user_id:
                        user.borrowed_books.remove(title)
                        users.save_users()
                        print('Book returned successfully!')
                else:
                    print('This user did not borrow that book or user not found!')
            else:
                print('Book not found or wasnt loaned.')


        elif option == '4':
            username = input('Username: ').strip()
            if not username:
                print('Please, type the username!')
                continue

            if any(char.isdigit() for char in username):
                print('Username cannot contain numbers!')
                continue

            users.create_user(username)

        elif option == '5':
            try:
                user_id = (int(input('User ID: ')))
                if not user_id:
                    print('Please, type the user ID.')
                    continue
                
            except ValueError:
                print('The ID must be a number!')
                continue

            if users.delete_users(user_id):
                print('User deleted successfully!')
            else:
                print('User not found!')


        elif option == '6':
            users.see_users()

        elif option == '7':
            books = library.see_books()
            if not books:
                print('There are no books in the library!')
            else:
                for book in books:
                    if book.is_loaned:
                        print(f'Title: {book.title} | Author: {book.author} | Loaned by: {book.borrowed_by}')
                    else:
                        print(f'Title: {book.title} | Author: {book.author} | Available')

                    
        elif option == '8':
            author = input('Author: ').strip()
            if not author:
                print('Please, type the author name!')
                continue

            author_books = library.find_book_by_author(author)
            if not author_books:
                print('This author has no books in the library or dont exist!')
            else:
                print(f'Books by {author}:')
                for book in author_books:
                    print(f'Title: {book.title} | Author: {book.author}')

        elif option == '9':
            print('Goodbye!!!!')
            break

            







if __name__ == '__main__':
    run()