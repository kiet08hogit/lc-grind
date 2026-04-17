/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(!head) return nullptr;
        Node * curr= head;
        unordered_map<Node*, Node*> storingll;
        while(curr!=nullptr){   
            storingll[curr]= new Node(curr->val);
            curr=curr->next;
        }

        curr= head;
        while (curr!=nullptr){

            storingll[curr]->next= storingll[curr->next];
            storingll[curr]->random= storingll[curr->random];
            curr= curr->next;
        }

        return storingll[head];
    }
};
