s = open('MATHSYS_oefeningen.tex','rb').read()
for i,b in enumerate(s):
    if b>127:
        start=max(0,i-10)
        end=min(len(s),i+40)
        chunk=s[start:end]
        print(i, b, chunk)
        break

# List all unique non-ascii bytes
bytes_set = sorted(set([b for b in s if b>127]))
print('\nUnique non-ascii bytes:', bytes_set)
# print occurrences with context for a few
for b in bytes_set[:10]:
    print('\nByte:', b)
    for i in range(len(s)):
        if s[i]==b:
            start=max(0,i-20); end=min(len(s),i+20)
            print(i, s[start:end])
            break
