
# def divide(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         return "Błąd: Nie można dzielić przez zero."
#     return result
#
#
#
#
# # Przykład użycia
# print(divide(10, 2))  # Powinno zwrócić 5.0
# print(divide(10, 0))  # Powinno zwrócić błąd
#
# def check_positive(number):
#     assert number > 0, "Liczba musi być dodatnia."
#
# # Przykład użycia
# try:
#     # check_positive(5)  # Powinno przejść bez problemu
#     check_positive(-3)  # Powinno zgłosić błąd
# except AssertionError as e:
#     print(e)

# class InvalidAgeError(Exception):
#     pass
#
# def set_age(age):
#     if age < 0:
#         raise InvalidAgeError("Wiek nie może być ujemny.")
#     print(f"Wiek ustawiony na: {age}")
#
# try:
#     set_age(25)  # Powinno przejść bez problemu
#     set_age(-5)  # Powinno zgłosić błąd
# except InvalidAgeError as e:
#     print(e)

# class UserAlreadyExistsError(Exception):
#     pass
#
# class ActiveDirectory:
#     def __init__(self):
#         self.users = set()  # Zbiór użytkowników
#
#     def add_user(self, username):
#         if username in self.users:
#             raise UserAlreadyExistsError(f"Użytkownik '{username}' już istnieje.")
#         self.users.add(username)
#         print(f"Użytkownik '{username}' został dodany.")
#
# # Przykład użycia
# ad = ActiveDirectory()
#
# try:
#     ad.add_user("jan.kowalski")
#     ad.add_user("jan.kowalski")  # Próba dodania tego samego użytkownika
# except UserAlreadyExistsError as e:
#     print(e)


# class UserNotFoundError(Exception):
#     pass
#
# class ActiveDirectory:
#     def __init__(self):
#         self.users = set()
#
#     def add_user(self, username):
#         self.users.add(username)
#
#     def remove_user(self, username):
#         if username not in self.users:
#             raise UserNotFoundError(f"Użytkownik '{username}' nie został znaleziony.")
#         self.users.remove(username)
#         print(f"Użytkownik '{username}' został usunięty.")
#
# # Przykład użycia
# ad = ActiveDirectory()
# ad.add_user("piotr.wisniewski")
#
# try:
#     ad.remove_user("piotr.wisniewski")  # Próba usunięcia nieistniejącego użytkownika
# except UserNotFoundError as e:
#     print(e)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def validate(self):
        assert "@" in self.email, "Email musi zawierać '@'."
        assert len(self.username) > 0, "Nazwa użytkownika nie może być pusta."

# Przykład użycia
user = User("maria.kowalska", "maria.kowalskaexample.com")

try:
    user.validate()  # Walidacja atrybutów
    print("Atrybuty użytkownika są poprawne.")
except AssertionError as e:
    print(f"Błąd walidacji: {e}")


