
"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS145 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub
import string

columnSeparator = "<>"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Set Trace for debugging
"""
def set_trace():
    from IPython.core.debugger import Pdb
    import sys
    Pdb(color_scheme='Linux').set_trace(sys._getframe().f_back)


"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Returns the location if location is present. Else, it returns 'NULL'.
"""

def bidder_location_presentabsent(dict_bid):
    if 'Location' in dict_bid:
        return str(dict_bid['Location']).strip()
    else:
        return 'NULL'

"""
Returns the country if country is present. Else, it returns 'NULL'.
"""

def bidder_country_presentabsent(dict_bid):
    if 'Country' in dict_bid:
        return str(dict_bid['Country']).strip()
    else:
        return 'NULL'

"""
Returns the buy_price if present. Else, it returns 'NULL'.
"""

def buy_price_presentabsent(dict_bid):
    if 'Buy_Price' in dict_bid:
        return str(dict_bid['Buy_Price']).strip()
    else:
        return 'NULL'



"""
Function that cleans up issues with quotes
"""

def quote_clean(string_val):
    return '\"'+string.replace(string_val,'\"','\"\"')+'\"'

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    f_usertable=open('auctionusers_table.dat','a')
    f_bidtable=open('bids_table.dat','a')
    f_categorytable=open('categories_table.dat','a')
    f_maintable=open('items_table.dat','a')

    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        for item in items:
            #set_trace()
            #Populating item-category table
            # ItemID<>category_name
            for category in item['Category']:
                f_categorytable.write(str(item['ItemID'].strip() + columnSeparator + category.strip() + '\n'))

            #Populating Item-bidder table
            # ItemID<>Bidder_User_id<>Time_of_bid<>Amount
            if item['Bids'] == None:
                pass
		#f_bidtable.write(str(item['ItemID'].strip() + columnSeparator + 'NULL' + columnSeparator + 'NULL'+ columnSeparator + 'NULL' +'\n'))
            else:
                #set_trace()
                for bidder in item['Bids']:
                    f_bidtable.write(str(item['ItemID']).strip()+ columnSeparator + str(bidder['Bid']['Bidder']['UserID']).strip() +columnSeparator + transformDttm(bidder['Bid']['Time']).strip() +columnSeparator + transformDollar(str(bidder['Bid']['Amount']).strip()) + '\n')

            #Populating usertable
            # UserID <> Rating <> Location <> Country

            f_usertable.write(str(item['Seller']['UserID']).strip() + columnSeparator + str(item['Seller']['Rating']).strip() + columnSeparator + quote_clean(str(item['Location']).strip()) + columnSeparator + quote_clean(str(item['Country']).strip()) + '\n')

            if item['Bids'] == None:
                pass
            else:
                try:
                    for bidder in item['Bids']:
                        line_to_write=str(bidder['Bid']['Bidder']['UserID']).strip() + columnSeparator + str(bidder['Bid']['Bidder']['Rating']).strip() + columnSeparator + quote_clean(bidder_location_presentabsent(bidder['Bid']['Bidder'])) + columnSeparator + quote_clean(bidder_country_presentabsent(bidder['Bid']['Bidder'])) + '\n'
                        f_usertable.write(line_to_write)
                except:
                    set_trace()

            #Populating the main_table
            # ItemID<>Name<>Currently<>BuyPrice<>Firstbid<>Noofbids<>Started<>Ends<>Description<>SellerID

            #"ItemID", "Name", "Currently", "First_Bid", "Number_of_Bids", "00Bids00", "00Location00", "00Country00", "Started", "Ends", "Seller", "Description" , "Buy_Price"
            line_to_write=str(item['ItemID']).strip() + columnSeparator + quote_clean(str(item['Name']).strip())+ columnSeparator + str(transformDollar(item['Currently'])).strip() + columnSeparator + str(transformDollar(item['First_Bid'])).strip()+ columnSeparator + str(item['Number_of_Bids']).strip()+ columnSeparator + str(transformDttm((item["Started"]))).strip() + columnSeparator+ str(transformDttm(item["Ends"])).strip()+ columnSeparator+ str(item["Seller"]['UserID']).strip()+ columnSeparator + quote_clean(str(item['Description']).strip()) + columnSeparator+ str(buy_price_presentabsent(item)).strip() + '\n'
            f_maintable.write(line_to_write)

    f_usertable.close()
    f_bidtable.close()
    f_categorytable.close()
    f_maintable.close()

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print "Success parsing " + f

if __name__ == '__main__':
    main(sys.argv)
