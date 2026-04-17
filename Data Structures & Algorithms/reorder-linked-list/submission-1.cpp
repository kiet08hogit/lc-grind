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
    void reorderList(ListNode* head) {
       if (head == nullptr) return;
       ListNode * fast= head->next;
       ListNode * slow = head;
       while (fast && fast->next){
        slow = slow ->next;
        fast= fast->next->next;
       }
       ListNode * secondhalf= slow->next;
       ListNode * prev= nullptr;
       slow->next = nullptr;
       while (secondhalf != nullptr){
            ListNode * temp = secondhalf->next;
            secondhalf->next =prev;
            prev= secondhalf;     
            secondhalf= temp;
       }

        ListNode * first= head;
        while (prev!= nullptr){
            ListNode * temp1 = first->next;
            ListNode * temp2= prev->next;
            first->next= prev;
            prev->next= temp1;
            first= temp1;
            prev= temp2;
        }

    }
};
