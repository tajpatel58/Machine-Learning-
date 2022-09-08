#%%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head: ListNode) -> ListNode:
    node = head
    prev = None
    output = head
    while node:
        output = node
        node = node.next
        output.next = prev
        prev = output
    return output

first_node = ListNode(10)
second_node = ListNode(15, first_node)
third_node = ListNode(20, second_node)

out = reverseLinkedList(third_node)
print(out.val)
# %%
