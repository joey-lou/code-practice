#include "helpers.h"

class Solution
// LeetCode 75 (all easy and medium)
{
public:
    int maxOperations(vector<int> &nums, int k)
    {
        // can sort the array and use two pointer to incrementally
        // loop over the sorted array
        // int i = 0, j = nums.size() - 1;
        // sort(nums.begin(), nums.end());
        // int retval = 0;
        // while (i < j)
        // {
        //     const int sum = nums[i] + nums[j];
        //     if (sum > k)
        //         j--;
        //     else if (sum < k)
        //         i++;
        //     else
        //     {
        //         retval++;
        //         i++;
        //         j--;
        //     }
        // }
        // return retval;

        // alternatively use hashmap
        unordered_map<int, int> map;
        int retval = 0;
        for (int num : nums)
        {
            const int remain = k - num;
            if (map.find(remain) != map.end() && map[remain])
            {
                map[remain]--;
                retval++;
            }
            else
            {
                if (map.find(num) != map.end())
                {
                    map[num]++;
                }
                else
                {
                    map.insert({num, 1});
                }
            }
        }
        return retval;
    }

    int maxVowels(string s, int k)
    {
        int i = 0;
        int num_vowels = 0;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        int retval = 0;

        for (; i < k && i < s.size(); i++)
        {
            if (vowels.find(s[i]) != vowels.end())
            {
                num_vowels++;
                retval = retval > num_vowels ? retval : num_vowels;
            }
        }

        for (; i < s.size(); i++)
        {
            const int j = i - k;
            if (vowels.find(s[j]) != vowels.end())
            {
                num_vowels--;
            }
            if (vowels.find(s[i]) != vowels.end())
            {
                num_vowels++;
                retval = max(retval, num_vowels);
            }
        }
        return retval;
    }

    int pivotIndex(vector<int> &nums)
    {
        int total = 0;
        for (int num : nums)
        {
            total += num;
        }
        int left_sum = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            const int right_sum = total - left_sum - nums[i];
            if (right_sum == left_sum)
                return i;
            left_sum += nums[i];
        }
        return null;
    }

    vector<vector<int>> findDifference(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> set2(nums2.begin(), nums2.end());
        vector<vector<int>> retval = {{}, {}};
        for (int num1 : set1)
        {
            if (set2.find(num1) == set2.end())
            {
                retval[0].push_back(num1);
            }
        }
        for (int num2 : set2)
        {
            if (set1.find(num2) == set1.end())
            {
                retval[1].push_back(num2);
            }
        }
        return retval;
    }

    bool closeStrings(string word1, string word2)
    {
        // simply need to make sure there are equivalent number
        // of characters and the number of counts match
        unordered_map<char, int> char_count1, char_count2;
        unordered_map<int, int> cnt_count1;

        for (char char1 : word1)
            char_count1[char1]++;
        for (char char2 : word2)
            char_count2[char2]++;

        for (auto pair : char_count1)
            cnt_count1[pair.second]++;
        for (auto pair : char_count2)
            cnt_count1[pair.second]--;

        for (auto pair : cnt_count1)
        {
            if (pair.second != 0)
                return false;
        }
        return true;
    }

    bool row_column_equal(vector<vector<int>> &grid, const int row, const int col, const int n)
    {
        for (int k = 0; k < n; k++)
        {
            if (grid[k][col] != grid[row][k])
                return false;
        }
        return true;
    }

    int equalPairs(vector<vector<int>> &grid)
    {
        // could potentially do custom hash, for instance, use the number and order
        // such that we only do O(mn)
        int retval = 0;
        const int n = grid.size();
        for (int r = 0; r < n; r++)
        {
            for (int c = 0; c < n; c++)
            {
                if (row_column_equal(grid, r, c, n))
                    retval++;
            }
        }
        return retval;
    }

    string removeStars(string s)
    {
        int i = 0, j = 0, n = s.length();

        while (j < n)
        {
            if (s[j] != '*')
            {
                swap(s[i], s[j]);
                i++;
            }
            else
            {
                i--;
            }
            j++;
        }
        s.erase(i); // [i, j)
        return s;
    }

    ListNode *deleteMiddle(ListNode *head)
    {
        // use two pointers
        ListNode *curr = head, *jump = head, *prev = nullptr;
        while (jump && jump->next)
        {
            prev = curr;
            curr = curr->next;
            jump = jump->next->next;
        }
        // single node case
        if (!prev)
            return nullptr;
        prev->next = curr->next;
        return head;
    }

    ListNode *oddEvenList(ListNode *head)
    {
        ListNode odd_head = ListNode();
        ListNode even_head = ListNode();

        ListNode *even_ptr, *odd_ptr;
        even_ptr = &even_head;
        odd_ptr = &odd_head;

        int i = 0;
        while (head)
        {
            if (i % 2)
            {
                odd_ptr->next = head;
                odd_ptr = odd_ptr->next;
            }
            else
            {
                even_ptr->next = head;
                even_ptr = even_ptr->next;
            }
            i++;
            head = head->next;
        }
        even_ptr->next = odd_head.next;
        if (odd_ptr)
            odd_ptr->next = nullptr;
        return even_head.next;
    }

    ListNode *reverseList(ListNode *head)
    {
        ListNode *curr = head, *prev = nullptr, *tmp;
        while (curr)
        {
            tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }
        if (!prev)
            return head;
        return prev;
    }

    int pairSum(ListNode *head)
    {
        // maintain stack and pop once half way
        vector<int> stack;
        int retval = 0;
        ListNode *curr = head, *jump = head;

        while (jump && jump->next)
        {
            stack.push_back(curr->val);
            jump = jump->next->next;
            curr = curr->next;
        }

        while (curr)
        {
            retval = max(curr->val + stack.back(), retval);
            stack.pop_back();
            curr = curr->next;
        }
        return retval;
    }

    vector<int> in_order_search(TreeNode *root)
    {
        // use stack
        vector<TreeNode *> stack = {root};
        vector<int> order;
        bool is_leaf;
        TreeNode *tmp;
        while (stack.size())
        {
            is_leaf = true;
            tmp = stack.back();
            stack.pop_back();
            if (tmp->right)
            {
                stack.push_back(tmp->right);
                is_leaf = false;
            }
            if (tmp->left)
            {
                stack.push_back(tmp->left);
                is_leaf = false;
            }
            if (is_leaf)
            {
                order.push_back(tmp->val);
            }
        }
        return order;
    }

    void in_order_search_recurse(TreeNode *node, vector<int> &order)
    {
        // use recursion
        if (!node)
            return;
        bool is_leaf = true;
        if (node->left)
        {
            in_order_search_recurse(node->left, order);
            is_leaf = false;
        }
        if (node->right)
        {
            in_order_search_recurse(node->right, order);
            is_leaf = false;
        }
        if (is_leaf)
            order.push_back(node->val);
    }

    bool leafSimilar(TreeNode *root1, TreeNode *root2)
    {
        // traverse both trees simultaneously
        vector<int> tree1_order = in_order_search(root1);
        vector<int> tree2_order;
        in_order_search_recurse(root2, tree2_order);
        return tree1_order == tree2_order;
    }

    int singlePathSumRecurse(TreeNode *node, int currSum)
    {
        if (!node)
            return 0;
        return singlePathSumRecurse(node->left, currSum - node->val) + singlePathSumRecurse(node->right, currSum - node->val) + (node->val == currSum);
    }

    int pathSum(TreeNode *root, int targetSum)
    {
        // start at each new node as root
        if (!root)
            return 0;
        return singlePathSumRecurse(root, targetSum) + pathSum(root->left, targetSum) + pathSum(root->right, targetSum);
    }

    int longestZigZag(TreeNode *root)
    {
        // use queue to run bfs on binary tree
        // at each node, we have at most two choices, continue on
        // with previous path, or start in the other direction anew,
        // append both to the queue (no separate child nodes essentially)
        struct ZigZagData
        {
            TreeNode *node = nullptr;
            int leftMax = 0; // if prev transition was towards left
            int rightMax = 0;
            ZigZagData(TreeNode *n, int lm, int rm) : node(n), leftMax(lm), rightMax(rm) {}

            int currMax()
            {
                return leftMax > rightMax ? leftMax : rightMax;
            }
        };

        queue<ZigZagData> q;
        q.push(ZigZagData(root, 0, 0));
        int maxLength = 0;
        while (!q.empty())
        {
            ZigZagData zzd = q.front();
            q.pop();
            maxLength = max(maxLength, zzd.currMax());
            TreeNode *node = zzd.node;
            if (node->right)
            {
                q.push(ZigZagData(node->right, 0, zzd.leftMax + 1));
            }
            if (zzd.node->left)
            {
                q.push(ZigZagData(node->left, zzd.rightMax + 1, 0));
            }
        }
        return maxLength;
    }

    int maxLevelSum(TreeNode *root)
    {
        int levelCnt, i, levelSum, maxSum, currLevel = 1, maxSumLevel = -1;
        queue<TreeNode *> q;
        q.push(root);

        while (!q.empty())
        {
            levelCnt = q.size();
            // one level at a time
            levelSum = 0;
            for (i = 0; i < levelCnt; i++)
            {
                TreeNode *node = q.front();
                q.pop();
                levelSum += node->val;
                if (node->left)
                    q.push(node->left);
                if (node->right)
                    q.push(node->right);
            }

            // check sums
            if (maxSumLevel == -1)
            {
                maxSum = levelSum;
                maxSumLevel = currLevel;
            }
            else if (maxSum < levelSum)
            {
                maxSum = levelSum;
                maxSumLevel = currLevel;
            }
            currLevel++;
        }
        return maxSumLevel;
    }

    TreeNode *deleteNode(TreeNode *root, int key)
    {
        // two step algo
        // 1. find the node with matching value O(h) for searching a key in BST
        // 2. delete the found node (by replacing it with largest node in left subtree)
        if (!root)
            return nullptr;

        if (root->val == key)
        {
            if (root->left)
            {
                TreeNode *replaceNode = root->left;
                while (replaceNode->right)
                {
                    replaceNode = replaceNode->right;
                }
                root->val = replaceNode->val;
                root->left = deleteNode(root->left, replaceNode->val);
            }
            else if (root->right)
            {
                TreeNode *replaceNode = root->right;
                while (replaceNode->left)
                {
                    replaceNode = replaceNode->left;
                }
                root->val = replaceNode->val;
                root->right = deleteNode(root->right, replaceNode->val);
            }
            else
            {
                return nullptr;
            }
        }
        else if (root->val > key)
        {
            root->left = deleteNode(root->left, key);
        }
        else
        {
            root->right = deleteNode(root->right, key);
        }
        return root;
    }

    int nearestExit(vector<vector<char>> &maze, vector<int> &entrance)
    {
        queue<vector<int>> q;
        q.push({entrance});
        int m = maze.size(), n = maze[0].size();
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int steps = 0;
        maze[entrance[0]][entrance[1]] = '+';
        while (!q.empty())
        {
            int size = q.size();
            for (int _ = 0; _ < size; _++)
            {
                vector<int> cell = q.front();
                q.pop();
                for (vector<int> dir : directions)
                {
                    int up = dir[0], left = dir[1];
                    vector<int> next_cell = {cell[0] + up, cell[1] + left};
                    if (next_cell[0] < 0 || next_cell[0] >= m || next_cell[1] < 0 || next_cell[1] >= n)
                    {
                        if (steps != 0)
                            return steps;
                    }
                    else
                    {
                        if (maze[next_cell[0]][next_cell[1]] == '.')
                        {
                            q.push(next_cell);
                            maze[next_cell[0]][next_cell[1]] = '+'; // mark as visited
                        }
                    }
                }
            }
            steps++;
        }
        return -1;
    }

    long long maxScore(vector<int> &nums1, vector<int> &nums2, int k)
    {
        // TODO: review, this is a difficult problem
        // the key is to think of the greedy algo, we can sort both arrays based off nums2
        // at each index [j] of nums2, we can assert that nums2[j] is the best min we can get
        // to multiply from all nums2 sequences up till index [j], and the heap of nums1 using
        // all elements up till [j] will ensure we get the best sum we can get.
        // now, it is a matter of iterating j and updating heap/min

        vector<pair<int, int>> pairs;
        for (int i = 0; i < nums1.size(); i++)
        {
            pairs.push_back({nums2[i], nums1[i]});
        }
        sort(pairs.rbegin(), pairs.rend()); // sort in ascending order

        priority_queue<int> prio_q; // max heap by default

        long long pq_sum = 0;
        for (int i = 0; i < k - 1; i++)
        {
            prio_q.push(-pairs[i].second);
            pq_sum += pairs[i].second;
        }

        long long retval = 0;
        for (int i = k - 1; i < nums1.size(); i++)
        {
            prio_q.push(-pairs[i].second);
            pq_sum += pairs[i].second;
            retval = max(retval, (long long)pq_sum * pairs[i].first);
            pq_sum += prio_q.top(); // it is negative
            prio_q.pop();
        }
        return retval;
    }

    long long totalCost(vector<int> &costs, int k, int candidates)
    {
        // brute force would have runtime O(k * c)
        // if we use heap, then O(k * log(c))

        priority_queue<int> left_pq, right_pq; // max heap by default
        long long cost = 0;
        // need to keep two heaps, so we know which heap to update
        int i = 0, j = costs.size() - 1;

        while (i <= j && candidates)
        {
            left_pq.push(-costs[i]);
            if (i != j)
                right_pq.push(-costs[j]);
            i++;
            j--;
            candidates--;
        }

        while (k)
        {
            if (right_pq.empty() && left_pq.empty())
                break;
            if (left_pq.empty() || (!right_pq.empty() && right_pq.top() > left_pq.top()))
            {
                cost -= right_pq.top();
                right_pq.pop();
                if (i <= j)
                {
                    right_pq.push(-costs[j]);
                    j--;
                }
            }
            else
            {
                cost -= left_pq.top();
                left_pq.pop();
                if (i <= j)
                {
                    left_pq.push(-costs[i]);
                    i++;
                }
            }
            k--;
        }
        return cost;
    }

    int potions_usable(vector<int> &sorted_potions, int min_strength)
    {
        int l = 0, u = sorted_potions.size() - 1;
        if (min_strength > sorted_potions.back())
        {
            return 0;
        }
        while (l < u)
        {
            int mid = l + (u - l) / 2;
            if (sorted_potions[mid] < min_strength)
            {
                l = mid + 1;
            }
            else
            {
                u = mid;
            }
        }
        return sorted_potions.size() - l;
    }

    vector<int> successfulPairs(vector<int> &spells, vector<int> &potions, long long success)
    {
        // brute force is O(mn)
        // if we sort potions and do bisection to find the index of
        // the minimum strength potion required, we can do O(nlogn + mlogn)
        sort(potions.begin(), potions.end());
        vector<int> successes;
        for (int spell : spells)
        {
            successes.push_back(potions_usable(potions, (success + spell - 1) / spell));
        }
        return successes;
    }

    int minFlips(int a, int b, int c)
    {
        int flips = 0;
        for (int i = 0; i < 30; i++)
        {
            // cout << (a & 1) << "," << (b & 1) << "," << (c & 1) << endl;
            if (((a & 1) | (b & 1)) == (c & 1)) {}
            else if (c & 1)
                flips++;
            else
            {
                flips += a & 1;
                flips += b & 1;
            }
            a >>= 1;
            b >>= 1;
            c >>= 1;
        }
        return flips;
    }

    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());

        vector<vector<string>> retval;
        Trie t = Trie(3);
        for (string p: products) {
            t.insert_word(p);
        }

        TrieNode * current = t.root;
        for (char c: searchWord) {
            int idx = c - 'a';
            if (current && current->children[idx]) {
                current = current->children[idx];
                retval.push_back(current->suggestions);
            } else {
                current = nullptr;
                retval.push_back({});
            }
        }
        return retval;
    }

    int minCut(string s) {
        // we can use dynamic programming
        // define c_i to be the mincut required for the substring s[0,i)
        // from top down, we can see for some j > i, and if s[i-1,j) is palindrome
        // then c_j is at most c_i + 1.
        // with this we can already recursively compute for full string s, but
        // this result in a lot of repeated checks for palindrome
        // for instance substring s[4,6) will be checked as part of s[3,7) and s[2,8)
        // this is because the process for verifying palindrome is repatitive

        // think in another way (bottom up), we can start from c_1, and move up, and instead of
        // checking treating c_i as the starting/end point, we treat it as mid point of palindrome

        int n = s.size();
        if (n < 2) return 0;
        vector<int> dp(n+1, n);  // at most n cuts, so safe as upper bound
        dp[0] = -1;

        for (int i=1; i<=n; i++) {
            // i is the center node for odd case
            for (int r=0; r<min(i, n+1-i); r++) {
                if (s[i-1-r] ==s[i-1+r]) dp[i+r] = min(dp[i+r], dp[i-r-1] + 1);
                else break;
            }
            // i is the left node for even case
            for (int r=0; r<min(i, n+1-i); r++) {
                if (s[i-1-r] == s[i+r]) dp[i+r+1] = min(dp[i+r+1], dp[i-r-1] + 1);
                else break;
            }
        }
        return dp[n];
    }

    char shift(char x, int shift) {
        // 26 characters total, z(100)->a(74) (1+100-74)%26+74
        return (x - 'a' + shift) % 26 + 'a';
    }

    string shiftingLetters(string s, vector<int>& shifts) {
        // we can calculate the shift needed at each point
        int n = shifts.size();
        if (!n) return s;
        vector<int> cum_shifts(n, 0);
        cum_shifts[0] = shifts[0];
        for (int i=1; i<n; i++) {
            cum_shifts[i] = (cum_shifts[i-1] + shifts[i]) % 26;
        }
        for (int i=0; i<n; i++) {
            s[i] = shift(s[i], cum_shifts[i]);
        }
        return s;
    }
};

class SmallestInfiniteSet
{
    int unpopped_smallest;
    set<int> added_back_set; // only if it has been popped before

public:
    SmallestInfiniteSet()
    {
        unpopped_smallest = 1;
        added_back_set.clear();
    }

    int popSmallest()
    {
        if (added_back_set.size())
        {
            int smallest = *added_back_set.begin();
            added_back_set.erase(smallest);
            return smallest;
        }
        else
        {
            unpopped_smallest++;
            return unpopped_smallest - 1;
        }
    }

    void addBack(int num)
    {
        if (num < unpopped_smallest)
            added_back_set.insert(num);
    }
};

int main(int argc, char *argv[])
{
    Solution sol;
    // vector<int> vec = {1, 2, 3, 2, 1};
    // cout << sol.maxOperations(vec, 6) << endl;
    // cout << sol.maxVowels("aeiou", 2) << endl;
    // cout << sol.pivotIndex(vec) << endl;
    // cout << sol.closeStrings("abc", "bca") << endl;
    // vector<vector<int>> grid = {{3, 2, 1}, {1, 7, 6}, {2, 7, 7}};
    // cout << sol.equalPairs(grid) << endl;
    // print_llist(sol.reverseList(array_to_llist({1, 2, 3, 4, 5})));
    // cout << sol.pairSum(array_to_llist({2, 3, 4, 5})) << endl;
    // cout << sol.leafSimilar(bfs_array_to_tree({3, 5, 1, 6, 2, 9, 8, null, null, 7, 4}), bfs_array_to_tree({3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8}));
    // cout << sol.pathSum(bfs_array_to_tree({1, null, 2, null, 3, null, 4, null, 5}), 3);
    // cout << sol.pathSum(bfs_array_to_tree({1, -2, -3, 1, 3, -2, null, -1}), -1);
    // cout << sol.longestZigZag(bfs_array_to_tree({1, null, 1, 1, 1, null, null, 1, 1, null, 1, null, null, null, 1}));
    // cout << sol.maxLevelSum(bfs_array_to_tree({1, 7, 0, 7, -8, null, null}));
    // vector<vector<char>> maze = {{'+', '+', '.', '+'},
    //                              {'.', '.', '.', '+'},
    //                              {'+', '+', '+', '.'}};
    // vector<int> entrance = {1, 2};
    // cout << sol.nearestExit(maze, entrance);
    // vector<int> costs = {1, 2, 4, 1};
    // cout << sol.totalCost(costs, 3, 3);
    // vector<int> spells = {5, 1, 3};
    // vector<int> potions = {1, 2, 3, 4, 5};
    // for (int s : sol.successfulPairs(spells, potions, 7))
    // {
    //     cout << s << ",";
    // }
    // cout << endl;
    // cout << sol.minFlips(*argv[1], *argv[2], *argv[3]) << endl;

    // Trie t = Trie();
    // t.insert_word("aa");
    // t.insert_word("aaa");
    // t.insert_word("aaaa");
    // t.insert_word("ab");
    // t.insert_word("abb");
    // t.insert_word("ac");
    // for (auto s: t.get_starts_with("a", 3)) {
    //     cout << s << endl;
    // }
    // cout << sol.minCut("aab");
    vector<int> shifts = {1};
    cout << sol.shiftingLetters("z", shifts);
}