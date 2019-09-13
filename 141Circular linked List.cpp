/* first solution
class Solution {
public:
    bool hasCycle(ListNode *head) 
    {
        std::set<ListNode *> node_set;
        while(head)
        {
            if(node_set.find(head)!=node_set.end())
            {
                return true;
            }
            node_set.insert(head);
            head = head->next;
        }
        return false;
    }
};*/
class Solution {
public:
    bool hasCycle(ListNode *head) 
    {
        ListNode *fast = head;
        ListNode *slow = head;
        while(fast)
        {
            slow = slow->next;
            fast = fast->next;
            
            if(!fast)
            {
                return NULL;
            }
            fast = fast->next;
            if(fast == slow)
            {
                return true;
            }
        }
        return false;
    }
};