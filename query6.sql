.mode columns
.headers off
.nullvalue NULL

--select distinct(item_id) in categories where count(item_id) = 4;

select count(distinct(seller_id)) from items where seller_id in (select user_id from bids);