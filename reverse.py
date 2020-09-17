# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss):
    # Write code here
    if len(string) == 0:
        return ""
    
    return string[-1] + reverse(string[:-1])
#explanation
# r + reverse('compute')
#     e + reverse('comput')
#         t + reverse('compu')
#             u + reverse('comp')
#                 p + reverse('com')
#                     m + reverse('co')
#                         o + reverse('c')
#                             c + reverse('')

# another solution
# _____________________________________
# def reverse(ss):
#     # Write code here
#     if len(ss) == 0:
#         return ss
#     else:
#         # print(ss[1:])
#         return reverse(ss[1:]) + ss[0]


# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
# print(reverse("ab")) 
# => "ba"
# print(reverse("computer")) 
# => "retupmoc"
# print(reverse(reverse("computer"))) 
# => "computer"