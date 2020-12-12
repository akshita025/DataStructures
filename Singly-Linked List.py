class Node:
    """
    A node in a singly-linked list.
    """
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head=None
    
    def append(self,dataz):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if self.head is None:
            self.head=Node(dataz)
            return
        #traversal
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=Node(dataz)
    
    def printLst(self):
        """
        Print list to verify the linkedlist data
        """
        l=[]
        curr=self.head
        l.append(curr.data)
        while curr.next:
            curr=curr.next
            l.append(curr.data)
        print(l)
        
    def prepend(self,dataz):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.x=self.head
        self.head=Node(dataz)
        self.head.next=self.x
        
    def find(self,dataz):
        """
        Search for the first element with 'data' matching
        'key'.
        """
        cur=self.head
        x=0
        while True:
            if cur.data==dataz:
                x=1
                break
            else:
                cur=cur.next
                if cur==None:
                    break
        if x==1:
            print("True")
        else:
            print("False")
    
    def concat(self,ls):
        """
        Concat a list into the likedlist
        """
        for i in ls:   
            self.append(i)
    
    def remove(self,dataz):
        """
        Remove the first occurrence of 'key' in the list.
        Takes O(n) time.
        """
        currt=self.head
        if currt.data == dataz:
            self.head=currt.next
        while True:
            if currt.next.data==dataz:
                currt.next=(currt.next).next
                break
            else:
                currt=currt.next
                
    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        lt=[]
        crt=self.head
        lt.append(crt.data)
        while crt.next:
            crt=crt.next
            lt.append(crt.data)
        lt.reverse()
        self.head=None
        self.concat(lt)
        
if __name__=="__main__":
    LLobj=Linkedlist()
    LLobj.append(1)
    LLobj.append(2)
    LLobj.append(3)
    LLobj.prepend(4)
    LLobj.concat(['a','b','c'])
    LLobj.find('b')
    LLobj.remove('c')
    LLobj.reverse()
    LLobj.printLst()
