inString = "2023-07-15 07:03:46.197 OUT: 8=FIX.4.49=5735=034=15249=PIAFIX_OM52=20230715-07:03:46.19756=DBS10=221"

count = 0
for char in inString:
    if char == '\x01':
        count += 1

print(count)