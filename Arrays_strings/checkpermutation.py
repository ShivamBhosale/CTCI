def check_permutation(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    if len(str1) != len(str2):
        return False
    else:
        if(sorted(str1) == sorted(str2)):
            return True
        
    return False
        
print(check_permutation("Hello","lloeHt"))