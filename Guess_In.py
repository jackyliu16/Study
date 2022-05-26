"""
@Target : 
@Annotation : 
@Author : JackyLiu
@Date   : 2022/5/26 18:04
@Reference  :None
"""
import random


class Guess(object):
    def __init__(self):
        self._num = random.randint(0, 1024)
        self._guess_times = 0

    def guess(self, num: int) -> int:
        """
        :return:
            0:  succeed
            1:  too low
            -1: too high
        """
        self._guess_times += 1
        return 0 if self._num == num else -1 if self._num < num else 1

    def get_time(self) -> int:
        return self._guess_times


if __name__ == '__main__':
    pass
    # guess = Guess()
    # print(guess.num)
    # num:int = int(input("C:\\"))
    # while num != guess.num:
    #     num:int = int(input("C:\\"))
    #     print(guess.guess(num))
