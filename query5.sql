.mode columns
.headers off
.nullvalue NULL

--select distinct(item_id) in categories where count(item_id) = 4;

select count(user_id) from auctionusers where rating> 1000 and user_id in (select seller_id from items);