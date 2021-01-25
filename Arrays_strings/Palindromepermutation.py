def pal_perm(phrase):
    phrase = phrase.replace(" ", "").lower()

    d = dict()

    for i in phrase:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k,v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False

    return True

print(pal_perm("racecar"))