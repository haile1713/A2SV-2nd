class Solution {
public:
    string reverseParentheses(string s) {
        
        stack<int>match;
        int n = s.size ();
        for (int i=0;i<n;i++){
            if (s[i]== '(') match.push (i);
            else if (s[i] == ')'){
                int start = match.top() + 1;
                int end =i;
                reverse(s.begin()+start,s.begin()+end);
                match.pop();
            }
        }
        string ans = "";
        for (int i=0;i<n;i++){
            if (s[i]=='(' || s[i]==')') continue;
            else ans.push_back (s[i]);
        }
        return ans;
    }
};
