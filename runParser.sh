rm *.dat
rm tempdb

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

#Verify foreign key constraints
sqlite3 tempdb < constraints_verify.sql

#Add triggers
sqlite3 tempdb < trigger1_add.sql
sqlite3 tempdb < trigger2_add.sql
sqlite3 tempdb < trigger3_add.sql
sqlite3 tempdb < trigger4_add.sql
sqlite3 tempdb < trigger5_add.sql
sqlite3 tempdb < trigger6_add.sql
sqlite3 tempdb < trigger7_add.sql