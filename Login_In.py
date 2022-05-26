"""
@Target : 完成用户登录模块的内部逻辑设计
@Annotation : 提供如下函数
    MemoryCell()
        check_passwd
        add_user
        find_user_name
@Author : JackyLiu
@Date   : 2022/5/25 22:10
@Reference  :None
"""


class _User(object):
    def __init__(self, name: str, passwd: str):
        self.name = name
        self.passwd = passwd

    # def __str__(self):
    #     # TODO only for debug
    #     return f"name={self.name}, \tpasswd={self.passwd}"


class MemoryCell(object):
    def __init__(self):
        self._user_list = []
        self._user_list.append(_User("admin", "123456"))

    def check_passwd(self, name: str, passwd: str) -> int:
        """
        check if have this user and passwd right!
        :return:
            0: user existed and passwd match
            -1:user existed and passwd not match
            -2:user not existed
        """
        # try to play with iterator but forgot
        for item in self._user_list:
            if item.name == name:
                if item.passwd == passwd:
                    return 0
                else:
                    return -1
        return -2

    def add_user(self, name: str, passwd: str) -> bool:
        if self.find_user_name(name):
            return False
        new_user = _User(name, passwd)
        self._user_list.append(new_user)
        return True

    def find_user_name(self, name:str) -> bool:
        for item in self._user_list:
            if item.name == name:
                return True
        return False


if __name__ == '__main__':
    memory_cell = MemoryCell()
    memory_cell.check_passwd("admin", "123456")
    memory_cell.add_user("jacky", "123")
    print(memory_cell.check_passwd("jacky", "123"))
    memory_cell.add_user("liu", "124")
    print(memory_cell.check_passwd("lsf", "14"))
    print(memory_cell.check_passwd("liu", "4221"))
    print(memory_cell.check_passwd("liu", "124"))
    print(memory_cell)
