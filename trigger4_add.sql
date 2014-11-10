--In every auction, the Number of Bids attribute corresponds to the actual number of bids for that particular item.
--Add a trigger to update the number_of_bids in items table after every insert to the bids table for each item_id. This trigger is added as 'trigger4_add.sql'

PRAGMA foreign_keys= ON;
drop trigger if exists trigger4;
create trigger trigger4
after insert on bids
for each row
begin
     update items set number_of_bids=number_of_bids+1 where item_id=new.item_id;
end;