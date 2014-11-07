.mode columns
.headers off
.nullvalue NULL

--select distinct(item_id) in categories where count(item_id) = 4;

select item_id from items where currently = (select max(currently) from items);
