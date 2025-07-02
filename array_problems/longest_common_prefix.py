def longestPrefix(strs):
    if not strs:
        return ""
    sort_strs = sorted(strs)
    res = ""
    first = sort_strs[0]
    last = sort_strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return res
        res = res + first[i]
    return res





strs = ["flower","flow","flight"]
result = longestPrefix(strs)
print(result)
