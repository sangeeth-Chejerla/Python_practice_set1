"""wow this process is great ,greedy sure is good .
haaha things get if i learn programming i guess even i dont thing i can solve in my second glance ,may i am getting better
if solve everyday i might be good at this but i mind is the villan here.
he always dragging me down and killing me inside with alll my misery on"""

def coin_change(total_number,coinlist):
    N = total_number
    coinlist.sort()
    coin_len = len(coinlist)-1
    while True:
        coin_value = coinlist[coin_len]
        if N>= coin_value:
            print(coin_value)
            N=N-coin_value

        if N < coin_value:
            coin_len-=1

        if N==0:
            break

coin_list = [1,2,5,10,20,50,100,1000]
coin_change(122,coin_list)


