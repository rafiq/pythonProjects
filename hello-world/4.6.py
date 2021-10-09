def computepay(h, r):
    if (h > 40):
        extraHRS = h - 40
        newRate = r * 1.5
        return (40 * r) + (extraHRS * newRate)
    else: return h * r

hrs = input("Enter Hours:")
hrsNum = float(hrs)
rate = input("Enter the rate:")
rateNum = float(rate)

p = computepay(hrsNum, rateNum)
print("Pay", p)

