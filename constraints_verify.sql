--2. All sellers and bidders must exist as users
select user_id from bids where user_id not in (select user_id from auctionusers);
select seller_id from items  where seller_id not in (select user_id from auctionusers);

--4. Every bid must correspond to an actual item
select item_id from bids where item_id not in (select io.item_id from items io);

--5. The items for a given category must all exist
select item_id from categories where item_id not in (select io.item_id from items io);