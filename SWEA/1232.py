class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def in_order(node):

    if not (node.data == '+' or node.data == '-' or node.data == '*' or node.data == '/'):
        return node.data

    oper1 = float(in_order(node.left))
    oper2 = float(in_order(node.right))
    if node.data == '+':
        return oper1 + oper2
    elif node.data == '-':
        return oper1 - oper2
    elif node.data == '*':
        return oper1 * oper2
    else:
        return oper1 / oper2

node_list = []

for test_case in range(1, 11):
    res = 0
    N = int(input()) # 정점의 개수

    for i in range(N + 1):
        node_list.append(Node())

    for i in range(N):
        arr = input().split()

        idx = int(arr[0]) # 정점번호
        val = arr[1] # 정점의 값

        node_list[idx].data = val

        if arr[1] == '+' or arr[1] == '-' or arr[1] == '*' or arr[1] == '/':
            left_idx = int(arr[2]) # 기호일때 왼쪽 자식 노드 번호
            right_idx = int(arr[3]) # 기호일때 오른쪽 자식 노드 번호

            node_list[idx].left = node_list[left_idx]
            node_list[idx].right = node_list[right_idx]

    res = in_order(node_list[1])

    print('#{} {}'.format(test_case, int(res)))