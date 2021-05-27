s = 'show how to index into sequences'.split()
s
# ['show', 'how', 'to', 'index', 'into', 'sequences']
s[0]
# 'show'
s[5]
# 'sequences'
s[-1]
# 'sequences'
s[-2]
# 'into'
s[-6]
# 'show'

print('----------------')

s[1:4]
# ['how', 'to', 'index']
s[1:-1]
# ['how', 'to', 'index', 'into']
s[:3]
# ['show', 'how', 'to']
s[:3] + s[3:] == s
# True
full_slice = s[:]
full_slice
# ['show', 'how', 'to', 'index', 'into', 'sequences']
full_slice == s
# True
full_slice is s
# False

print('----------------')

u = s.copy()
v = list(s)
u
# ['show', 'how', 'to', 'index', 'into', 'sequences']
v
# ['show', 'how', 'to', 'index', 'into', 'sequences']


s = 'show how to index into sequences'.split()
s
# ['show', 'how', 'to', 'index', 'into', 'sequences']
s[::2]
# ['show', 'to', 'into']


s = 'show how to index into sequences'.split()
s
# ['show', 'how', 'to', 'index', 'into', 'sequences']
s[::-1]
# ['sequences', 'into', 'index', 'to', 'how', 'show']
