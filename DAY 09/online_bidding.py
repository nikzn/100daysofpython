import logo
print(logo.logo)
print("\n"*5)
bidList={}
isContinue =True



def find_the_max_bidder_details(bidList):
    maxBid = 0
    maxBidder = ''
    for bid in bidList:

        if maxBid < bidList[bid]:
            maxBid = bidList[bid]
            maxBidder = bid

    print(f"{maxBidder} won the bid with ${maxBid}")



while isContinue ==True:
    name = input("What is your name?:")
    bid =int(input("what is your Bid?:$"))

    bidList[name]=bid
    yesOrno = input("is there any other bidders,type 'yes' for Yes and 'no' for No ").lower()
    print("\n" * 100)

    if(yesOrno == 'no'):
       isContinue = False
       find_the_max_bidder_details(bidList)




