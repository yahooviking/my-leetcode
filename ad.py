word1 = "dadad"
word2 = "ghjkld"

m = len(word1)
n = len(word2)

i = 0
j = 0

res = ""

while (i<m or j<n):
    if i<m:
        res += word1[i]
        i += 1
    if j<n:
        res += word2[j]
        j += 1

a = res
