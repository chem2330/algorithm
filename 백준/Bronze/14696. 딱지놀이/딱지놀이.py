N = int(input())
score = [0, 1, 2e+2, 3e+4, 4e+6]
for _ in range(N):
    a_total = 0
    b_total = 0
    a, *card_list_a = list(map(int, input().split()))
    b, *card_list_b = list(map(int, input().split()))
    for card_a in card_list_a:
        a_total += score[card_a]
    for card_b in card_list_b:
        b_total += score[card_b]

    if a_total > b_total:
        print("A")
    if a_total < b_total:
        print("B")
    if a_total == b_total:
        print("D")