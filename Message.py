# This defines a Message sent from one node to another using Spanning Tree Protocol.

class Message(object):

    def __init__(self, claimedRoot, distanceToRoot, originID, destinationID, pathThrough):
    # root = id of the switch thought to be the root by the origin switch
    # distance = the distance from the origin to the root node
    # origin =  the ID of the origin switch 
    # destination = the ID of the destination switch
    # pathThrough = Boolean value indicating the path to the claimed root from the origin passes through the destination 
        self.root = claimedRoot
        self.distance = distanceToRoot
        self.origin = originID
        self.destination = destinationID
        self.pathThrough = pathThrough

    # Member function that returns True if the message is properly formed, and False otherwise
    def verify_message(self):
        valid = True

        if self.pathThrough != True and self.pathThrough != False:
            valid = False
        if isinstance(self.root, int) == False or isinstance(self.distance, int) == False or isinstance(self.origin, int) == False or isinstance(self.destination, int) == False :
            valid = False
        
        return valid