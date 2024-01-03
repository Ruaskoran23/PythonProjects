#working with functions to calculate overtime pay

#file created on 08/11/23 08:23

def computepay(h, r):
    h = input("Enter Hours: ")
    r = input("Enter Rate: ")
    hr = float(h)
    rt = float(r)
    if (hr > 40): #calculate overtime and regular time pay
        reg = hr * rt
        ot = (hr - 40) * (rt * 0.5)
        pay = reg + ot
    else:
        pay = hr * rt
    
    return pay
p = computepay(0,0)
print('Pay ', p)
