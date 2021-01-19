p_phrase = "was it a car or a cat I saw"

p_list = p_phrase.split(" ")
rp_list = p_list.reverse
r_phrase=""
if p_list == rp_list:
    r_phrase =r_phrase+ p_phrase
    
print(r_phrase)    
