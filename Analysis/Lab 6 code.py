# Def the Node class
class Node:
    def __init__(self, data):
        #stores node data 
        self.data = data      
        #Initialize the next pointer 
        self.next = None      

# Create nodes with data values
node1 = Node(10)             
node2 = Node(20)             
node3 = Node(30) 

# Link the nodes together and form a chain 
node1.next = node2           
node2.next = node3           

# Func to go over the list and print node's data
def print_linked_list(head):
    current = head
    while current is not None:
        print(f"{current.data} -> ", end="")
        current = current.next
    print("None")  


#Test the print fuc, print list of node1
print("Initial linked list:")
print_linked_list(node1)


# Ex 1: Update node2's data and print
node2.data = 25 
print("\nLinked list after updating node2's data:")
print_linked_list(node1)

## Ex 2: Add a new node with value and link it to list
node4 = Node(40)            
node3.next = node4          
print("\nLinked list after adding node4:")
print_linked_list(node1)

# Ex 3: Modify the print function to count nodes and print the count
def print_linked_list_with_count(head):
    current = head
    count = 0
    while current is not None:
        print(f"{current.data} -> ", end="")
        current = current.next
        count += 1
    print("None")            
    print(f"Total nodes count: {count}")


# Test the new function
print("\nLinked list with node count:")
print_linked_list_with_count(node1)