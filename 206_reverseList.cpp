/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        ListNode *new_head = NULL;
        while(head !=NULL)
        {
            ListNode *next = head->next; //备份
            head->next = new_head; //更新地址
            new_head = head;     //更新值
            head = next;   //遍历
        }
        return new_head;
    }
};