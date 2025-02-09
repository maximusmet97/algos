#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def find_first_occurence(haystack,needle):
    substr_len = len(needle)

    for idx in range(0,len(haystack)):
        if haystack[idx:idx+substr_len] == needle:
            return idx
    
    return -1

print(find_first_occurence("mississippi","issi"))
