class Solution:
 def detectCycle(self,head:Optional[ListNode])->Optional[ListNode]:
  f=s=head
  while f and f.next:
   s=s.next;f=f.next.next
   if s==f:
    st=head
    while st!=s:st=st.next;s=s.next
    return st
  return None