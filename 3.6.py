from collections import deque

class Shelter:

    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.counter = 0

    def enqueue(self, type):
        if type == 0:
            self.dogs.append(self.counter)
        else:
            self.cats.append(self.counter)
        self.counter += 1

    def dequeueAny(self):
        if not self.dogs and not self.cats:
            raise Exception("no animals available")
        if not self.cats:
            return self.dogs.popleft()
        if not self.dogs:
            return self.cats.popleft()
        if self.cats[-1] < self.dogs[-1]:
            return self.cats.popleft()
        return self.dogs.popleft()

    def dequeueDog(self):
        if not self.dogs:
            raise Exception("no dogs available")
        return self.dogs.popleft()

    def dequeueCat(self):
        if not self.cats:
            raise Exception("no cats available")
        return self.cats.popleft()


s = Shelter()

for func in [s.dequeueAny, s.dequeueCat, s.dequeueDog]:
    try:
        func()
    except Exception as e:
        print(e)

for t in [1,0,1,1,0,0,0]:
    s.enqueue(t)

print(s.dequeueAny())
print(s.dequeueCat())
print(s.dequeueDog())
print(s.dequeueAny())
print(s.dequeueDog())
print(s.dequeueAny())
