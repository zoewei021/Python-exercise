
class RMB(object):
    def __init__(self,Money):
        self.Money = Money
    def __nonzero__(self):
        return bool(self.Money)
    def update(self):
        input_mon= input("Please input the new value:\n")
        self.Money=input_mon

    def up2(self):
        pass
    def up3(self):
        pass

    def moneyfmt(self):

        Money_str = str(self.Money)
        if "-" not in  Money_str :
            Money_li = list( Money_str.split('.')[0])
        else:
            Money_li= list( Money_str.split('.')[0])[1:]
        Money_len=len(Money_li)
        if Money_len < 3:
            if "-" not in str(self.Money):
                return ("$%.2f" % self.Money)
            else:
                return ("-$%.2f" % abs(self.Money))
        else:
            rev = "%.2f" % self.Money
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
                Money_str2="$" + ''.join(Money_li) + rev[-3:]
                return Money_str2
            else:
                Money_str2="-$" + ''.join(Money_li) + rev[-3:]
                return Money_str2

t=input("Please input the money:\n")
t1=RMB(t)
t1.moneyfmt()
print(t1.moneyfmt())
t1.update()
print(t1.moneyfmt())


