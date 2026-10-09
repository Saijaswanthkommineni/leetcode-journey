class Solution:
 def hasCycle(self,head:Optional[ListNode])->bool:
  st=set()
  while head:
   if head in st:return 1
   st.add(head);head=head.next
  return 0