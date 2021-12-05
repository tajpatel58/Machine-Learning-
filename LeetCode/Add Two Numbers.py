#%%

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    node_1 = l1
    node_2 = l2
    val_1 = node_1.val
    val_2 = node_2.val
    val = val_1 + val_2 
    carry_over = val // 10
    remainder = val % 10
    output = ListNode(val=remainder)
    node_1 = node_1.next
    node_2 = node_2.next
    indicator = 0 
    if node_1 != None or node_2 != None:
        indicator = 1 
        output.next = ListNode()
        previous_pointer = output.next
    while node_1 != None or node_2 != None:
        indicator = 1 
        if node_1 == None:
            val_1 = 0
            val_2 = node_2.val
            node_2 = node_2.next
        elif node_2 == None:
            val_1 = node_1.val
            val_2 = 0
            node_1 = node_1.next
        else:
            val_1 = node_1.val
            val_2 = node_2.val
            node_1 = node_1.next
            node_2 = node_2.next
        val = val_1 + val_2 + carry_over 
        remainder = val % 10
        carry_over = val // 10
        previous_pointer.val = remainder
        if node_1 != None or node_2 != None:
            previous_pointer.next = ListNode()
            previous_pointer = previous_pointer.next
    if node_1 == None and node_2 == None and carry_over > 0:
        if indicator == 1:
            previous_pointer.next = ListNode(val=carry_over)
        else:
            output.next = ListNode(val=carry_over)
    return output 

node_4 = ListNode(val=4)
node_3 = ListNode(val=3, next=node_4)
node_2 = ListNode(val=2, next=node_3)
node_1 = ListNode(val=1, next=node_2)

node_6 = ListNode(val=6)
node_5 = ListNode(val=5, next=node_6)

node_5_2 = ListNode(val=5)

x = addTwoNumbers(node_5_2, node_5_2)

while x.next != None:
    print(x.val)
    x = x.next
print(x.val)
# %%
