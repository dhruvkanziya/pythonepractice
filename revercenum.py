no = 123
rev = 0
while no!=0:
    digit = no% 10
    rev = no %10 +digit

no = no // 10

print("reverce  number is ",str(rev))