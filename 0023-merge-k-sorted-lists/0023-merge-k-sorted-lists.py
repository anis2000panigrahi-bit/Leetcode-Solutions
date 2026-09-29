class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        def merge(list1, list2):
            dummy = ListNode(0)
            current = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next

                current = current.next

            if list1:
                current.next = list1
            else:
                current.next = list2

            return dummy.next

        result = None

        for i in range(len(lists)):
            result = merge(result, lists[i])

        return result