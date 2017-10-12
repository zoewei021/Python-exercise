#!/user/bin/env python
#zoe
def RMB(Money):

    Money_str = str(Money)
    if "-" not in  Money_str :
        Money_li = list( Money_str.split('.')[0])
    else:
        Money_li= list( Money_str.split('.')[0])[1:]
    Money_len=len(Money_li)
    if Money_len < 3:
        if "-" not in str(Money):
            return ("$%.2f" % Money)
        else:
            return ("-$%.2f" % abs(Money))
    else:
        rev = "%.2f" % Money
        n,x = divmod(Money_len, 3)
        if x != 0:
            count = n
        else:
            count = n - 1
        i = 0
        while i < count:
             Money_li.insert((Money_len - 3), ',')
             i += 1
             Money_len -= 3

        if "-" not in rev:
            Money_str2="+$" + ''.join(Money_li) + rev[-3:]
            return Money_str2
        else:
            Money_str2="-$" + ''.join(Money_li) + rev[-3:]
            return Money_str2

Mon = input("Please input the money:\n")
mon2 = RMB(Mon)
print(mon2)

