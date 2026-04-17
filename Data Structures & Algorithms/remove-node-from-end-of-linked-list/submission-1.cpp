/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* first = head;
        ListNode * second = head;
        int track=0;
        while(first != nullptr){
            first=first->next;
            track++;
        }
    
        int runtime= track-n;
        if(runtime == 0){
            return head->next;
        }
        for (int i =0 ; i < track-1; i ++){
            if((i+1) == runtime){
                second->next = second->next->next;
                break;
            }

            second= second->next;
        }
        return head;
    }
};
