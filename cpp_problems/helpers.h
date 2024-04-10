#pragma once
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <set>
#include <queue>

using namespace std;

const int null = -123456789; // for purpose of leetcode, use an arbitrary int to represent null node in an int array

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

struct RedBackTree
{
    // TODO:
};

template <typename T>
struct MinHeap
{
    // TODO:
    vector<T> array;

public:
    void push(T &&item){};
    T pop(){};
    T top(){};

    MinHeap(vector<T> arr)
    {
        for (auto item : arr)
            push(item);
    };
};

template <typename T>
void sort_array(T arr[], size_t size)
{
    // TODO:
}

ListNode *array_to_llist(vector<int> array)
{
    ListNode head = ListNode();
    ListNode *node = &head;
    for (int num : array)
    {
        // have to use heap here since stack
        // gets deallocated as soon as out of scope
        node->next = new ListNode(num);
        node = node->next;
    }
    return head.next;
}

void print_llist(ListNode *head)
{
    while (head)
    {
        cout << head->val << "->";
        head = head->next;
    }
    cout << "null" << endl;
}

TreeNode *bfs_array_to_tree(vector<int> numbers)
{
    TreeNode *root;
    if (!numbers.size())
        return root;
    root = new TreeNode(numbers[0]);
    queue<TreeNode *> q;
    q.push(root);
    int i = 1, n = numbers.size();
    while (i < n)
    {
        TreeNode *curr = q.front();
        q.pop();
        if (i < n)
        {
            if (numbers[i] != null)
            {
                curr->left = new TreeNode(numbers[i]);
                q.push(curr->left);
            }
            i++;
        }

        if (i < n)
        {
            if (numbers[i] != null)
            {
                curr->right = new TreeNode(numbers[i]);
                q.push(curr->right);
            }
            i++;
        }
    }
    return root;
}


struct TrieNode {
    int max_suggestion;
    char value;
    TrieNode* children[26];  // 26 lower case letters
    bool is_end = false;
    vector<string> suggestions;

    TrieNode (char c, int max_s) {
        value = c;
        is_end = false;
        max_suggestion = max_s;
        for (int i=0; i<26; i++) {
            children[i] = nullptr;
        }
    }

    void insert_suggestion(string word) {
        if (suggestions.size() < max_suggestion) {
            suggestions.push_back(word);
        }
    }
    
};

struct Trie {
    int max_suggestions;
    TrieNode* root;
    vector<string> matching_words = {};

    Trie (int max_s) {
        max_suggestions = max_s;
        root = new TrieNode(-1, max_s);
    }

    void insert_word(string word) {
        TrieNode * current = root;
        for (char c: word) {
            int idx = c - 'a';
            if (!current->children[idx]) {
                current->children[idx] = new TrieNode(c, max_suggestions);
            }
            current = current->children[idx];
            current->insert_suggestion(word);
        }
        current->is_end = true;
    }

    void dfs(string current_word, TrieNode* node, int max_size){
        if (matching_words.size() == max_size) return;
        if (node->is_end) matching_words.push_back(current_word);
        for (TrieNode* child: node->children) {
            if (child) dfs(current_word + child->value, child, max_size);
        }
        return;
    }

    vector<string> get_starts_with(string word, int max_size=3) {
        matching_words.clear();

        TrieNode * current = root;
        for (char c: word) {
            int idx = c - 'a';
            if (!current -> children[idx]) return matching_words;
            current = current->children[idx];
        }

        // run dfs to search for the valid words in lexigcal order
        dfs(word, current, max_size);
        return matching_words;
    }
};
