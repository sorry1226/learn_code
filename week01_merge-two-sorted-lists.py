# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
        return l1 or l2
    if l1.val <= l2.val:  # 递归调用
        l1.next = mergeTwoLists(l1.next,l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1,l2.next)
        return l2





if __name__ == '__main__':
    print('11')
    # print(l1)
