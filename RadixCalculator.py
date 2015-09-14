alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
input = "33"
radix = 7.5

input = input.upper( )
res = 0
for x in input:
    d = alphabet.find( x )
    if d < 0 or d > radix:
        print "The given number is not in base ", radix
        res = -1
        break
    else:
        res = radix * res + d

if res > -1:
    print input, "in base", radix, "is", res, "in base 10."
