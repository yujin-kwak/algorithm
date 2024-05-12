
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def in_order(node):
    global word
    if node == None:
        return

    in_order(node.left)
    word += node.data
    in_order(node.right)
    return

node_list = []

for test_case in range(1, 11):
    node_list = []
    N = int(input())
    for i in range(N + 1):
        node_list.append(Node())

    for i in range(N):
        in_arr = input().split()

        idx = int(in_arr[0])
        data = in_arr[1]
        left_idx = None
        right_idx = None
        if len(in_arr) >= 3 :
            left_idx = int(in_arr[2])
        if len(in_arr) >= 4 :
            right_idx = int(in_arr[3])

        node_list[idx].data = data # 노드 번호
        if left_idx != None:
            node_list[idx].left = node_list[left_idx]
        if right_idx != None:
            node_list[idx].right = node_list[right_idx]

    word = ""
    in_order(node_list[1])

    print('#{} {}'.format(test_case, word))