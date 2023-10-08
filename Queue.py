class queue:
    def __init__(self):
        self.queue =[]
        self.n = 0
    def Enqueue (self,item):
        self.queue.append(item)
        self.n+=1
    def __len__(self):
        return self.n
    def Dequeue (self):
        if self.n == 0:
            return "queue is empty"
        else :
            item = self.queue[0]
            self.queue = self.queue[1:]
            self.n-=1
            return item
    def Display(self):
        for i in range(self.n):
            print(self.queue[i])
            