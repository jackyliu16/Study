class Philosophers:
    num, seen, locked = 3, "", ""
    chopsticks = [0 for i in range(num)] 
        
    @thread
    def people0(self):
        pid = 0

        while not self.tryacquire(): pass
        while not self.try_get_key((pid-1+self.num) % self.num): pass
        self.get_chopsticks((pid-1+self.num) % self.num)
        while not self.try_get_key(pid): pass
        self.get_chopsticks(pid)
        self.release()

        # eat

        while not self.tryacquire(): pass
        self.release_chopsticks((pid-1+self.num) % self.num)
        self.release_chopsticks(pid)
        self.release()


    
    def mark_green(self, state):
        acc = 0
        for i in range(self.num):
            if self.chopsticks[i] == 0:
                acc += 1
        if acc == 3:
            return 'red'

    def try_get_key(self, index : int) -> bool:
        """ if chopstick[pid] == 0 return true"""
        return self.chopsticks[index] == 0
    
    def get_chopsticks(self, index : int) -> None:
        self.chopsticks[index] += 1
    
    def release_chopsticks(self, index : int) -> None:
        self.chopsticks[index] -= 1

    def tryacquire(self):
        self.locked, seen = '🔒', self.locked
        return seen == ''

    def release(self):
        self.locked = ''
