from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def constructTree(nums):
    if not nums:
        return
    root = TreeNode(nums[0])
    q = deque([root])
    i = 1
    while i < len(nums):
        cur = q.popleft()
        if nums[i] != 'null':
            left = TreeNode(nums[i])
            cur.left = left
            q.append(left)
        i += 1
        if i < len(nums) and nums[i] != 'null':
            right = TreeNode(nums[i])
            cur.right = right
            q.append(right)
        i += 1
    return root

def traverse(root):
    if not root:
        return
    traverse(root.left)
    print(root.val, end=" ")
    traverse(root.right)

# nums = [1, 'null', 1, 'null', 1, 2]
# root = constructTree(nums)
# traverse(root)



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def numsToLinkedList(nums):
    if not nums:
        return
    dummy = ListNode()
    p = dummy
    for i in range(len(nums)):
        cur = ListNode(nums[i])
        p.next = cur
        p = p.next
    return dummy.next

def printLinkedList(head):
    while head:
        print(head.val, end=" ")
        head = head.next

nums = [1,4,2,5,6]
head = numsToLinkedList(nums)
printLinkedList(head)
