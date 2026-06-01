#we make list flow from reverse
class solution:
    def reverseLL(self, Node, head):
      # we take prev as none
        prev=None 
      # use cur for pointing the status of head
        cur=head 
        while cur:
          # while cur not equal to null we goes on next and next 
            front=cur.next 
          # move to next head
            cur.next=prev 
          # point prev as cur
            prev=cur 
          #we swap it from prev to cur and cur to front 
            cur=front 
          # we written reverse fromat by prev 
        return prev
