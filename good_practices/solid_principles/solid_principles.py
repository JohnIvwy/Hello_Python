# -----------------------------------------------------------------------------------------------------
# ---------------------------------------- Principios SOLID -------------------------------------------
# -----------------------------------------------------------------------------------------------------

# Son 5 principios que nos ayudan a crear código más limpio, mantenible y fácil de escalar.


# -----------------------------------------------------------------------------------------------------

# Principio #1: S - Single Responsibility Principle (SPR - Principios de Responsabilidad Única)

# Una clase se encarga de una única Responsabilidad o Tarea y una Única razón para cambiar.

# Forma correcta de aplicar el principio:
# Una clase solo para crear el usuario
class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

# Una única clase para guardar en la base de datos
class UserService:
    def save_to_database(self, user):
        pass

# Una única clase para la responsabilidad de enviar un email
class EmailService:
    def send_email(self, email, message):
        pass


''' EXTRA '''
'''
Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
manejar diferentes aspectos como el registro de libros, la gestión de usuarios
y el procesamiento de préstamos de libros.

Requisitos:
    1. Registrar libros: El sistema debe permitir agregar nuevos libros con
    información básica como título, autor y número de copias disponibles.
    2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
    información básica como nombre, número de identificación y correo electrónico.
    3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
    tomar prestados y devolver libros.
Instrucciones:
    1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
    los tres aspectos mencionados anteriormente (registro de libros, registro de
    usuarios y procesamiento de préstamos).
    2. Refactoriza el código: Separa las responsabilidades en diferentes clases
    siguiendo el Principio de Responsabilidad Única.
'''

# Modelamos: lo primero es modelar como objetos las entidades

# Entidad book
class Book:

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

# Entidad User
class User:

    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

# Entidad Loan: solo gestiona el procesamiento de prestamos
class Loan:

    def __init__(self):
        self.loans = []

    def loan_book(self, user, book):
        if book.copies > 0:
            book.copies -= 1
            self.loans.append(
                {"user_id": user.id, "book_title": book.title})
            return True
        return False

    def return_book(self, user, book):
        for loan in self.loans:
            if loan["user_id"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)
                book.copies += 1
                return True
        return False

# Desarrollamos el sistema que gestiona la Biblioteca

class Library:

    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans_service = Loan()

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loans_service.loan_book(user, book)
        return False

    def return_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book:
            return self.loans_service.return_book(user, book)
        return False



# -----------------------------------------------------------------------------------------------------

# Principio #2: O - Open / Closed Principle (OCP)

# Abierto a extensión / cerrado a modificación


# -----------------------------------------------------------------------------------------------------

# Principio #3: L - Liskov Substitution Principle (LSP)

# Las subclases deben poder reemplazar a la clase padre sin romper nada


# -----------------------------------------------------------------------------------------------------

# Principio #4: I - Interface Segregation Principle (ISP)

# Nadie debería depender de métodos que no usa


# -----------------------------------------------------------------------------------------------------

# Principio #5: D - Dependency Inversion Principle (DIP)

# Depende de abstracciones, no de clases concretas
