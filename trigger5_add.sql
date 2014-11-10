--Any new bid for a particular item must have a higher amount than any of the previous bids for that particular item.
--Add a trigger to block/reject bids that are lower than the max bid_amount in the bids table for that particular item_id.This trigger is added as 'trigger5_add.sql'

PRAGMA foreign_keys= ON;
drop trigger if exists trigger5;
create trigger trigger5
before insert on bids
for each row
when exists (select * from items where item_id=new.item_id and new.bid_amount<=currently)
begin
     SELECT raise(rollback, "The bid amount is lower than the highest bid for the item. Please enter a bid higher than the highest bid to be in contention");
end;