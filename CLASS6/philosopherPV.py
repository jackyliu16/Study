class Philosophers:
    num = 3
    chopsticks, locked, seen, waits = [0 for i in range(num)], "", "",  []

    def tryacquire(self):
        self.locked, seen = '🔒', self.locked
        return seen == ''

    def release(self):
        self.locked = ''

    def try_get_chopsticks(self, pid):
        return self.chopsticks[(pid-1+self.num)%self.num]==0 and self.chopsticks[(pid)]==0

    @thread
    def people0(self):
        pid = 0
        
        while not self.tryacquire(): pass # mutex_lock
        self.chopsticks[(pid-1+self.num)%self.num], self.chopsticks[pid], cs = self.chopsticks[(pid-1+self.num)%self.num] + 1, self.chopsticks[pid] + 1, True
        self.release()

        while not self.tryacquire(): pass
        self.chopsticks[(pid-1+self.num)%self.num], self.chopsticks[pid], cs = self.chopsticks[(pid-1+self.num)%self.num] - 1, self.chopsticks[pid] - 1, True
        del cs
        self.release()  # mutex_unlock

    @thread
    def people1(self):
        pid = 1
        
        while not self.tryacquire(): pass # mutex_lock
        self.chopsticks[(pid-1+self.num)%self.num], self.chopsticks[pid], cs = self.chopsticks[(pid-1+self.num)%self.num] + 1, self.chopsticks[pid] + 1, True
        self.release()

        while not self.tryacquire(): pass
        self.chopsticks[(pid-1+self.num)%self.num], self.chopsticks[pid], cs = self.chopsticks[(pid-1+self.num)%self.num] - 1, self.chopsticks[pid] - 1, True
        del cs
        self.release()  # mutex_unlock

    @thread
    def people2(self):
        pid = 2
        
        while not self.tryacquire(): pass # mutex_lock    
        self.chopsticks[(pid-1+self.num)%self.num], self.chopsticks[pid], cs = self.chopsticks[(pid-1+self.num)%self.num] + 1, self.chopsticks[pid] + 1, True
        self.release()

        while not self.tryacquire(): pass
        self.chopsticks[(pid-1+self.num)%self.num], self.chopsticks[pid], cs = self.chopsticks[(pid-1+self.num)%self.num] - 1, self.chopsticks[pid] - 1, True
        del cs
        self.release()  # mutex_unlock


    @marker
    def mark_red(self, state):
        for pid in range(self.num):
            if self.chopsticks[pid] >= 2:
                return 'red'

