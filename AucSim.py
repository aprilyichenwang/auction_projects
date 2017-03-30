import numpy as np
import matplotlib.pyplot as plt


def price_1st_BF_uniform0_1(N):
    V = np.random.uniform(0, 1, N)  # V is an array
    B_1= V- V/N
    Revenue_1 = max(B_1)
    return np.mean(V),np.mean(B_1), Revenue_1


def price_2nd_BF_uniform0_1(N):
    V = np.random.uniform(0, 1, N)  # V is an array
    B_2= V
    B_2.sort()
    Revenue_2 = B_2[-2]
    return np.mean(V),np.mean(B_2), Revenue_2


def price_2nd_BF_uniform5_10(N):
    V = np.random.uniform(5, 10, N)  # V is an array
    B_2= V
    B_2.sort()
    Revenue_2 = B_2[-2]
    return np.mean(V),np.mean(B_2), Revenue_2


def simulate_BF_1st(N, iters=20000):
    pairs=[]
    for i in range(iters):
        pairs.append(price_1st_BF_uniform0_1(N))
    values=zip(*pairs)[0]
    bidding_functions=zip(*pairs)[1]
    revenue=zip(*pairs)[2]
    print "N=%d, E(Rev) of 1st price is %.2f"% (N, np.mean(revenue))
    print "N=%d, STD(Rev) of 1st price is %.2f"% (N, np.std(revenue))
    print "---------"
    return values, bidding_functions, revenue



def simulate_BF_2nd(N, iters=20000):
    pairs=[]
    for i in range(iters):
        pairs.append(price_2nd_BF_uniform0_1(N))
    values=zip(*pairs)[0]
    bidding_functions=zip(*pairs)[1]
    revenue=zip(*pairs)[2]
    print "N=%d, E(Rev) of 2nd price is %.2f"% (N, np.mean(revenue))
    print "N=%d, STD(Rev) of 2nd price is %.2f"% (N, np.std(revenue))
    print "----------"
    return values, bidding_functions,revenue


def simulate_BF_2nd_5_10(N, iters=20000):
    pairs=[]
    for i in range(iters):
        pairs.append(price_2nd_BF_uniform5_10(N))
    values=zip(*pairs)[0]
    bidding_functions=zip(*pairs)[1]
    revenue=zip(*pairs)[2]
    print "N=%d, E(Rev) of 2nd price is %.2f"% (N, np.mean(revenue))
    print "N=%d, STD(Rev) of 2nd price is %.2f"% (N, np.std(revenue))
    print "----------"
    return values, bidding_functions,revenue



def make_bid_function_plot(simulation_type):
    if simulation_type=='1st price, Unif[0,1]':
        values_2, bidding_functions_2, revenue_2=simulate_BF_1st(2)
        values_5, bidding_functions_5, revenue_5 = simulate_BF_1st(5)
        values_10, bidding_functions_10, revenue_10 = simulate_BF_1st(10)

    elif simulation_type=='2nd price, Unif[0,1]':
        values_2, bidding_functions_2, revenue_2=simulate_BF_2nd(2)
        values_5, bidding_functions_5, revenue_5 = simulate_BF_2nd(5)
        values_10, bidding_functions_10, revenue_10 = simulate_BF_2nd(10)

    elif simulation_type=='2nd price, Unif[5,10]':
        values_2, bidding_functions_2, revenue_2 = simulate_BF_2nd_5_10(2)
        values_5, bidding_functions_5, revenue_5 = simulate_BF_2nd_5_10(5)
        values_10, bidding_functions_10, revenue_10 = simulate_BF_2nd_5_10(10)

    plt.plot(values_2, bidding_functions_2,label='N=2')
    plt.plot(values_5, bidding_functions_5,label='N=5')
    plt.plot(values_10, bidding_functions_10,label='N=10')
    plt.legend(['N = 2','N = 5','N = 10'],loc=3)
    plt.title('Auction %s'%simulation_type)
    plt.xlabel('value')
    plt.ylabel('bidding price')
    plt.show()


# Question 1  (a) (b) given uniform[0,1] N=2,5,10
# each plot will plot N=2,5,10 in one plot
make_bid_function_plot(simulation_type='1st price, Unif[0,1]')
make_bid_function_plot(simulation_type='2nd price, Unif[5,10]')

make_bid_function_plot(simulation_type='2nd price, Unif[0,1]')





