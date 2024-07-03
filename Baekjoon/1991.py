import sys

input = sys.stdin.readline
N = int(input())

tree = {}
for i in range(N):
    root, left, right = input().strip().split()
    tree[root] = left, right  # {'A': ('B', 'C')}

def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])

def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')

preorder('A')
print('')
inorder('A')
print('')
postorder('A')
