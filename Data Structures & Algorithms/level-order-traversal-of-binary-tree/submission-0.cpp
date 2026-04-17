/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> doublearr;
        if(root == nullptr) {
            return doublearr;
        }
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            vector<int> temp;
            int size= q.size();
            for(int i = 0 ; i < size; i++ ){
                TreeNode* tempnode= q.front();
                q.pop();
                temp.push_back(tempnode->val);
                if(tempnode->left != nullptr) q.push(tempnode->left);
                if(tempnode->right != nullptr) q.push(tempnode->right);
            }
            doublearr.push_back(temp);

        }
        return doublearr;
    }
};
