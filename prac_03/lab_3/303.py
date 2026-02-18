s = input().strip()

d = {
    "ZER":"0","ONE":"1","TWO":"2","THR":"3","FOU":"4",
    "FIV":"5","SIX":"6","SEV":"7","EIG":"8","NIN":"9"
}
rd = {v:k for k,v in d.items()}

for op in "+-*":
    if op in s:
        a, b = s.split(op)
        break

def conv(x):
    return int(''.join(d[x[i:i+3]] for i in range(0, len(x), 3)))

res = eval(f"{conv(a)}{op}{conv(b)}")

print(''.join(rd[c] for c in str(res)))