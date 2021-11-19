from entities.user import User
from string import ascii_lowercase

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class RequirementsNotMetError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise RequirementsNotMetError("Username or password does not meet requirements")

        for letter in username:
            if letter not in ascii_lowercase:
                raise RequirementsNotMetError("Username or password does not meet requirements")
        
        if len(password) < 8:
            raise RequirementsNotMetError("Username or password does not meet requirements")

        for letter in password:
            if letter not in ascii_lowercase:
                if letter not in "0123456789":
                    raise RequirementsNotMetError("Username or password does not meet requirements")
        
        if not any(char.isdigit() for char in password):
            raise RequirementsNotMetError("Username or password does not meet requirements")