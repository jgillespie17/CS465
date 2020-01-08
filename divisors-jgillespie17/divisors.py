def divisors(num):
    div = [1]
    if num == 1:
        return [num]
    i = div[0]
    for i in range(2, num) :
        if (num % i == 0):
            div.append(i)
    div.append(num)
    return div
