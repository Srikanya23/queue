class Circular_queue :
    def __init__(self,size):
        self.size = size
        self.queue = [None for i in range(self.size)]
        self.f = self.r = int(-1)
        self.n = 0
    def Enqueue (self,val):
        self.r = (self.r + 1)%self.size
        if self.r == self.f:
            print("Queue is Full")
            return "Queue is Full"
        elif self.queue[self.r] != None:
            print(f"Queue isfull and {val} is not Enqueued")
            return  
        else :
            self.queue[self.r] = val
            self.n += 1
    def Dequeue(self):
        
        if self.r == self.f :
            return "Queue is empty"
            
        
        
        else :
            self.f = (self.f + 1)%self.size
            temp = self.queue[self.f]
            self.queue[self.f] = None
            self.n -= 1
            return temp
        
    def Display(self):
        if(self.f== self.r): 
            print ("Queue is Empty")
        
        elif (self.r >= self.f):
            for i in range(self.f, self.r + 1):
                print(self.queue[i], end = " ")
        else:
            for i in range(self.f, self.size):
                print(self.queue[i], end = " ")
            for i in range(0, self.r + 1):
                print(self.queue[i], end = " ")