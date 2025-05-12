class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def display_info(self):
        print(f"Name: {self.name}, Membership iD: {self.membership_id}")
    
class StudentMember(Member):
    def __init__(self, name, membership_id):
        super().__init__(name, membership_id)
        self.borrowed_books = []  
 
    def add_book(self, book_title):
        self.borrowed_books.append(book_title)
        print(f"{book_title} has been added to {self.name}'s borrowed books.")        

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            print(f"{book_title} has been returned by {self.name}.")
        else:
            print(f"{self.name} has not borrowed {book_title}.")

    def display_borrowed_books_status(self):
        print(f"{self.name}'s borrowed books: {', '.join(self.borrowed_books) if self.borrowed_books else 'No books borrowed.'}")
        if self.borrowed_books:
            print("Books: ")
            for book in self.borrowed_books:
                print(f"- {book}")


student = StudentMember("Jhon Snow", "rt50")
student.display_info()
student.add_book("The Art of War")
student.add_book("48 Laws of Power")
student.display_borrowed_books_status()
student.return_book("The Art of War")
student.display_borrowed_books_status()