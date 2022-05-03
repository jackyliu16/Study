class Philosophers:
    chopsticks, locked, seen, num = ["" for i in range(5)], "", ["", ""], 6

    def tryacquire(self):
        self.locked, seen = '🔒', self.locked
        return seen == ''

    def try_to_eat(self, number):
        self.chopsticks[number], self.chopsticks[(
            number - 1 + len(self.chopsticks) %
            len(self.chopsticks))], self.seen[0], self.seen[
                1] = "🔒", "🔒", self.chopsticks[number], self.chopsticks[(
                    number - 1 + len(self.chopsticks) % len(self.chopsticks))]
        return self.seen[0] == "" and self.seen[1] == ""

    def release(self):
        self.locked = ''

    @thread
    def people0(self):
        for _ in range(2):
            while not self.tryacquire():  # mutex_lock
                pass
            
            if try_to_eat(0):
                #cond_wait 
                _, self.waits = self.release(), self.waits + "0"
                # while "0" in self.waits:pass
                # while not try_to_eat(0):pass




            self.release()  # mutex_unlock
