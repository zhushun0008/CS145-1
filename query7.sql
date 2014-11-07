.mode columns
.headers off
.nullvalue NULL

select count(distinct(category)) from categories where item_id in (select distinct(item_id) from bids group by item_id having max(bid_amount)>100 and max(bid_amount)<>'NULL');