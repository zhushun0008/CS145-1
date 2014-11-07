.mode columns
.headers off
.nullvalue NULL


select count(item_id) from items I1 
where item_id in (select item_id from categories group by item_id having count(item_id) =4);
