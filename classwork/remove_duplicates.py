# start from the head 
# go through each node, check the node's after and check if they are duplicates
# set those duplicates to None

def remove_duplicates(self):
    current = self.head # current set to head
    
    while current.next != None: 
        if current.data == current.next.data: # if current data is matched with the next then we have a duplicate
            current.next = current.next.next # set current.nect to the next next one (skip over the next) - remove the duplicate
        else: # no duplicate
            current = current.next # we move our current to the next value that we are checking


