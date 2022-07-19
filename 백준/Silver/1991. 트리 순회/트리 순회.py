N = int(input())

P = [0] * (N + 1)
C1 = [0] * (N + 1)
C2 = [0] * (N + 1)

for _ in range(N):
    a, b, c = map(lambda x: ord(x) - 64, input().split())
    if b != -18:
        P[b] = a
        C1[a] = b
    if c != -18:
        P[c] = a
        C2[a] = c


def preorder(root):
    global pre_order
    if root != 0:
        pre_order.append(chr(root + 64))
        preorder(C1[root])
        preorder(C2[root])


def inorder(root):
    global in_order
    if root != 0:
        inorder(C1[root])
        in_order.append(chr(root + 64))
        inorder(C2[root])


def postorder(root):
    global post_order
    if root != 0:
        postorder(C1[root])
        postorder(C2[root])
        post_order.append(chr(root + 64))


pre_order = []
preorder(1)
print(''.join(pre_order))

in_order = []
inorder(1)
print(''.join(in_order))


post_order = []
postorder(1)
print(''.join(post_order))