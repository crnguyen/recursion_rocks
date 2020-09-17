# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible outcomes from flipping a coin N times.
# Input type: Integer 
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"

# def coinflip(n):
#   if n <= 0:
#     return 0
#   else:
#     flip = coinflip(["H","T"])
#     if flip == "H":
#       return 1 + coinflip(n-1)
#     else:
#       return 0 + coinflip(n-1)

# print(coinflip(2)) 
# => ["HH", "HT", "TH", "TT"]

f = 6
flips = list('-' * f)
def coinflip(m):
    global flips
    if m == 1:
        flips[-m] = 'T'
        print( ''.join(flips))
        flips[-m] = 'H'
        print( ''.join(flips))
    else:
        flips[-m] = 'T'
        coinflip(m-1)
        flips[-m] = 'H'
        coinflip(m-1)
print(coinflip(6))