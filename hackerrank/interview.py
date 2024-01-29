s = "hackerrank"
queries = [1,2,4,6]
lst = [0] * len(queries)

for count, ele in enumerate(queries):
    #print(count)
    #print(ele)
    for element in s:
        if element == s[ele]:
            lst[count] += 1

for i in range(len(lst)):
    if lst[i] < 2:
        lst[i] = -1

print(lst)
