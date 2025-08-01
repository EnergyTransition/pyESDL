from dataclasses import dataclass


@dataclass
class Credentials:
    username: str
    password: str

    @staticmethod
    def create_dict(id: str, username: str, password: str) -> dict[str, 'Credentials']:
        d = dict()
        d[id] = Credentials(username, password)
        return d
