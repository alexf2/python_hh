import re


class User:
    def __init__(self, name, acc_level):
        self.name = name
        self.level = acc_level

    def __rtepr__(self):
        return f'{self.name}: {self.level}'

    def __str__(self):
        return f'{self.name}: {self.level}'


class UserManager:

    user_expr = re.compile(r'\s*(get_users)|(\w+)\s+(\w+)\s+(\d+)?')

    def __init__(self):
        self.users = {}

    def add_user(self, name, level):
        if name in self.users:
            return None

        res = self.users[name] = User(name, level)
        return res

    def promote(self, name, level_inc=1):
        user = self.users.get(name, None)
        if not user:
            raise ValueError(f'No user: {name}')

        user.level += level_inc

    def demote(self, name, level_dec=1):
        user = self.users.get(name, None)
        if not user:
            raise ValueError(f'No user: {name}')

        user.level -= level_dec

    def get_users(self):
        return self.users.values()

    def remove_user(self, name):
        if name in self.users:
            return self.users.pop(name)

        return None

    @staticmethod
    def parse(user_record):
        if not len(user_record):
            return None

        um = UserManager()
        for m in UserManager.user_expr.findall(user_record):
            command = m[0] if m[0] else m[1]

            match command.casefold():
                case 'add_user':
                    um.add_user(m[2], int(m[3]))
                case 'remove_user':
                    um.remove_user(m[2])
                case 'promote':
                    um.promote(m[2])
                case 'demote':
                    um.demote(m[2])
                case 'get_users':
                    print(
                        ' '.join(
                            [f'{u.name}: {u.level} 'for u in um.get_users()]))
                    if not len(um.get_users()):
                        print('Не найдено')
                case _:
                    raise ValueError(
                        'Not supported command: {command.casefold()}')

        return um


for v in [
    'add_user Анна 1 add_user Борис 2 promote Анна get_users',
    'add_user Анна 3 add_user Борис 2 promote Анна get_users add_user Евгений 2',
        'add_user Bob 3 add_user Charlie 2 remove_user Bob remove_user Charlie get_users']:
    print(v)
    um = UserManager.parse(v)
    print('---------')
