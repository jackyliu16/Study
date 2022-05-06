class Philosophers:
    num, seen, locked = 3, "", ""
    chopsticks = [0 for i in range(num)] 


        
    @thread
    def people0(self):
        pid = 0

        while not self.tryacquire(): pass
        while not self.try_get_key((pid-1+self.num) % self.num) or not self.try_get_key(pid): pass
        _, _ = self.get_chopsticks((pid-1+self.num) % self.num), self.get_chopsticks(pid)
        self.release()

        # eat

        while not self.tryacquire(): pass
        _, _ = self.release_chopsticks((pid-1+self.num) % self.num), self.release_chopsticks(pid)
        self.release()
    
    @thread
    def people1(self):
        pid = 1

        while not self.tryacquire(): pass
        while not self.try_get_key((pid-1+self.num) % self.num) or not self.try_get_key(pid): pass
        _, _ = self.get_chopsticks((pid-1+self.num) % self.num), self.get_chopsticks(pid)
        self.release()

        # eat

        while not self.tryacquire(): pass
        _, _ = self.release_chopsticks((pid-1+self.num) % self.num), self.release_chopsticks(pid)
        self.release()

    @thread
    def people2(self):
        pid = 2

        while not self.tryacquire(): pass
        while not self.try_get_key((pid-1+self.num) % self.num) or not self.try_get_key(pid): pass
        _, _ = self.get_chopsticks((pid-1+self.num) % self.num), self.get_chopsticks(pid)
        self.release()

        # eat

        while not self.tryacquire(): pass
        _, _ = self.release_chopsticks((pid-1+self.num) % self.num), self.release_chopsticks(pid)
        self.release()


    
    @marker
    def mark_red(self, state):
        for pid in range(self.num):
            if self.chopsticks[pid] >= 2:
                return 'red'
    
    def try_get_key(self, index : int) -> bool:
        return self.chopsticks[index] == 0

    def get_chopsticks(self, index : int) -> None:
        self.chopsticks[index] += 1
    
    def release_chopsticks(self, index : int) -> None:
        self.chopsticks[index] -= 1

    def tryacquire(self):
        """ if 🔒 return false, else return true """
        self.locked, seen = '🔒', self.locked
        return seen == ''

    def release(self):
        self.locked = ''
    
