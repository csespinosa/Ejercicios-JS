def count_substrings(string: str, sub_string: str):
    count = 0
    start = 0
    
    while True:
        index = string.find(sub_string, start)
        
        if index == -1:
            break
        
        count +=1
        start = index + 1
        
    return count
        
print(count_substrings("ABCDCDC", "CDC"))