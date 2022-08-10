class MyCircularQueue:
    def _init_(self, size: int):
        self.size=size
        self.queue=[None]*size
        self.rear=-1
        self.front=-1
    
    def enqueue(self, value: int) -> bool:
        if(self.is_full()==False):
            if(self.front==-1):
                self.front=0
                self.rear=0
                self.queue[self.rear]=value
            else:
                self.rear=(self.rear+1)%self.size
                self.queue[self.rear]=value
            return True
        else:
            return False
     
    def dequeue(self) -> bool:
        if(self.is_empty()==False):
            if(self.front==self.rear):
                self.front=-1
                self.rear=-1
                return True
            else:
                self.front=(self.front+1)%self.size
                return True
        else:
            return False
