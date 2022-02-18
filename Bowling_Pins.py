def bowling_pins(arr):
    pins = [" " if x in arr else "I" for x in range(10,0,-1)]
    idx = 0
    mount = ""
    for x in range(4,0,-1):
        #mount += " "*(4-x)
        tmp = ""
        for y in range(x,0,-1):
            tmp += f"{pins[idx + y - 1]} "
        idx += x
        mount += tmp.center(7) + "\n"
    return mount
    

print(bowling_pins([3,5,9]))