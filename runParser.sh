rm *.dat

#Generate .dat files
python himanshu_parser.py /usr/class/cs145/project/ebay_data/items-*.json

#Remove duplicate rows from tables below
sort bids_table.dat | uniq > bids_table_uniq.dat
sort auctionusers_table.dat | uniq > auctionusers_table_uniq.dat
sort items_table.dat | uniq > items_table_uniq.dat
sort categories_table.dat | uniq > categories_table_uniq.dat

#Load sql schema into database
sqlite3 tempdb < create.sql
sqlite3 tempdb < load.txt

