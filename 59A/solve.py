stri = input()

test = [1 if x.isupper() else 0 for x in stri]
if test.count(0) >= test.count(1):
    print(stri.lower())
else:
    print(stri.upper())