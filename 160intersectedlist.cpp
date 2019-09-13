/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
int get_list_length(ListNode *head) //compute the length of the list
{
    int len = 0;
    while(head)
    {
        len ++;
        head = head->next;
    }
    return len;
}

ListNode *forward_long_list(int long_len, int short_len, ListNode *head)//shift the longer list
{
    int delta = long_len - short_len;
    while(head && delta)
    {
        head = head ->next;
        delta --;
        
    }
    return head;
}
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) 
    {
        int list_A_len = get_list_length(headA);
        int list_B_len = get_list_length(headB);
        if(list_A_len > list_B_len)
        {
            headA = forward_long_list(list_A_len,list_B_len, headA);
        }
        else
        {
            headB = forward_long_list(list_B_len,list_A_len, headB);
        }
        while(headA && headB)
        {
            if(headA == headB) // find the intersection 
            {
                return headA;
            }
            headA = headA -> next; // otherwise shift
            headB = headB -> next;
        }
        return NULL;
       
    }
};