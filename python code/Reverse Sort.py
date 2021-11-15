q = int(input())
for tc in range(q):
    n = int(input())
    s = input()
    t = ''.join(sorted(s))
    ans = []
    for i in range(len(s)):
        if s[i] != t[i]: 
            ans.append(i)
    val = 1 if len(ans) > 0 else 0
    print(val)
    if val > 0:
        print(len(ans), end = " ")
    for elem in range(len(ans)):
        print(ans[elem] + 1, end = " ")
    print()
