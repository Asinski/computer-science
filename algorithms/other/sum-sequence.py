seq = list(map(int, input().split()))
seqsum = 0
for i in range(len(seq)):
    seqsum += seq[i]
print(seqsum)
