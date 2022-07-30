list_minus = input().split('-')
ans = 0
for i in range(len(list_minus)):
    plus = sum(map(int, list_minus[i].split('+')))
    if i == 0:
        ans += plus
    else:
        ans -= plus
print(ans)