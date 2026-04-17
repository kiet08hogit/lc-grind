/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node == nullptr) return nullptr;
        unordered_map<Node*,Node*> tracking;
        return dfs(node,tracking);
        
    }

    Node* dfs(Node * vert,unordered_map<Node*,Node*> & tracking){
        if (!vert) return nullptr;

        if ( tracking.count(vert)) return tracking[vert];
            Node * newvert= new Node(vert->val);
            tracking[vert]= newvert;
            for (Node * neighbor : vert->neighbors){
                dfs(neighbor, tracking);
                tracking[vert]->neighbors.push_back(tracking[neighbor]);
            }
        return tracking[vert];
    }
};
