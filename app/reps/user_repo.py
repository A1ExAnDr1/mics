from uuid import UUID
from app.models.user import User

users: list[User] = [
    User(id=UUID('7c7f4267-56da-481f-8a4f-0b33a2fcc188'),
         name='Александр'),
    User(id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
         name='Роман'),
    User(id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
         name='Иван')
]
class UsersRepo():
    def get_users(self) -> list[User]:
        return users

    def get_user_by_id(self, id: UUID) -> User:
        for d in users:
            if d.id == id:
                return d
        raise KeyError
