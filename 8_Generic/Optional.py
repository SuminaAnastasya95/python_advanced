
from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    name: str
    email: str


def get_user_by(user_id: int) -> Optional[User]:
    users = [
        User(1, "Nana", "aa@aa.ru"),
        User(2, "Bana", "bb@bb.ru")
    ]
    for user in users:
        if user.id == user_id:
            return user
    return None


user = get_user_by(99)
