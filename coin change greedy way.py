""""""

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


