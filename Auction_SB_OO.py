from bidding_function import *
import numpy as np

# bid_history- possibly empty

def SB(price_format, bid_information):

    winner_to_pick = []
    bid_prices = [dic['BidFunction'] for dic in bid_information]
    for i in range(len(bid_information)):
        if bid_prices[i] == max(bid_prices):
            winner_to_pick.append(i)
            # return a list of indexes of winner location
    if len(winner_to_pick) > 1:
        winner = np.random.choice(winner_to_pick, 1)
        print "tie, randomly pick a winner: Bidder %s" % (winner[0] + 1)
    else:
        print "winner is bidder %d" % (winner_to_pick[0] + 1)

    if price_format == 1:
        price_to_pay = max(bid_prices)
        print "1st price auction,winner is paying %.2f" % price_to_pay

    elif price_format == 2:
        pr = bid_prices[:]  # copy pr content only
        pr.remove(max(pr))
        price_to_pay = max(pr)
        print "2nd price auction, winner is paying %.2f" % price_to_pay

    else:
        print "this function only supports 1st and 2nd auction"

    bid_history = [{'Round': 1, 'Value': None, 'Bids': bid_prices}]
    return bid_history, price_to_pay


# In[716]:

def has_winner(BH):
    # bid ends, all 0 or 1 bidder left in the last round,
    # bid history completes
    return (sum(BH[-1]['Bids']) in [0, 1])


def find_winner(BH):
    # given bidding history, return the winner index
    # if in last round, there is one person bid
    if (sum(BH[-1]['Bids']) == 1):
        return True, BH[-1]['Bids'].index(1)
    else:
        winners = []
        for i in range(len(BH[-2]['Bids'])):
            if BH[-2]['Bids'][i] == 1:
                winners.append(i)
    return False, np.random.choice(winners, 1)[0]


def find_winning_price(BH, win_on_last_round, price_format):
    # round n has zero bids, n-1 has more than 1 bids(tie), bidder pay n-1 price (disregard 1st & 2nd price)
    if not win_on_last_round:
        return BH[-2]['Value']
    # there is one bidder in last round, given 1st price, 2nd price, pay accordingly
    else:
        return BH[-price_format]['Value']


def bid(current_bid, value):
    if value >= current_bid:
        return 1
    else:
        return 0


def OO(price_format, bid_history, value_to_increment, bidder_information):
    # building and updating bid_history, until it finds and return the winner and price to pay

    print "%s price auction" % price_format

    # if no winner created, keep updating bid_history
    while not has_winner(bid_history):  # loop ends until has_winner= True

        # Initiates dic for next round
        rd = bid_history[-1]['Round']
        current_bid = bid_history[-1]['Value']
        current_bid = current_bid + value_to_increment

        next_dic = {"Round": (rd + 1),
                    "Value": round(current_bid, 2),
                    'Bids': [0] * len(bidder_information)}
        bid_history.append(next_dic)

        BidF=[0]*len(bidder_information)
        for b in range(len(bid_history[0]['Bids'])):
            # update bidding history
            BidF[b] = bidder_information[b]['BidFunction']
            value = BidF[b](current_bid, bid_history)
            bid_history[-1]['Bids'][b] = bid(current_bid, value)

    # once loop ends (we have a winner, find winner and price)
    win_on_last_round, winner = find_winner(bid_history)
    price_to_pay = find_winning_price(bid_history, win_on_last_round, price_format)

    print 'winner is bidder %s, paying %s' % (winner + 1, price_to_pay)
    print "total %d rounds \n----------" % bid_history[-1]['Round']
    return bid_history, price_to_pay


def auction_evaluator(price_format,
                      auction_format,
                      bid_history,
                      bidder_information,
                      value_to_bid=None,
                      value_to_increment=None):
    if auction_format == 'SB':
        bid_history, price_to_pay = SB(price_format, bidder_information)

    elif auction_format == 'OO':  # run recursively
        if bid_history is None:
            start_bidding = {
                'Round': 1,
                'Value': value_to_bid,
                'Bids': [0] * len(bidder_information)}
            for b in range(len(bidder_information)):
                value = bidder_information[b]['BidFunction'](value_to_bid, bid_history)
                start_bidding['Bids'][b] = bid(value_to_bid, value)
            bid_history = [start_bidding]

        # given bid_history, evaluate OO bids
        bid_history, price_to_pay = OO(price_format, bid_history,
                                       value_to_increment, bidder_information)
    print bid_history
    return bid_history, price_to_pay


###############
# in the case of the sealed bid, the BidF should return the bid of the bidder
# given the 2nd price auction, the bidder should always bid its value
# the revenue should always be the 2nd largest from that bid


# given the number of bidders, create BI, a list of dictionary



def get_args(lamb_ls=[1, 10], num_bidders=[2, 5, 10]):
    combo_lamb_bidders = [(l, n) for l in lamb_ls for n in num_bidders]
    return combo_lamb_bidders


def get_BidF_exponential(lamb, num_bidders):
    # return the the list of bidding price for each bidder,
    # given lambda exponential distribution and num_bidder

    BidF = []
    for rnd in np.random.exponential(1.0 / lamb, num_bidders):
        BidF.append(rnd)
    return BidF


