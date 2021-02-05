def main(num):
    m = num%1
    intpart = num - m
    m1 = (0,1)
    m2 = (1,1)
    w = 0
    for i in range(10000):
        mediant = ((m1[0]+m2[0])/(m1[1]+m2[1]))
        mediantt = ((m1[0]+m2[0]), (m1[1]+m2[1]))
        if mediant>m:
            m2 = ((m1[0]+m2[0]), (m1[1]+m2[1]))
        elif mediant<m:
            m1 = ((m1[0]+m2[0]), (m1[1]+m2[1]))
        else:
            break
    return f"{int(intpart*mediantt[1]+mediantt[0])}/{mediantt[1]}", (int(intpart*mediantt[1]+mediantt[0]),mediantt[1])
