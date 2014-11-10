--Blocks bids placed by the seller of the item itself. Added a trigger to block insertion (before) on bids table where the user_id for the item_id is already listed as seller_id in table 'items' for the same item_id. 

PRAGMA foreign_keys= ON;
drop trigger if exists trigger2;
create trigger trigger2
before insert on bids
for each row
when exists (select * from items where seller_id=new.user_id and item_id=new.item_id)
begin
     SELECT raise(rollback, "You are not allowed to bid on an item you are selling.");
end;